from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from flask_hospital.extensions import db


class Specialty(db.Model):
    __tablename__: str = "specialty"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), unique=True, nullable=False)
    abbreviation: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(db.String(200), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(db.Boolean, default=1, nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    def __repr__(self) -> str:
        return (
            f"Specialty (id={self.id}, name={self.name}, abbreviation={self.abbreviation}, "
            f"description={self.description}, state={self.state})"
        )

    def to_dict(self) -> dict[str, str | int | None]:
        return {
            "id": self.id,
            "name": self.name,
            "abbreviation": self.abbreviation,
            "description": self.description,
            "state": self.state,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
