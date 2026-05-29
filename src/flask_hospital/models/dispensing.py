from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db

if TYPE_CHECKING:
    from flask_hospital.models.atention import Atention
    from flask_hospital.models.medicine import Medicine


class Dispensing(db.Model):
    __tablename__: str = "dispensing"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    atention_id: Mapped[int] = mapped_column(db.Integer, nullable=False)
    medicine_id: Mapped[int] = mapped_column(db.Integer, nullable=False)
    quantity_supplied: Mapped[float] = mapped_column(db.Float, nullable=False)
    delivery_date_time: Mapped[datetime] = mapped_column(db.DateTime, defaul=db.func.now(), nullable=False)
    cost: Mapped[float] = mapped_column(db.Float, nullable=False)
    observation: Mapped[str] = mapped_column(db.String(255))
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    atention: Mapped["Atention"] = relationship("Atention", back_populates="dispensations", lazy="joined")
    medicine: Mapped["Medicine"] = relationship("Medicine", back_populates="dispensations", lazy="joined")

    def __repr__(self) -> str:
        return (
            f"Dispensing(atention_id={self.atention_id}, "
            f"medicine_id={self.medicine_id}, "
            f"quantity_supplied={self.quantity_supplied}, "
            f"delivery_date_time={self.delivery_date_time}, "
            f"cost={self.cost}, "
            f"observation={self.observation})"
        )

    def to_dict(self) -> dict[str, str | int | float | None]:
        return {
            "id": self.id,
            "atention_id": self.atention_id,
            "medicine_id": self.medicine_id,
            "quantity_supplied": float(self.quantity_supplied) if self.quantity_supplied else None,
            "delivery_date_time": self.delivery_date_time.isoformat() if self.delivery_date_time else None,
            "cost": float(self.cost) if self.cost else None,
            "observation": self.observation,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
