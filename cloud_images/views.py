from django.shortcuts import render

from .models import CloudImage

from .forms import CloudImageForm

# Create your views here.

def cloudindex(request):
    
    print(request)
    cloud_images = CloudImage.objects.all()
    if request.method == "POST":
        # print("Post method firing")
        form = CloudImageForm(request.POST, request.FILES)
        # print("Files: ", request.FILES["image"])
        print(form.errors)
        if form.is_valid():
            # print("Form is valid")
            form.save()

    return render(request, "index.html", {"images":cloud_images})