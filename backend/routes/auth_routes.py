from flask import Blueprint
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from flask import request
from services.auth_service import register_user
from services.auth_service import login_user

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)

@auth_bp.route("/test", methods=["GET"])
def test():
    return jsonify({
        "message": "Authentication Route Working"
    })

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    response, status = register_user(data)

    return jsonify(response), status

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    response, status = login_user(data)

    return jsonify(response), status

@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    return jsonify({
        "user_id": user.user_id,
        "name": user.full_name,
        "email": user.email,
        "phone": user.phone,
        "role": user.role
    })