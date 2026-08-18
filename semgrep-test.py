# semgrep-test.py
# INTENTIONALLY VULNERABLE TEST CODE - DO NOT USE IN PRODUCTION

import jwt
import requests
import sqlite3
import subprocess
import yaml


# 1. Command Injection
def run_command(user_input):
    subprocess.run(user_input, shell=True)


# 2. SQL Injection
def find_user(username):
    db = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return db.execute(query).fetchall()


# 3. Server-Side Request Forgery (SSRF)
def fetch_url(url):
    return requests.get(url)


# 4. Weak TLS verification
def insecure_request(url):
    return requests.get(url, verify=False)


# 5. Hardcoded Secret
API_TOKEN = "test-secret-token-123456"


# 6. Weak JWT configuration
def create_token(user):
    return jwt.encode(
        {"user": user},
        "secret",
        algorithm="HS256"
    )


# 7. Unsafe YAML deserialization
def load_config(data):
    return yaml.load(data, Loader=yaml.Loader)


# 8. Dangerous eval
def calculate(expression):
    return eval(expression)


# 9. Debug mode
def start_app(app):
    app.run(debug=True)


if __name__ == "__main__":
    print("Semgrep vulnerability testing")
