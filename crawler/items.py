from scrapy import Field, Item


class Case(Item):
    name = Field()
    url = Field()
    dob = Field()
    mother = Field()
    father = Field()
    missing_since = Field()
    last_seen_at = Field()
    eyes = Field()
    hair = Field()
    skin = Field()
    full_text = Field()
