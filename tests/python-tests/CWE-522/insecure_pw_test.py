#!/usr/bin/env python3

from flask import Flask, request
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from base64 import b64encode


app = Flask(__name__)
db = SQLAlchemy(app)


class InsecureUser(db.Model, UserMixin):
    __tablename__ = 'insecure_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))


class InsecureUser2(db.Model, UserMixin):
    __tablename__ = 'insecure_users_2'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = b64encode(password.decode('utf-8')).encode('utf-8')
        #self.password = b64encode(password)


class InsecureUser3(db.Model, UserMixin):
    __tablename__ = 'insecure_users_3'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.usename = username
        self.password = password


class SecureUser(db.Model, UserMixin):
    __tablename__ = 'secure_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)


class SecureUser2(db.Model, UserMixin):
    """Secure only because it is always used securely."""
    __tablename__ = 'secure_users_2'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))


@app.route("/register-insecure")
def reg1():
    username = request.json['username']
    password = request.json['password']

    user = InsecureUser(username, password)


@app.route("/register-secure")
def reg2():
    username = request.json['username']
    password = request.json['password']

    user = SecureUser(username, password)

@app.route("/register-secure-2")
def reg3():
    username = request.json['username']
    password = request.json['password']

    password_hash = generate_password_hash(password)

    user = SecureUser2(username, password_hash)

@app.route("/register-insecure-2")
def reg4():
    username = request.json['username']
    password = request.json['password']

    user = InsecureUser2(username, password)

@app.route("/register-insecure-3")
def reg5():
    username = request.json['username']
    password = request.json['password']

    password_hash = b64encode(password.decode('utf-8')).encode('utf-8')
    #password_hash = b64encode(password)

    user = InsecureUser3(username, password_hash)
