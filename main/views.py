from django.shortcuts import render
from .models import Wallpaper

def home(request):
    wallpapers = Wallpaper.objects.all()

    # filter by device (mobile / desktop)
    wallpaper_type = request.GET.get('type')
    device = request.GET.get('device')

    if wallpaper_type:
        wallpapers = wallpapers.filter(type=wallpaper_type)

    if device:
        wallpapers = wallpapers.filter(device=device)

    # search by title
    search = request.GET.get('search')
    if search:
        wallpapers = wallpapers.filter(title__icontains=search.strip())

    print(f"DEBUG: Found {wallpapers.count()} wallpapers")  # This will show in Render logs
    for w in wallpapers:
        print(f"DEBUG: {w.title} - {w.img.url if w.img else 'No image'}")

    return render(request, 'home.html', {'wallpapers': wallpapers})