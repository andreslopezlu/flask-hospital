from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db

if TYPE_CHECKING:
    from flask_hospital.models.administrative import Administrative
    from flask_hospital.models.doctor import Doctor
    from flask_hospital.models.nurse import Nurse
    from flask_hospital.models.patient import Patient


class Identification(db.Model):
    __tablename__: str = "identification"

    id: Mapped[int] = mapped_column(db.Integer(unsigned=True), primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), unique=True, nullable=False)
    abbreviation: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    doctors: Mapped[list["Doctor"]] = relationship("Doctor", back_populates="identification", lazy="selectin")
    nurses: Mapped[list["Nurse"]] = relationship("Nurse", back_populates="identification", lazy="selectin")
    administratives: Mapped[list["Administrative"]] = relationship(
        "Administrative", back_populates="identification", lazy="selectin"
    )
    patients: Mapped[list["Patient"]] = relationship("Patient", back_populates="identification", lazy="selectin")

    def __repr__(self) -> str:
        return f"Identification(name={self.name}, abbreviation={self.abbreviation})"

    def to_dict(self) -> dict[str, str | int | None]:
        return {
            "id": self.id,
            "name": self.name,
            "abbreviation": self.abbreviation,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
