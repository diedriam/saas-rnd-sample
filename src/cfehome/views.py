import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

this_dir = pathlib.Path(__file__)

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs  = PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_content = {
        "page_title": my_title,
        "queryset": qs,
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count() * 100)/qs.count(),
        "total_visit_count": qs.count(),
    }

    PageVisit.objects.create(path=request.path)
    return render(request, "home.html", my_content)


