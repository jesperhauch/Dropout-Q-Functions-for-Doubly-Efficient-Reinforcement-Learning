import shlex, subprocess, cryptography


# New enviornments for different drop_out rates
env_name = "Pendulum-v1"
commands = []
dropout_rates = [0.001, 0.005, 0.01, 0.1]

commands = [f"python main.py -info redq -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method redq",
            f"python main.py -info sac -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10  -gpu_id 0 -updates_per_step 20 -method sac"]


for d_rate in dropout_rates:
    command = f"python main.py -info drq -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method sac -target_drop_rate {d_rate} -layer_norm 1","
    commands.append(command)
        
# New enviornments for different drop_out rates
env_name = "Pendulum-v1"

if __name__ == "__main__":
    for command in commands:
        args = shlex.split(command)
        subprocess.Popen(args)