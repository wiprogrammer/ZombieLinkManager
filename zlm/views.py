from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .forms import SubmitURLForm
from analytics.models import ClickEvent

# Create your views here.
from .models import ZlmURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitURLForm()
        context = {
            "title": "Zombie Link Manager",
            "form": the_form,
        }
        return render(request, 'home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        context = {"title": "Zombie Link Manager", "form": form, }
        template = "home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = ZlmURL.objects.get_or_create(url=new_url)
            context = {
                "title": "Zombie Link Manager",
                "object": obj,
                "created": created,
            }
            if created:
                template = "success.html"
            else:
                template = "already-exist.html"

        return render(request, template, context)


class ZlmRedirectView(View):
    def get(self, request, short_code=None, *args, **kwargs):
        qs = ZlmURL.objects.filter(short_code=short_code)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        ClickEvent.objects.click_event(obj)
        return HttpResponseRedirect(obj.url)
