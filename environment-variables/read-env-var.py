import os
import sys

if len(sys.argv) < 2:
  print("Usage: python read-env-var.py <ENV_VAR_NAME>")
  sys.exit(1)

env_var_name = sys.argv[1]
value = os.getenv(env_var_name)

print(value)
