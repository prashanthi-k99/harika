from pathlib import Path
from flask import Flask, render_template

from config import Config
from models import db, initialize_database
from routes.creator_routes import creator_bp
from routes.campaign_routes import campaign_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    Path(app.instance_path).mkdir(
        parents=True,
        exist_ok=True
    )

    db.init_app(app)

    app.register_blueprint(creator_bp)
    app.register_blueprint(campaign_bp)

    with app.app_context():
        initialize_database()

    @app.route("/")
    def home():
        from models import Creator

        creators = Creator.query.limit(4).all()

        return render_template(
            "index.html",
            creators=creators
        )

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("base.html"), 404

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)