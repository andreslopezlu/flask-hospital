from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db

if TYPE_CHECKING:
    from flask_hospital.models.dispensing import Dispensing


class Medicine(db.Model):
    __tablename__: str = "medicine"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(500), nullable=False, unique=True)
    abbreviation: Mapped[str] = mapped_column(db.String(500), nullable=False, unique=True)
    concentration: Mapped[str] = mapped_column(db.String(500), nullable=False, unique=True)
    batch_number: Mapped[str] = mapped_column(db.String(100), nullable=False, unique=True)
    expiration_date: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    existing_quantity: Mapped[int] = mapped_column(db.Integer, nullable=False)
    historical_cost: Mapped[Any] = mapped_column(db.JSON, nullable=True)
    technical_sheet: Mapped[Any] = mapped_column(db.JSON, nullable=True)
    is_active: Mapped[bool] = mapped_column(db.Boolean, default=1, nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    dispensations: Mapped[list["Dispensing"]] = relationship("Dispensing", back_populates="medicine", lazy="selectin")

    def __repr__(self) -> str:
        return (
            f"Medicine(name={self.name}, abbreviation={self.abbreviation}, "
            f"concentration={self.concentration}, expiration_date={self.expiration_date}, "
            f"existing_quantity={self.existing_quantity}, historical_cost={self.historical_cost}, "
            f"technical_sheet={self.technical_sheet}, is_active={self.is_active})"
        )

    def to_dict(self) -> dict[str, str | int | bool | None]:
        return {
            "id": self.id,
            "name": self.name,
            "abbreviation": self.abbreviation,
            "concentration": self.concentration,
            "batch_number": self.batch_number,
            "expiration_date": self.expiration_date.isoformat() if self.expiration_date else None,
            "existing_quantity": self.existing_quantity,
            "historical_cost": self.historical_cost,
            "technical_sheet": self.technical_sheet,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
