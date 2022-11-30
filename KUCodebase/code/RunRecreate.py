import shlex, subprocess, cryptography

# Recreate runs from paper
env_name = "Humanoid-v2"
target_entropy = "-2.0"

if target_entropy:
    commands = [f"python main.py -info drq -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method sac -target_entropy {target_entropy} -target_drop_rate 0.01 -layer_norm 1",
                f"python main.py -info redq -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method redq -target_entropy {target_entropy}",
                f"python main.py -info sac -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10  -gpu_id 0 -updates_per_step 20 -method sac -target_entropy {target_entropy}"]

else:     
    commands = [f"python main.py -info drq -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method sac -target_drop_rate 0.01 -layer_norm 1",
                f"python main.py -info redq -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method redq",
                f"python main.py -info sac -env {env_name} -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10  -gpu_id 0 -updates_per_step 20 -method sac"]


commands.append("python main.py -info redq -env Hopper-v2 -seed 0 -eval_every 1000 -frames 100000 -eval_runs 10 -gpu_id 0 -updates_per_step 20 -method redq -target_entropy -1")

if __name__ == "__main__":
    for command in commands:
        args = shlex.split(command)
        subprocess.Popen(args)