from models.creator import Creator


def calculate_match_score(creator, campaign):
    """
    Calculate a transparent compatibility score from 0 to 100.

    Weights:
    - Niche match: 30%
    - Platform match: 20%
    - Budget compatibility: 20%
    - Follower requirements: 15%
    - Engagement requirements: 15%
    """

    score = 0
    reasons = []

    # 1. Niche compatibility: 30 points
    if creator.niche.casefold() == campaign.niche.casefold():
        score += 30
        reasons.append("Matches the campaign niche.")

    # 2. Platform compatibility: 20 points
    if creator.platform.casefold() == campaign.platform.casefold():
        score += 20
        reasons.append("Uses the requested social platform.")

    # 3. Budget compatibility: 20 points
    if campaign.budget > 0:
        if creator.price_per_post <= campaign.budget:
            score += 20
            reasons.append("Fits within the campaign budget.")
        elif creator.price_per_post <= campaign.budget * 1.25:
            score += 10
            reasons.append("Slightly exceeds the target budget.")

    # 4. Follower requirements: 15 points
    if creator.followers >= campaign.min_followers:
        score += 15
        reasons.append("Meets the minimum follower requirement.")

    # 5. Engagement requirements: 15 points
    if creator.engagement_rate >= campaign.min_engagement:
        score += 15
        reasons.append("Meets the engagement requirement.")

    return {
        "score": score,
        "reasons": reasons
    }


def find_matching_creators(campaign, limit=10):
    """
    Rank creators against a campaign.

    This initial version uses transparent rules, not a trained
    machine-learning model or external AI API.
    """

    creators = Creator.query.all()
    matches = []

    for creator in creators:
        result = calculate_match_score(creator, campaign)

        matches.append({
            "creator": creator,
            "score": result["score"],
            "reasons": result["reasons"]
        })

    matches.sort(
        key=lambda item: (
            item["score"],
            item["creator"].engagement_rate
        ),
        reverse=True
    )

    return matches[:max(0, limit)]