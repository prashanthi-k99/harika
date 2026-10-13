import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "linkfluence-local-development-key"
    )

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///"
        + str(BASE_DIR / "instance" / "linkfluence.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False