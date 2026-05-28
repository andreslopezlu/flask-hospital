from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db

if TYPE_CHECKING:
    from flask_hospital.models.doctor import Doctor
    from flask_hospital.models.specialty import Specialty


class DoctorSpecialty(db.Model):
    __tablename__: str = "doctor_specialty"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    doctor_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("doctor.id"), nullable=False)
    specialty_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("specialty.id"), nullable=False)
    vinculation_date: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    doctor: Mapped["Doctor"] = relationship("Doctor", back_popultes="doctor_specialties", lazy="joined")
    specialty: Mapped["Specialty"] = relationship("Specialty", back_populates="doctor_specialties", lazy="joined")

    def __repr__(self) -> str:
        return (
            f"DoctorSpecialty(id={self.id}, doctor_id={self.doctor_id}, specialty_id={self.specialty_id}, "
            f"vinculation_date={self.vinculation_date}, created_at={self.created_at}, "
            f"updated_at={self.updated_at})"
        )

    def to_dict(self) -> dict[str, int | str | None]:
        return {
            "id": self.id,
            "doctor_id": self.doctor_id,
            "specialty_id": self.specialty_id,
            "vinculation_date": self.vinculation_date.isoformat() if self.vinculation_date else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
