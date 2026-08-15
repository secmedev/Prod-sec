# semgrep-test.py

import subprocess

def run_command(user_input):
    # Deliberately vulnerable: user-controlled input reaches a shell.
    subprocess.run(user_input, shell=True)

user_input = input("Enter command: ")
run_command(user_input)
