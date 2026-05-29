from flask_hospital.extensions import db

medicine_presentation = db.Table(
    "medicine_presentation",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("medicine_id", db.Integer, db.ForeignKey("medicine.id")),
    db.Column("presentation_id", db.Integer, db.ForeignKey("presentation.id")),
    db.Column("created_at", db.DateTime, default=db.func.now(), nullable=False),
    db.Column("updated_at", db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False),
)
