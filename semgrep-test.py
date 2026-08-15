# semgrep-secure-test.py

import hashlib
import os
import pickle
import sqlite3
import subprocess
from pathlib import Path


# 1. Command Injection
# Avoid shell execution with untrusted input.
def command_injection(user_input):
    allowed_commands = {
        "status": ["echo", "status"],
        "version": ["echo", "version"],
    }

    if user_input not in allowed_commands:
        raise ValueError("Invalid command")

    return subprocess.run(
        allowed_commands[user_input],
        check=True,
        capture_output=True,
        text=True,
    )


# 2. Shell Command Injection
# Do not use shell=True with user-controlled input.
def shell_injection(user_input):
    return subprocess.run(
        ["echo", user_input],
        check=True,
        capture_output=True,
        text=True,
    )


# 3. SQL Injection
# Use parameterised SQL queries.
def sql_injection(username):
    connection = sqlite3.connect("test.db")

    query = "SELECT * FROM users WHERE username = ?"

    try:
        return connection.execute(query, (username,)).fetchall()
    finally:
        connection.close()


# 4. Hardcoded Secret
# Read secrets from environment variables instead.
API_KEY = os.environ.get("API_KEY")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")


# 5. Weak Hashing
# Use a password-hashing algorithm such as Argon2 or bcrypt.
# Example using PBKDF2 from the Python standard library.
def secure_password_hash(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600_000,
    ).hex()


# 6. Insecure Deserialization
# Do not use pickle.loads() on untrusted data.
# JSON is safer for data interchange.
import json


def secure_deserialization(data):
    return json.loads(data)


# 7. Path Traversal
# Restrict access to a specific directory.
def path_traversal(filename):
    base_directory = Path("/tmp/safe-files").resolve()
    requested_file = (base_directory / filename).resolve()

    if base_directory not in requested_file.parents:
        raise ValueError("Invalid file path")

    return requested_file.read_text(encoding="utf-8")


# 8. Code Execution with eval()
# Do not evaluate user-controlled Python expressions.
def safe_eval(user_input):
    allowed_values = {
        "one": 1,
        "two": 2,
        "three": 3,
    }

    if user_input not in allowed_values:
        raise ValueError("Invalid value")

    return allowed_values[user_input]


# 9. Code Execution with exec()
# Avoid dynamic code execution entirely.
def safe_exec(user_input):
    allowed_actions = {
        "start": "Application started",
        "stop": "Application stopped",
    }

    if user_input not in allowed_actions:
        raise ValueError("Invalid action")

    return allowed_actions[user_input]


# 10. Debug Mode
# Debug mode should be disabled in production.
def start_application(app):
    app.run(debug=False)


if __name__ == "__main__":
    print("Secure Semgrep test application")
