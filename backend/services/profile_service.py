from models import db
from models.patient_profile import PatientProfile


def create_profile(user_id, data):

    existing = PatientProfile.query.filter_by(user_id=user_id).first()

    if existing:
        return {
            "error": "Profile already exists"
        }, 400

    profile = PatientProfile(

        user_id=user_id,

        age=data.get("age"),

        gender=data.get("gender"),

        height=data.get("height"),

        weight=data.get("weight"),

        blood_group=data.get("blood_group"),

        allergies=data.get("allergies"),

        chronic_diseases=data.get("chronic_diseases"),

        emergency_contact=data.get("emergency_contact")
    )

    db.session.add(profile)

    db.session.commit()

    return {

        "message": "Profile Created Successfully"

    }, 201

def get_profile(user_id):

    profile = PatientProfile.query.filter_by(
        user_id=user_id
    ).first()

    if not profile:

        return {

            "error": "Profile not found"

        }, 404

    return {

        "profile_id": profile.profile_id,

        "user_id": profile.user_id,

        "age": profile.age,

        "gender": profile.gender,

        "height": profile.height,

        "weight": profile.weight,

        "blood_group": profile.blood_group,

        "allergies": profile.allergies,

        "chronic_diseases": profile.chronic_diseases,

        "emergency_contact": profile.emergency_contact

    }, 200

def update_profile(user_id, data):

    profile = PatientProfile.query.filter_by(
        user_id=user_id
    ).first()

    if not profile:

        return {

            "error": "Profile not found"

        }, 404

    profile.age = data.get("age")

    profile.gender = data.get("gender")

    profile.height = data.get("height")

    profile.weight = data.get("weight")

    profile.blood_group = data.get("blood_group")

    profile.allergies = data.get("allergies")

    profile.chronic_diseases = data.get("chronic_diseases")

    profile.emergency_contact = data.get("emergency_contact")

    db.session.commit()

    return {

        "message": "Profile Updated Successfully"

    }, 200