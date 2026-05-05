# 🧠 Arabic nanoGPT Project (ATHAR)

## 📌 Overview

في هذا المشروع قمت ببناء نموذج **GPT مصغّر من الصفر** لتوليد نصوص عربية باستخدام بيانات من مجموعة **ATHAR**.
المشروع يغطي كامل الـ pipeline: من تجهيز البيانات إلى تدريب النموذج ثم توليد النص.

---

## ⚙️ What I Implemented

### 1. Data Preparation

* استخدمت بيانات عربية من ATHAR (حوالي 40,000 نص)
* دمجت النصوص في ملف واحد
* قسمتها إلى:

  * 90% تدريب
  * 10% تحقق (Validation)

---

### 2. Tokenizer (مهم 🔥)

* استخدمت **SentencePiece Tokenizer (BPE)**
* تم تدريبه من الصفر على البيانات العربية الخاصة بالمشروع
* حجم القاموس (Vocabulary Size): **8000**

### 💡 فكرة التوكنايزر:

بدل ما النموذج يتعامل مع كلمات كاملة، يتم تقسيم الكلمات إلى **وحدات أصغر (Subwords)**
مثال:

* "المؤمنين" → ["الم", "ؤمن", "ين"]

📌 الفائدة:

* التعامل مع الكلمات النادرة
* دعم اللغة العربية بشكل أفضل
* تقليل حجم القاموس

---

### 3. Data Encoding

* تم تحويل النص إلى أرقام باستخدام التوكنايزر
* حفظ البيانات في ملفات:

  * `train.bin`
  * `val.bin`

---

### 4. Model Training

* تدريب نموذج GPT صغير باستخدام:

  * Attention Mechanism
  * Softmax
* تم تتبع:

  * Training Loss
  * Validation Loss

📉 النموذج تحسن مع الوقت (loss نزل من ~9 إلى ~3)

---

### 5. Sampling (Text Generation)

* استخدمت `sample.py` لتوليد نصوص جديدة
* مثال:

```bash
python sample.py --start="امير المؤمنين"
```

---

## 🧪 Evaluation

تم التقييم باستخدام:

* **Validation Loss داخل التدريب**

📌 لا يوجد ملف evaluation منفصل لأن التقييم مدمج داخل training loop

---

## 📂 Project Structure

```
nanoGPT/
│
├── train.py
├── prepare.py
├── sample.py
├── model.py
├── configurator.py
│
├── data/athar/
│   └── meta.pkl
│
├── tokenizer/
│   ├── athar_sp.model
│   └── athar_sp.vocab
│
└── out-athar/
```

---

## 🎯 What I Learned

* بناء Tokenizer من الصفر
* تحويل النص إلى بيانات رقمية قابلة للتدريب
* فهم آلية Attention داخل GPT
* تدريب نموذج Language Model ومتابعة الـ loss
* التعامل مع مشاكل مثل:

  * عدم حفظ checkpoint
  * أخطاء المسارات (FileNotFound)

---

## 🚀 Conclusion

تم بناء نموذج GPT عربي بسيط يعمل من الصفر، مع tokenizer مخصص، ويستطيع توليد نصوص عربية بناءً على prompt.

---
