# Pendulum-v1

```
python main.py -info drq -env Pendulum-v1 -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 7 -updates_per_step 20 -method sac -target_entropy -1.0 -target_drop_rate 0.005 -layer_norm 1

python main.py -info redq -env Pendulum-v1 -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method redq -target_entropy -1.0

python main.py -info sac -env Pendulum-v1 -seed 0 -eval_every 1000 -frames 100000 \
-eval_runs 10  -gpu_id 0 -updates_per_step 20 -method sac -target_entropy -1.0
```
