from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db

if TYPE_CHECKING:
    from flask_hospital.models.bill import Bill
    from flask_hospital.models.dispensing import Dispensing
    from flask_hospital.models.doctor import Doctor
    from flask_hospital.models.history import History
    from flask_hospital.models.patient import Patient
    from flask_hospital.models.procedure_atention import ProcedureAtention
    from flask_hospital.models.triage import Triage


class Atention(db.Model):
    __tablename__: str = "atention"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    patient_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    history_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("history.id"), nullable=False)
    triage_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("triage.id"), nullable=False, unique=True)
    doctor_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("doctor.id"), nullable=True)
    start_date_time: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    end_date_time: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    consultation_reason: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    evolution: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    diagnosis: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    treatment: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    physical_examination: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    observation: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    is_active: Mapped[bool] = mapped_column(db.Boolean, default=1, nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    bill: Mapped["Bill"] = relationship(
        "Bill", back_populates="atention", lazy="joined", uselist=False, cascade="all, delete-orphan"
    )
    patient: Mapped["Patient"] = relationship("Patient", back_populates="atentions", lazy="joined")
    history: Mapped["History"] = relationship("History", back_populates="atentions", lazy="joined")
    triage: Mapped["Triage"] = relationship("Triage", back_populates="atention", lazy="joined", uselist=False)
    doctor: Mapped["Doctor"] = relationship("Doctor", back_populates="atentions", lazy="joined")
    procedure_atentions: Mapped[list["ProcedureAtention"]] = relationship(
        "ProcedureAtention", back_populates="atention", lazy="selectin", cascade="all, delete-orphan"
    )
    dispensations: Mapped[list["Dispensing"]] = relationship("Dispensing", back_populates="atention", lazy="selectin")

    def __repr__(self) -> str:
        return (
            f"Atention(id={self.id}, patient_id={self.patient_id}, history_id={self.history_id}, "
            f"triage_id={self.triage_id}, doctor_id={self.doctor_id}, start_date_time={self.start_date_time}, "
            f"end_date_time={self.end_date_time}, observation={self.observation}, is_active={self.is_active})"
        )

    def to_dict(self) -> dict[str, int | datetime | Any | bool | None]:
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "history_id": self.history_id,
            "triage_id": self.triage_id,
            "doctor_id": self.doctor_id,
            "start_date_time": self.start_date_time,
            "end_date_time": self.end_date_time,
            "consultation_reason": self.consultation_reason,
            "evolution": self.evolution,
            "diagnosis": self.diagnosis,
            "treatment": self.treatment,
            "physical_examination": self.physical_examination,
            "observation": self.observation,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
