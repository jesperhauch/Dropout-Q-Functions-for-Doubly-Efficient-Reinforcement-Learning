import shlex, subprocess, cryptography


# New enviornments for different drop_out rates
env_names = ['Hopper-v2', 'HalfCheetah-v2']
target_entropy = ["-1", "-3"]
commands = []
#dropout_rates = [0.001, 0.005, 0.01, 0.1]
lambdas = ["1", "5"]
seeds = [1, 0]

for i, env_name in enumerate(env_names):
    command = f"python main.py -info drq_lambda_{lambdas[i]} -env {env_name} -seed {seeds[i]} -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method sac -target_drop_rate 0.01 -layer_norm 1 -sparsity_th {lambdas[i]}"
    commands.append(command)
    command = f"python main.py -info sac_lambda_{lambdas[i]} -env {env_name} -seed {seeds[i]} -eval_every 1000 -frames 100000 -eval_runs 10  -gpu_id 0 -updates_per_step 20 -method sac -target_entropy {target_entropy[i]} -sparsity_th {lambdas[i]}"
    commands.append(command)
    command = f"python main.py -info drq_advanced_8_lambda_{lambdas[i]} -env {env_name} -seed {seeds[i]} -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method sac -layer_norm 1 -advanced_dropout 1 -reduction 8 -sparsity_th {lambdas[i]}"
    commands.append(command)
        
if __name__ == "__main__":
    for command in commands:
        args = shlex.split(command)
        subprocess.Popen(args)