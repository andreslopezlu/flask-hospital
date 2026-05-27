from datetime import datetime
from typing import Any

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db
from flask_hospital.models.blood_type import BloodType
from flask_hospital.models.gender import Gender
from flask_hospital.models.identification import Identification


class Administrative(db.Model):
    __tablename__: str = "administrative"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    lastname: Mapped[str] = mapped_column(db.String(100), nullable=False)
    identification_number: Mapped[int] = mapped_column(db.Integer, nullable=False, unique=True)
    identification_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("identification.id"), nullable=True)
    birth_date: Mapped[datetime] = mapped_column(db.DateTime, nullable=False)
    gender_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("gender.id"), nullable=True)
    blood_type_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("blood_type.id"), nullable=True)
    administrative_license_number: Mapped[int] = mapped_column(db.Integer, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(db.String(100), nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(db.String(50), nullable=False, unique=True)
    address: Mapped[str] = mapped_column(db.String(100), nullable=False)
    emergency_contact: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    salary: Mapped[float] = mapped_column(db.Float, nullable=False)
    day_hour_price: Mapped[float] = mapped_column(db.Float, nullable=False)
    night_hour_price: Mapped[float] = mapped_column(db.Float, nullable=False)
    is_active: Mapped[bool] = mapped_column(db.Boolean, default=1, nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now())
    updated_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    identification: Mapped["Identification"] = relationship(
        "Identification", back_populates="administratives", lazy="joined"
    )
    gender: Mapped["Gender"] = relationship("Gender", back_populates="administratives", lazy="joined")
    blood_type: Mapped["BloodType"] = relationship("BloodType", back_populates="administratives", lazy="joined")

    def __repr__(self) -> str:
        return (
            f"Administrative (id={self.id}, name='{self.name}', lastname='{self.lastname}', "
            f"identification_number={self.identification_number}, "
            f"administrative_license_number={self.administrative_license_number}, "
            f"blood_type='{self.blood_type.name if self.blood_type else None}', "
            f"email='{self.email}', phone_number='{self.phone_number}', "
            f"emergency_contact='{self.emergency_contact or None}')"
        )

    def to_dict(self) -> dict[str, str | int | float | bool | datetime | Identification | Gender | BloodType | None]:
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "identification_number": self.identification_number,
            "identification": self.identification or None,
            "birth_date": self.birth_date,
            "gender": self.gender or None,
            "blood_type": self.blood_type or None,
            "administrative_license_number": self.administrative_license_number,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "emergency_contact": self.emergency_contact,
            "salary": self.salary,
            "day_hour_price": self.day_hour_price,
            "night_hour_price": self.night_hour_price,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
