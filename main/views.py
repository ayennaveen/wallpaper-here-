from django.http import JsonResponse
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

    # Render logs for debugging
    print(f"DEBUG: Found {wallpapers.count()} wallpapers")  
    for w in wallpapers:
        print(f"DEBUG: {w.title} - {w.img.url if w.img else 'No image'}")

    # NEW: Convert the queryset into a list of dictionaries for React
    data = []
    for w in wallpapers:
        data.append({
            'id': w.id,
            'title': w.title,
            'device': w.device,
            'type': w.type, 
            'img_url': w.img.url if w.img else ''
        })

    # NEW: Return JsonResponse instead of render()
    return JsonResponse({'wallpapers': data})