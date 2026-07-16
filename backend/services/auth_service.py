import bcrypt
from flask_jwt_extended import create_access_token
from models import db
from models.user import User
from utils.jwt_helper import generate_token

from utils.validators import (
    is_valid_email,
    is_valid_password
)

def register_user(data):
    full_name = data.get("full_name")
    email = data.get("email")
    password = data.get("password")
    phone = data.get("phone")

    if not is_valid_email(email):
        return {"error": "Invalid email"}, 400

    if not is_valid_password(password):
        return {"error": "Weak password"}, 400

    existing = User.query.filter_by(email=email).first()

    if existing:
        return {"error": "Email already exists"}, 409

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    user = User(
        full_name=full_name,
        email=email,
        password_hash=password_hash,
        phone=phone
    )

    db.session.add(user)
    db.session.commit()

    return {
        "message": "Registration Successful"
    }, 201

def login_user(data):
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return {"error": "Invalid Email"}, 401

    if not bcrypt.checkpw(
        password.encode("utf-8"),
        user.password_hash.encode("utf-8")
    ):
        return {"error": "Invalid Password"}, 401

    token = generate_token(user.user_id)

    return {
        "message": "Login Successful",
        "access_token": token,
        "user": {
            "user_id": user.user_id,
            "name": user.full_name,
            "email": user.email
        }
    }, 200