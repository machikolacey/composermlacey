from django.shortcuts import render
from .models import Page

def index(request, permalink):
    """ A view to return the index page """

    page = Page.objects.all()
    try:
        page = Page.objects.get(permalink=permalink)
    except ObjectDoesNotExist:
        page = None

    context = {
        'page': page
    }
    return render(request, 'advert/page.html', context)

