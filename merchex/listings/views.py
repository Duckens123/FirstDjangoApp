from cgitb import handler
from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from django.http import Http404


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})
    # return HttpResponse(f"""<h1>Hello duckenson</h1>
    # <p>My favorites groupes<p>
    # <ul>
    #     <li>{bands[0].name}</li>
    #     <li>{bands[1].name}</li>
    # </ul>
    # """)


def band_detail(request, id):
    try:
        band=Band.objects.get(id=id)
        return render(request, 'listings/band_detail.html', {'band': band})
    except Band.DoesNotExist:
        raise Http404("Band Not Found")


def contact(request):
    return HttpResponse('<a href="http://www.infoverite.com">Infoverite</a>')
