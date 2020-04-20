from json import loads

import pytest
from django.urls import reverse
from model_bakery import baker


@pytest.fixture
@pytest.mark.django_db
def kids():
    baker.make("core.Kid", eyes="black")
    baker.make("core.Kid", eyes="brown")


@pytest.mark.django_db
def test_list(kids, client):
    resp = client.get(reverse("api:api_kid_list"))
    data = loads(resp.content)["objects"]
    assert len(data) == 2


@pytest.mark.django_db
def test_list_with_filter(kids, client):
    resp = client.get(f"{reverse('api:api_kid_list')}?eyes=black")
    data = loads(resp.content)["objects"]
    assert len(data) == 1
