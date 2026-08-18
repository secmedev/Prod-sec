# semgrep-test.py
# INTENTIONALLY VULNERABLE - FOR SECURITY TESTING ONLfY

import hashlib
import os
import sqlite3
import subprocess


# 1. Command injection
def run_command(user_input):
    os.system(user_input)


# 2. Shell injection
def execute_command(user_input):
    subprocess.run(user_input, shell=True)


# 3. SQL injection
def get_user(username):
    db = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return db.execute(query).fetchall()


# 4. Dangerous eval
def calculate(user_input):
    return eval(user_input)


# 5. Weak cryptographic hash
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# 6. Hardcoded credential
PASSWORD = "TestPassword123!"
API_KEY = "test-api-key-123456"


if __name__ == "__main__":
    print("Semgrep security test")
