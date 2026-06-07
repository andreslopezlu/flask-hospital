from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db

if TYPE_CHECKING:
    from flask_hospital.models.medicine import Medicine
    from flask_hospital.models.presentation import Presentation


class MedicinePresentation(db.Model):
    __tablname__: str = "medicine_presentation"

    id: Mapped[int] = mapped_column(db.Integer(unsigned=True), primary_key=True)
    medicine_id: Mapped[int] = mapped_column(db.Integer(unsigned=True), db.ForeignKey("medicine.id"), nullable=False)
    presentation_id: Mapped[int] = mapped_column(
        db.Integer(unsigned=True), db.ForeignKey("presentation.id"), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    medicine: Mapped["Medicine"] = relationship("Medicine", back_populates="medicine_presentations", lazy="joined")
    presentation: Mapped["Presentation"] = relationship(
        "Presentation", back_populates="medicine_presentations", lazy="joined"
    )

    def __repr__(self) -> str:
        return (
            f"<MedicinePresentation id={self.id} medicine_id={self.medicine_id} presentation_id={self.presentation_id}>"
        )

    def to_dict(self) -> dict[str, int]:
        return {
            "id": self.id,
            "medicine_id": self.medicine_id,
            "presentation_id": self.presentation_id,
        }
