from django.shortcuts import render
from .models import Wallpaper
from django.shortcuts import render

def home(request):
    wallpapers = Wallpaper.objects.all()

    # filter by device (mobile / desktop)
   
    wallpaper_type = request.GET.get('type')
    device = request.GET.get('device')

    wallpapers = Wallpaper.objects.all()

    if wallpaper_type:
        wallpapers = wallpapers.filter(type=wallpaper_type)

    if device:
        wallpapers = wallpapers.filter(device=device)
    # search by title
    search = request.GET.get('search')
    if search:
        wallpapers = wallpapers.filter(title__icontains=search.strip())

    return render(request, 'home.html', {
        'wallpapers': wallpapers
    })
