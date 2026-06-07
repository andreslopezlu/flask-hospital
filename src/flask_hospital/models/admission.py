from datetime import datetime
from typing import Any

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db

if TYPE_CHECKING:
    from flask_hospital.models.administrative import Administrative
    from flask_hospital.models.patient import Patient
    from flask_hospital.models.turn import Turn


class Admission(db.Model):  # type: ignore[misc]
    __tablename__: str = "admission"

    id: Mapped[int] = mapped_column(db.Integer(unsigned=True), primary_key=True)
    start_date_time: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    end_date_time: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    reason: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    administrative_id: Mapped[int] = mapped_column(
        db.Integer(unsigned=True), db.ForeignKey("administrative.id"), nullable=True
    )
    turn_id: Mapped[int] = mapped_column(
        db.Integer(unsigned=True), db.ForeignKey("turn.id"), nullable=True, unique=True
    )
    patient_id: Mapped[int] = mapped_column(db.Integer(unsigned=True), db.ForeignKey("patient.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    administrative: Mapped["Administrative"] = relationship(
        "Administrative", back_populates="admissions", lazy="joined"
    )
    turn: Mapped["Turn"] = relationship("Turn", back_populates="admission", lazy="joined", uselist=False)
    patient: Mapped["Patient"] = relationship("Patient", back_populates="admissions", lazy="joined")

    def __repr__(self) -> str:
        return (
            f"Admission(id={self.id}, start_date_time={self.start_date_time}, end_date_time={self.end_date_time}, "
            f"reason={self.reason}, administrative_id={self.administrative_id}, turn_id={self.turn_id}, "
            f"patient_id={self.patient_id})"
        )

    def to_dict(self) -> dict[str, int | datetime | Any | None]:
        return {
            "id": self.id,
            "start_date_time": self.start_date_time.isoformat() if self.start_date_time else None,
            "end_date_time": self.end_date_time.isoformat() if self.end_date_time else None,
            "reason": self.reason,
            "administrative_id": self.administrative_id,
            "turn_id": self.turn_id,
            "patient_id": self.patient_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
