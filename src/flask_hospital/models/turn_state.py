from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from flask_hospital.extensions import db


class TurnState(db.Model):
    __tablename__: str = "turn_state"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), unique=True, nullable=False)
    abbreviation: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    def __repr__(self) -> str:
        return f"TurnState(name={self.name}, abbreviation={self.abbreviation})"

    def to_dict(self) -> dict[str, str | int | None]:
        return {
            "id": self.id,
            "name": self.name,
            "abbreviation": self.abbreviation,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
