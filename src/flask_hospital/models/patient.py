from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db
from flask_hospital.models.blood_type import BloodType
from flask_hospital.models.gender import Gender
from flask_hospital.models.identification import Identification

if TYPE_CHECKING:
    from flask_hospital.models.admission import Admission
    from flask_hospital.models.atention import Atention
    from flask_hospital.models.history import History
    from flask_hospital.models.triage import Triage


class Patient(db.Model):
    __tablename__: str = "patient"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    lastname: Mapped[str] = mapped_column(db.String(100), nullable=False)
    identification_number: Mapped[int] = mapped_column(db.Integer, nullable=False, unique=True)
    identification_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("identification.id"), nullable=True)
    birth_date: Mapped[datetime] = mapped_column(db.DateTime, nullable=False)
    gender_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("gender.id"), nullable=True)
    blood_type_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("blood_type.id"), nullable=True)
    email: Mapped[str] = mapped_column(db.String(100), nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(db.String(50), nullable=False, unique=True)
    address: Mapped[str] = mapped_column(db.String(100), nullable=False)
    emergency_contact: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    notification_preference: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    is_active: Mapped[bool] = mapped_column(db.Boolean, default=1, nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now())
    updated_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    identification: Mapped["Identification"] = relationship("Identification", back_populates="patients", lazy="joined")
    gender: Mapped["Gender"] = relationship("Gender", back_populates="patients", lazy="joined")
    blood_type: Mapped["BloodType"] = relationship("BloodType", back_populates="patients", lazy="joined")
    atentions: Mapped[list["Atention"]] = relationship(
        "Atention", back_populates="patient", lazy="selectin", cascade="all, delete-orphan"
    )
    history: Mapped["History"] = relationship(
        "History", back_populates="patient", lazy="joined", uselist=False, cascade="all, delete-orphan"
    )
    triages: Mapped["Triage"] = relationship(
        "Triage", back_populates="patient", lazy="selectin", cascade="all, delete-orphan"
    )
    admissions: Mapped[list["Admission"]] = relationship(
        "Admission", back_populates="patient", lazy="selectin", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return (
            f"Patient (id={self.id}, name='{self.name}', lastname='{self.lastname}', "
            f"identification_number={self.identification_number}, "
            f"blood_type='{self.blood_type.name if self.blood_type else None}', "
            f"email='{self.email}', phone_number='{self.phone_number}', "
            f"emergency_contact='{self.emergency_contact or None}', "
            f"notification_preference='{self.notification_preference or None}')"
        )

    def to_dict(self) -> dict[str, str | int | bool | datetime | Identification | Gender | BloodType | None]:
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "identification_number": self.identification_number,
            "identification": self.identification or None,
            "birth_date": self.birth_date,
            "gender": self.gender or None,
            "blood_type": self.blood_type or None,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "emergency_contact": self.emergency_contact,
            "notification_preference": self.notification_preference,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
