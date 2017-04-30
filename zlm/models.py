from django.db import models
from .utils import create_short_code
from django.conf import settings

from .validators import validate_com,validate_url
from django.core.urlresolvers import reverse
#from django_hosts.resolvers import reverse
# Create your models here.

SHORT_CODE_MAX = getattr(settings, "SHORT_CODE_MAX", 15)


class ZlmURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(ZlmURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs


class ZlmURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url, validate_com])
    short_code = models.CharField(max_length=SHORT_CODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  # Updated on Save
    timestamp = models.DateTimeField(auto_now_add=True)  # When Created
    active = models.BooleanField(default=True)

    objects = ZlmURLManager()

    def save(self, *args, **kwargs):
        if self.short_code is None or self.short_code == "":
            self.short_code = create_short_code(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(ZlmURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={'short_code': self.short_code})
        path2 = "http://zlm.io" + url_path
        return  path2
