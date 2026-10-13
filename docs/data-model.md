# LinkFluence Data Model

## Creator

Stores information about each content creator.

Fields:
- id
- name
- username
- niche
- platform
- followers
- engagement_rate
- location
- price_per_post
- bio

## Campaign

Stores brand campaign requirements.

Fields:
- id
- brand_name
- title
- description
- niche
- platform
- budget
- min_followers
- min_engagement
- created_at

## Matching

The matching service compares campaign requirements with
creator attributes and calculates a compatibility score.

The initial matching algorithm is rule-based and explainable.