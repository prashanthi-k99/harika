from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from database.db import db
from models.campaign import Campaign
from services.matching_service import find_matching_creators


campaign_bp = Blueprint(
    "campaigns",
    __name__,
    url_prefix="/campaigns"
)


@campaign_bp.route("/new", methods=["GET", "POST"])
def create_campaign():
    if request.method == "POST":
        brand_name = request.form.get(
            "brand_name", ""
        ).strip()

        title = request.form.get(
            "title", ""
        ).strip()

        description = request.form.get(
            "description", ""
        ).strip()

        niche = request.form.get(
            "niche", ""
        ).strip()

        platform = request.form.get(
            "platform", ""
        ).strip()

        try:
            budget = float(request.form.get("budget", 0))
            min_followers = int(
                request.form.get("min_followers", 0)
            )
            min_engagement = float(
                request.form.get("min_engagement", 0)
            )

            if (
                not brand_name
                or not title
                or not description
                or not niche
                or not platform
            ):
                raise ValueError("All text fields are required.")

            if (
                budget <= 0
                or min_followers < 0
                or min_engagement < 0
                or min_engagement > 100
            ):
                raise ValueError("Please enter valid campaign requirements.")

        except (ValueError, TypeError):
            flash("Please check your campaign details.", "error")

            return render_template(
                "create_brief.html"
            ), 400

        campaign = Campaign(
            brand_name=brand_name,
            title=title,
            description=description,
            niche=niche,
            platform=platform,
            budget=budget,
            min_followers=min_followers,
            min_engagement=min_engagement
        )

        db.session.add(campaign)
        db.session.commit()

        return redirect(
            url_for(
                "campaigns.campaign_results",
                campaign_id=campaign.id
            )
        )

    return render_template("create_brief.html")


@campaign_bp.route("/<int:campaign_id>/results")
def campaign_results(campaign_id):
    campaign = Campaign.query.get_or_404(campaign_id)

    matches = find_matching_creators(campaign)

    return render_template(
        "results.html",
        campaign=campaign,
        matches=matches
    )


@campaign_bp.route("/")
def campaign_dashboard():
    campaigns = Campaign.query.order_by(
        Campaign.created_at.desc()
    ).all()

    return render_template(
        "brand_dashboard.html",
        campaigns=campaigns
    )