from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db

if TYPE_CHECKING:
    from flask_hospital.models.turn_state import TurnState


class Turn(db.Model):
    __tablename__: str = "turn"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    arrival_date_time: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    turn_state_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("turn_state.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    turn_state: Mapped["TurnState"] = relationship("TurnState", back_populates="turns", lazy="joined")

    def __repr__(self) -> str:
        return f"Turn (id={self.id}, arrival_date_time={self.arrival_date_time}, turn_state_id={self.turn_state_id})"

    def to_dict(self) -> dict[str, int | str | None]:
        return {
            "id": self.id,
            "arrival_date_time": self.arrival_date_time.isoformat() if self.arrival_date_time else None,
            "turn_state_id": self.turn_state_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
