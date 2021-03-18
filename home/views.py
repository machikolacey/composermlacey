from django.shortcuts import render
from .models import Advert, homepageVideo
from products.models import Product

def index(request):
    """ A view to return the index page """

    adverts = Advert.objects.all()
    products = Product.objects.all()
    homepagevideo = homepageVideo.objects.first()

    embedvideo = homepagevideo.youtube_link.replace("watch?v=", "embed/")

    context = {
        'adverts': adverts,
        'products': products,
        'homepagevideo': homepagevideo,
        'embedvideo': embedvideo
    }
    return render(request, 'home/index.html', context)

