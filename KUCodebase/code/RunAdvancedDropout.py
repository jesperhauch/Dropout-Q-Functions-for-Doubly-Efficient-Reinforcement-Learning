import shlex, subprocess, cryptography


# New enviornments for different drop_out rates
env_names = ['LunarLanderContinuous-v2', 'Pendulum-v1', 'Reacher-v2']
commands = []

for env_name in env_names:
    #command = f"python main.py -info drq_advanced -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method sac -layer_norm 1 -advanced_dropout 1"
    command = f"python main.py -info drq -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method sac -target_drop_rate 0.01 -layer_norm 1"
    commands.append(command)

if __name__ == "__main__":
    for command in commands:
        args = shlex.split(command)
        subprocess.Popen(args)