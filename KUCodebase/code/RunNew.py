import shlex, subprocess, cryptography


# New enviornments for different drop_out rates
env_name = 'Hopper-v2'
target_entropy = "-1"
commands = []
#dropout_rates = [0.001, 0.005, 0.01, 0.1]
lambdas = ["1", "3"]

for lambda_ in lambdas:
    #command = f"python main.py -info drq_lambda_{lambda_} -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method sac -target_drop_rate 0.01 -layer_norm 1 -sparsity_th {lambda_}"
    #commands.append(command)
    #command = f"python main.py -info sac_lambda_{lambda_} -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10  -gpu_id 0 -updates_per_step 20 -method sac -target_entropy {target_entropy} -sparsity_th {lambda_}"
    #commands.append(command)
    command = f"python main.py -info drq_advanced_8_lambda_{lambda_} -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method sac -layer_norm 1 -advanced_dropout 1 -reduction 8 -sparsity_th {lambda_}"
    commands.append(command)
        
if __name__ == "__main__":
    for command in commands:
        args = shlex.split(command)
        subprocess.Popen(args)