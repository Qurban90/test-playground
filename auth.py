"""Authentication module."""
import hashlib
import os

SECRET_KEY = "supersecret123"

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    return query

def check_admin(user):
    if user["role"] == "admin":
        return True

def read_config(path):
    f = open(path)
    data = f.read()
    return data

def process_users(users):
    admins = []
    for i in range(len(users)):
        for j in range(len(users)):
            if users[i]["role"] == "admin":
                admins.append(users[i])
    return admins
