from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db

if TYPE_CHECKING:
    from flask_hospital.models.atention import Atention
    from flask_hospital.models.doctor import Doctor
    from flask_hospital.models.nurse import Nurse
    from flask_hospital.models.procedure import Procedure


class ProcedureAtention(db.Model):
    __tablename__: str = "procedure_atention"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    atention_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("atention.id"), nullable=False)
    procedure_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("procedure.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(db.Integer, nullable=False)
    observation: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    cost: Mapped[float] = mapped_column(db.Float, nullable=False)
    doctor_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("doctor.id"), nullable=True)
    nurse_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("nurse.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    atention: Mapped["Atention"] = relationship("Atention", back_populates="procedure_atentions", lazy="joined")
    procedure: Mapped["Procedure"] = relationship("Procedure", back_populates="procedure_atentions", lazy="joined")
    doctor: Mapped["Doctor"] = relationship("Doctor", back_populates="procedure_atentions", lazy="joined")
    nurse: Mapped["Nurse"] = relationship("Nurse", back_populates="procedure_atentions", lazy="joined")

    def __repr__(self) -> str:
        return (
            f"ProcedureAtention(id={self.id}, atention_id={self.atention_id}, "
            f"procedure_id={self.procedure_id}, quantity={self.quantity}, "
            f"observation={self.observation}, cost={self.cost}, "
            f"doctor_id={self.doctor_id}, nurse_id={self.nurse_id})"
        )

    def to_dict(self) -> dict[str, int | float | str | Any | None]:
        return {
            "id": self.id,
            "atention_id": self.atention_id,
            "procedure_id": self.procedure_id,
            "quantity": self.quantity,
            "observation": self.observation,
            "cost": self.cost,
            "doctor_id": self.doctor_id,
            "nurse_id": self.nurse_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
