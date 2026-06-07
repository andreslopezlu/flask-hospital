from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db

if TYPE_CHECKING:
    from flask_hospital.models.admission import Admission
    from flask_hospital.models.atention import Atention
    from flask_hospital.models.nurse import Nurse
    from flask_hospital.models.patient import Patient
    from flask_hospital.models.priority_level import PriorityLevel


class Triage(db.Model):
    __tablename__: str = "triage"

    id: Mapped[int] = mapped_column(db.Integer(unsigned=True), primary_key=True)
    patient_id: Mapped[int] = mapped_column(db.Integer(unsigned=True), db.ForeignKey("patient.id"), nullable=False)
    nurse_id: Mapped[int] = mapped_column(db.Integer(unsigned=True), db.ForeignKey("nurse.id"), nullable=True)
    admission_id: Mapped[int] = mapped_column(
        db.Integer(unsigned=True), db.ForeignKey("admission.id"), nullable=False, unique=True
    )
    priority_level_id: Mapped[int] = mapped_column(
        db.Integer(unsigned=True), db.ForeignKey("priority_level.id"), nullable=True
    )
    vital_signs: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    start_date_time: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    end_date_time: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    is_active: Mapped[bool] = mapped_column(db.Boolean, default=1, nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    patient: Mapped["Patient"] = relationship("Patient", back_populates="triages", lazy="joined")
    nurse: Mapped["Nurse"] = relationship("Nurse", back_populates="triages", lazy="joined")
    admission: Mapped["Admission"] = relationship(
        "Admission", back_populates="triage", lazy="joined", uselist=False, cascade="all, delete-orphan"
    )
    priority_level: Mapped["PriorityLevel"] = relationship("PriorityLevel", back_populates="triages", lazy="joined")
    atention: Mapped["Atention"] = relationship("Atention", back_populates="triage", lazy="joined", uselist=True)

    def __repr__(self) -> str:
        return (
            f"Triage(id={self.id}, patient_id={self.patient_id}, nurse_id={self.nurse_id}, "
            f"admission_id={self.admission_id}, priority_level_id={self.priority_level_id}, "
            f"vital_signs={self.vital_signs}, start_date_time={self.start_date_time}, "
            f"end_date_time={self.end_date_time}, is_active={self.is_active})"
        )

    def to_dict(self) -> dict[str, int | datetime | Any | bool | None]:
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "nurse_id": self.nurse_id,
            "admission_id": self.admission_id,
            "priority_level_id": self.priority_level_id,
            "vital_signs": self.vital_signs,
            "start_date_time": self.start_date_time.isoformat() if self.start_date_time else None,
            "end_date_time": self.end_date_time.isoformat() if self.end_date_time else None,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
