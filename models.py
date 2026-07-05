from datetime import UTC, datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# Base class for all database models
class Base(DeclarativeBase):
    pass


# SQLAlchemy extension
db = SQLAlchemy(model_class=Base)


# Return the current UTC time
def utc_now() -> datetime:
    return datetime.now(UTC)


class User(db.Model):
    """Application users."""

    __tablename__ = "users"

    # User information
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))

    # Account status
    is_verified: Mapped[bool] = mapped_column(default=False)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
    )

    # One-to-one relationship with the verification record
    email_verification: Mapped["EmailVerification"] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        uselist=False,
    )

    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email}>"


class EmailVerification(db.Model):
    """Pending email verification tokens."""

    __tablename__ = "email_verifications"

    # Verification record
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )

    # Verification token
    token: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    # Verification timestamps
    verification_sent_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=True,
    )

    verification_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Link back to the owning user
    user: Mapped["User"] = relationship(back_populates="email_verification")

    def __repr__(self) -> str:
        return f"<EmailVerification id={self.id} user_id={self.user_id}>"