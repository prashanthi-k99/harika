from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import or_
from models.creator import Creator

creator_bp = Blueprint(
    "creators",
    __name__,
    url_prefix="/creators"
)


@creator_bp.route("/")
def list_creators():
    query = Creator.query

    niche = request.args.get("niche", "").strip()
    platform = request.args.get("platform", "").strip()
    search = request.args.get("q", "").strip()

    if niche:
        query = query.filter(
            Creator.niche.ilike(niche)
        )

    if platform:
        query = query.filter(
            Creator.platform.ilike(platform)
        )

    if search:
        pattern = f"%{search}%"

        query = query.filter(
            or_(
                Creator.name.ilike(pattern),
                Creator.username.ilike(pattern),
                Creator.bio.ilike(pattern)
            )
        )

    creators = query.order_by(
        Creator.engagement_rate.desc()
    ).all()

    return render_template(
        "creators.html",
        creators=creators
    )


def db_or(*conditions):
    from sqlalchemy import or_
    return or_(*conditions)


@creator_bp.route("/<int:creator_id>")
def creator_profile(creator_id):
    creator = Creator.query.get_or_404(creator_id)

    return render_template(
        "creator_profile.html",
        creator=creator
    )


@creator_bp.route("/api")
def creators_api():
    creators = Creator.query.all()

    return jsonify([
        creator.to_dict()
        for creator in creators
    ])