from flask import Blueprint, request, jsonify

from flask_jwt_extended import jwt_required, get_jwt_identity

from services.profile_service import (
    create_profile,
    get_profile,
    update_profile
)

profile_bp = Blueprint(
    "profile",
    __name__,
    url_prefix="/api/profile"
)

@profile_bp.route("/test")
def test():

    return jsonify({

        "message": "Profile Route Working"

    })


@profile_bp.route("", methods=["POST"])
@jwt_required()
def create():

    user_id = get_jwt_identity()

    data = request.get_json()

    response, status = create_profile(user_id, data)

    return jsonify(response), status


@profile_bp.route("", methods=["GET"])
@jwt_required()
def get():

    user_id = get_jwt_identity()

    response, status = get_profile(user_id)

    return jsonify(response), status


@profile_bp.route("", methods=["PUT"])
@jwt_required()
def update():

    user_id = get_jwt_identity()

    data = request.get_json()

    response, status = update_profile(user_id, data)

    return jsonify(response), status