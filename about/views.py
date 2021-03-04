from django.shortcuts import render
from .models import Page
from .models import SampleVideo



def index(request, permalink):
    """ A view to return the index page """

    sampleVideos = SampleVideo.objects.all()

    try:
        page = Page.objects.get(permalink=permalink)
    except ObjectDoesNotExist:
        page = None


    if(permalink == 'sample-videos'):
        template = 'advert/video_samples.html'
    else:
        template = 'advert/page.html'

    context = {
        'page': page,
        'sampleVideos': sampleVideos
    }
    return render(request, template, context)

