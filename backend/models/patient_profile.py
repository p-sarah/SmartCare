from models import db

class PatientProfile(db.Model):

    __tablename__ = "patient_profiles"

    profile_id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id"),
        nullable=False
    )

    age = db.Column(db.Integer)

    gender = db.Column(db.String(20))

    height = db.Column(db.Float)

    weight = db.Column(db.Float)

    blood_group = db.Column(db.String(10))

    allergies = db.Column(db.Text)

    chronic_diseases = db.Column(db.Text)

    emergency_contact = db.Column(db.String(20))

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )