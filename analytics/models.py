from django.db import models
from zlm.models import ZlmURL


class ClickEventManager(models.Manager):
    def click_event(self, Zlminstance):
        if isinstance(Zlminstance, ZlmURL):
            obj, created = self.get_or_create(zlm_url=Zlminstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    zlm_url = models.OneToOneField(ZlmURL)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "Zlm URL : {url} Count : {i}".format(url=self.zlm_url, i=self.count)