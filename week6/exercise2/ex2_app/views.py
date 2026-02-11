from django.shortcuts import render
import os
from django.conf import settings

def cover_form(request):
    context = {}

    if request.method == "POST":
        image = request.FILES.get('image')

        if image:
            file_path = os.path.join(settings.MEDIA_ROOT, image.name)

            with open(file_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            context['image_url'] = settings.MEDIA_URL + image.name

        context['title'] = request.POST.get('title')
        context['subtitle'] = request.POST.get('subtitle')
        context['bg_color'] = request.POST.get('bg_color')
        context['font_color'] = request.POST.get('font_color')
        context['font_size'] = request.POST.get('font_size')

    return render(request, 'ex2_app/index.html', context)
