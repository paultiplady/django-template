from django.conf import settings


def test_config():
    assert settings.SECRET_KEY
