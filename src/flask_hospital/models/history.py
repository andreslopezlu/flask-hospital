from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db

if TYPE_CHECKING:
    from flask_hospital.models.atention import Atention
    from flask_hospital.models.patient import Patient


class History(db.Model):
    __tablename__: str = "history"

    id: Mapped[int] = mapped_column(db.Integer(unsigned=True), primary_key=True)
    patient_id: Mapped[int] = mapped_column(
        db.Integer(unsigned=True), db.ForeignKey("patient.id"), nullable=False, unique=True
    )
    aperture_date_time: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    closure_date_time: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    antecedents: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    observations: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    patient: Mapped["Patient"] = relationship("Patient", back_populates="history", lazy="joined", uselist=False)
    atentions: Mapped["Atention"] = relationship("Atention", back_populates="history", lazy="selectin")

    def __repr__(self) -> str:
        return (
            f"History (id={self.id}, aperture_date_time={self.aperture_date_time}, "
            f"closure_date_time={self.closure_date_time})"
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "aperture_date_time": self.aperture_date_time.isoformat() if self.aperture_date_time else None,
            "closure_date_time": self.closure_date_time.isoformat() if self.closure_date_time else None,
            "antecedents": self.antecedents,
            "observations": self.observations,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
