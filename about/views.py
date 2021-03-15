from django.shortcuts import render
from .models import Page
from .models import SampleVideo
from .models import Images


def index(request, permalink):
    """ A view to return the index page """

    sampleVideos = SampleVideo.objects.all()

    try:
        page = Page.objects.get(permalink=permalink)
    except ObjectDoesNotExist:
        page = None


    images = Images.objects.filter(page=page)

    if(permalink == 'sample-videos'):
        template = 'advert/video_samples.html'
    else:
        template = 'advert/page.html'

    context = {
        'page': page,
        'sampleVideos': sampleVideos,
        'images': images
    }
    return render(request, template, context)

