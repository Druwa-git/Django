import os
import json

from django.core.management.utils import get_random_secret_key

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def setup_secret_key():
    with open(os.path.join(BASE_DIR, "credentials.json"), "w") as fp:
        context = dict()
        context['DJANGO_SECRET_KEY'] = get_random_secret_key()
        fp.write(json.dumps(context))


if __name__ == "__main__":
    setup_secret_key()
