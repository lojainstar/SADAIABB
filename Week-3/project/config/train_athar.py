
# Dataset name
dataset = 'athar'

out_dir = 'out-athar'

# model size
n_layer = 4
n_head = 4
n_embd = 128

#training
batch_size = 32
block_size = 128

learning_rate = 3e-4
init_from = 'resume'
out_dir = 'out-athar'
max_iters = 5000


#evaluation
eval_interval = 200
eval_iters = 100

# logging
log_interval = 10
