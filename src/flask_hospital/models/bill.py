from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_hospital.extensions import db

if TYPE_CHECKING:
    from flask_hospital.models.administrative import Administrative
    from flask_hospital.models.atention import Atention
    from flask_hospital.models.bill_state import BillState
    from flask_hospital.models.payment_method import PaymentMethod


class Bill(db.Model):
    __tablename__: str = "bill"

    id: Mapped[int] = mapped_column(db.Integer(unsigned=True), primary_key=True)
    atention_id: Mapped[int] = mapped_column(
        db.Integer(unsigned=True), db.ForeignKey("atention.id"), nullable=False, unique=True
    )
    administrative_id: Mapped[int] = mapped_column(
        db.Integer(unsigned=True), db.ForeignKey("administrative.id"), nullable=True
    )
    billing_date_time: Mapped[datetime] = mapped_column(db.Datetime, default=db.func.now(), nullable=False)
    subtotal: Mapped[float] = mapped_column(db.Float(unsigned=True), nullable=False)
    tax: Mapped[float] = mapped_column(db.Float(unsigned=True), nullable=False)
    discount: Mapped[float] = mapped_column(db.Float(unsigned=True), nullable=False)
    total: Mapped[float] = mapped_column(db.Float(unsigned=True), nullable=False)
    payment_method_id: Mapped[int] = mapped_column(
        db.Integer(unsigned=True), db.ForeignKey("payment_method.id"), nullable=True
    )
    bill_state_id: Mapped[int] = mapped_column(db.Integer(unsigned=True), db.ForeignKey("bill_state.id"), nullable=True)
    bill_metadata: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    observations: Mapped[Any] = mapped_column(db.JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    atention: Mapped["Atention"] = relationship("Atention", back_populates="bill", lazy="joined", uselist=False)
    administrative: Mapped["Administrative"] = relationship("Administrative", back_populates="bills", lazy="joined")
    payment_method: Mapped["PaymentMethod"] = relationship("PaymentMethod", back_populates="bills", lazy="joined")
    bill_state: Mapped["BillState"] = relationship("BillState", back_populates="bills", lazy="joined")

    def __repr__(self) -> str:
        return (
            f"Bill(id={self.id}, billing_date_time={self.billing_date_time}, "
            f"subtotal={self.subtotal}, tax={self.tax}, discount={self.discount}, "
            f"total={self.total}, payment_method={self.payment_method.name if self.payment_method else None}, "
            f"bill_state={self.bill_state.name if self.bill_state else None}, "
            f"administrative={self.administrative.name if self.administrative else None})"
        )

    def to_dict(self) -> dict[str, int | float | datetime | Any | None]:
        return {
            "id": self.id,
            "billing_date_time": self.billing_date_time,
            "subtotal": self.subtotal,
            "tax": self.tax,
            "discount": self.discount,
            "total": self.total,
            "bill_metadata": self.bill_metadata,
            "observations": self.observations,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "payment_method_id": self.payment_method_id,
            "bill_state_id": self.bill_state_id,
            "administrative_id": self.administrative_id,
        }
