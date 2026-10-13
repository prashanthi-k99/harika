from datetime import datetime, timezone
from database.db import db


class Campaign(db.Model):
    __tablename__ = "campaigns"

    id = db.Column(db.Integer, primary_key=True)

    brand_name = db.Column(
        db.String(120),
        nullable=False
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    niche = db.Column(
        db.String(50),
        nullable=False
    )

    platform = db.Column(
        db.String(30),
        nullable=False
    )

    budget = db.Column(
        db.Float,
        nullable=False
    )

    min_followers = db.Column(
        db.Integer,
        default=0
    )

    min_engagement = db.Column(
        db.Float,
        default=0.0
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    def to_dict(self):
        return {
            "id": self.id,
            "brand_name": self.brand_name,
            "title": self.title,
            "description": self.description,
            "niche": self.niche,
            "platform": self.platform,
            "budget": self.budget,
            "min_followers": self.min_followers,
            "min_engagement": self.min_engagement
        }