import sys
import os
import platform
import subprocess

if len(sys.argv) < 3:
    print("Usage: python write-sys-env-var.py <ENV_VAR_NAME> <VALUE>")
    sys.exit(1)

env_var_name = sys.argv[1]
value = sys.argv[2]

def set_env_windows(name, val):
    # User variable
    subprocess.run(["setx", name, val, "/M"])
    print(f"Set Windows system variable (requires admin privileges) {name} = {val}")
    # For user variable (does not require admin privileges), uncomment:
    # subprocess.run(["setx", name, val])
    # print(f"Set Windows user variable {name} = {val}")

def set_env_linux(name, val):
    bashrc_path = os.path.expanduser("~/.bashrc")
    export_line = f'\nexport {name}="{val}"\n'
    with open(bashrc_path, "a") as f:
        f.write(export_line)
    print(f'Appended to {bashrc_path}: {export_line.strip()}')
    print('Run `source ~/.bashrc` or restart your terminal to apply changes.')

if platform.system() == "Windows":
    set_env_windows(env_var_name, value)
else:
    set_env_linux(env_var_name, value)
