import random
import string
from django.conf import settings


SHORT_CODE_MAX = getattr(settings, "SHORT_CODE_MAX", 15)
SHORT_CODE_MIN = getattr(settings, "SHORT_CODE_MIN", 6)


def code_generator(size=SHORT_CODE_MIN, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

    # Same As
    # new_code = ''
    # for _ in range(size):
    #   new_code += random.choice(chars)
    # return new_code


def create_short_code(instance, size=SHORT_CODE_MIN):
    new_code = code_generator(size=size)
    zlm_url = instance.__class__
    url_exist = zlm_url.objects.filter(short_code=new_code).exists()
    if url_exist:
        return create_short_code(size=size)
    return new_code

