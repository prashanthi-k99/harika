from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def initialize_database():
    # Import models before creating their database tables.
    from models.creator import Creator
    from models.campaign import Campaign

    db.create_all()

    # Add sample creators only when the database is empty.
    if Creator.query.count() == 0:
        sample_creators = [
            Creator(
                name="Ananya Creates",
                username="ananya_creates",
                niche="Fashion",
                platform="Instagram",
                followers=45000,
                engagement_rate=5.8,
                location="Hyderabad",
                price_per_post=5000,
                bio="Fashion styling and everyday lifestyle content."
            ),
            Creator(
                name="TechWithArjun",
                username="techwitharjun",
                niche="Technology",
                platform="YouTube",
                followers=72000,
                engagement_rate=4.9,
                location="Bengaluru",
                price_per_post=10000,
                bio="Technology reviews and beginner-friendly tutorials."
            ),
            Creator(
                name="FoodieMeghana",
                username="foodie_meghana",
                niche="Food",
                platform="Instagram",
                followers=38000,
                engagement_rate=6.2,
                location="Hyderabad",
                price_per_post=4000,
                bio="Restaurant discoveries and home cooking."
            ),
            Creator(
                name="TravelWithRavi",
                username="travelwithravi",
                niche="Travel",
                platform="YouTube",
                followers=95000,
                engagement_rate=5.1,
                location="Chennai",
                price_per_post=12000,
                bio="Travel guides, destination stories, and local experiences."
            ),
            Creator(
                name="DanceDiaries",
                username="dance_diaries",
                niche="Dance",
                platform="Instagram",
                followers=28000,
                engagement_rate=7.4,
                location="Hyderabad",
                price_per_post=3000,
                bio="Dance reels, choreography, and creative performances."
            )
        ]

        db.session.add_all(sample_creators)
        db.session.commit()