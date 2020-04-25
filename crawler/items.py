from scrapy import Field, Item


class Case(Item):
    name = Field()
    url = Field()
    dob = Field()
    mother = Field()
    father = Field()
    missing_since = Field()
    age_at_occurrence = Field()
    last_seen_at_city = Field()
    last_seen_at_state = Field()
    eyes = Field()
    hair = Field()
    skin = Field()
    full_text = Field()
