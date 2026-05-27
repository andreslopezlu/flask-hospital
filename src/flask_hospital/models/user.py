from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import check_password_hash, generate_password_hash

from flask_hospital.extensions import db
from flask_hospital.models.role import Role


class User(db.Model):
    __tablename__: str = "user"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    email: Mapped[str] = mapped_column(db.String(200), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(db.String(200), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column("password", db.String(200), nullable=False)
    is_active: Mapped[bool] = mapped_column(db.Boolean, default=1, nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now())
    updated_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    role_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("role.id"), nullable=True)
    role: Mapped["Role"] = relationship("Role", back_populates="users", lazy="joined")

    @property
    def password(self) -> None:
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        role_name: str | None = self.role.name if self.role else None
        return (
            f"User (id={self.id}, email={self.email}, username={self.username}, "
            f"is_active={self.is_active}, role={role_name})"
        )

    def to_dict(self) -> dict[str, str | int | bool | Role | None]:
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "role": self.role or None,
        }
