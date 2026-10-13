from database.db import db


class Creator(db.Model):
    __tablename__ = "creators"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )

    username = db.Column(
        db.String(80),
        unique=True,
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

    followers = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    engagement_rate = db.Column(
        db.Float,
        nullable=False,
        default=0.0
    )

    location = db.Column(
        db.String(100),
        default="Not specified"
    )

    price_per_post = db.Column(
        db.Float,
        nullable=False,
        default=0.0
    )

    bio = db.Column(
        db.Text,
        default=""
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "niche": self.niche,
            "platform": self.platform,
            "followers": self.followers,
            "engagement_rate": self.engagement_rate,
            "location": self.location,
            "price_per_post": self.price_per_post,
            "bio": self.bio
        }