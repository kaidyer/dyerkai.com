from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Education(db.Model):
    __tablename__ = 'education'  # Optional: specify the table name

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    school: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=False)
    degree: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=False)
    graduation_date: so.Mapped[Optional[sa.Date]] = so.mapped_column(sa.Date, nullable=True)

    def __repr__(self) -> str:
        return f"<Education, school='{self.school}', degree='{self.degree}', graduation_date={self.graduation_date})>"
