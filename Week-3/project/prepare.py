
from datasets import load_dataset
import tiktoken
import sentencepiece as spm
import numpy as np
import os
import pickle
#البيانات والحجم
dataset = load_dataset("mohamed-khalil/ATHAR", split="train")
dataset = dataset.select(range(40000))

texts = [x['arabic'] for x in dataset if x['arabic']]
full_text = "\n".join(texts)

os.makedirs("data/athar", exist_ok=True)

with open("data/athar/text.txt", "w") as f:
    f.write(full_text)

#استخدمت SentencePiece مع خوارزمية BPE لبناء tokenizer خاص باللغة العربية


spm.SentencePieceTrainer.train(
    input="data/athar/text.txt",
    model_prefix="tokenizer/athar_sp",
    vocab_size=8000,
    model_type="bpe",
    character_coverage=0.9995
)

print("TOKENIZER TRAINED")

sp = spm.SentencePieceProcessor()
sp.load("tokenizer/athar_sp.model")

tokens = sp.encode(full_text, out_type=int)
tokens = np.array(tokens, dtype=np.uint16)

split = int(0.9 * len(tokens))
train_ids = tokens[:split]
val_ids = tokens[split:]

train_ids.tofile("data/athar/train.bin")
val_ids.tofile("data/athar/val.bin")

meta = {"vocab_size": enc.n_vocab}
with open("data/athar/meta.pkl", "wb") as f:
    pickle.dump(meta, f)

