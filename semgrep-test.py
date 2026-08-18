# semgrep-vulnerable-test.py
# INTENTIONALLY VULNERABLE TEST CODE - DO NOT USE IN PRODUCTION oaky

import hashlib
import os
import pickle
import sqlite3
import subprocess

# 1. OS Command Injection
def command_injection(user_input):
    os.system(user_input)


# 2. Shell Command Injection
def shell_injection(user_input):
    subprocess.run(user_input, shell=True)


# 3. SQL Injection
def sql_injection(username):
    connection = sqlite3.connect("test.db")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return connection.execute(query).fetchall()


# 4. Hardcoded Secret
API_KEY = "TEST_API_KEY_123456789"
DATABASE_PASSWORD = "TestPassword123!"


# 5. Weak Hashing
def weak_hash(password):
    return hashlib.md5(password.encode()).hexdigest()


# 6. Insecure Deserialization
def insecure_deserialization(data):
    return pickle.loads(data)


# 7. Path Traversal
def path_traversal(filename):
    with open("/tmp/" + filename, "r") as file:
        return file.read()


# 8. Code Execution with eval()
def unsafe_eval(user_input):
    return eval(user_input)


# 9. Code Execution with exec()
def unsafe_exec(user_input):
    exec(user_input)


# 10. Debug Mode
def start_application(app):
    app.run(debug=True)


# Test calls
if __name__ == "__main__":
    print("Semgrep vulnerability test file")
