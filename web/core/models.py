from django.db.models import CharField, DateField, Model, TextField, URLField


class Kid(Model):

    # required fiels
    name = CharField("Nome", max_length=255, db_index=True, unique=True)
    url = URLField("URL")
    full_text = TextField()

    # optional indexed fields
    dob = DateField("Data de nascimento", null=True, blank=True, db_index=True)
    missing_since = DateField(
        "Desaparecida(o) desde", null=True, blank=True, db_index=True
    )
    eyes = CharField(
        "Cor dos olhos", max_length=255, null=True, blank=True, db_index=True
    )
    hair = CharField(
        "Cor dos cabelos", max_length=255, null=True, blank=True, db_index=True
    )
    skin = CharField(
        "Cor da pele", max_length=255, null=True, blank=True, db_index=True
    )

    # optional fields
    mother = CharField("Mãe", max_length=255, null=True, blank=True)
    father = CharField("Pai", max_length=255, null=True, blank=True)
    last_seen_at = CharField(
        "Local onde foi vista(o) pela última vez", max_length=255, null=True, blank=True
    )

    class Meta:
        verbose_name = "criança"
        ordering = ("name",)
