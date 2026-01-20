from django.shortcuts import render
from .models import Destination   # IMPORTANT import

def home(request):
    dests = Destination.objects.all()
    return render(request, 'main/home.html', {
        'dests': dests
    })
def home(request):
    search_query = request.GET.get('search')

    if search_query:
        dests = Destination.objects.filter(name__icontains=search_query)
    else:
        dests = Destination.objects.all()

    return render(request, 'main/home.html', {
        'dests': dests
    })

def home(request):
    dests = Destination.objects.all()

    category = request.GET.get('type')
    search = request.GET.get('search')

    if category:
        dests = dests.filter(img_type=category)

    if search:
        dests = dests.filter(name__icontains=search)  # ✅ FIXED HERE

    return render(request, 'main/home.html', {
        'dests': dests
    })
