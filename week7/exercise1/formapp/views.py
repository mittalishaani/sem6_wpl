from django.shortcuts import render

def home(request):
    manufacturers = ["Toyota", "Honda", "BMW", "Hyundai", "Tesla"]
    return render(request, "home.html", {"manufacturers": manufacturers})


def result(request):
    if request.method == "POST":
        manufacturer = request.POST.get("manufacturer")
        model = request.POST.get("model")

        return render(request, "result.html", {
            "manufacturer": manufacturer,
            "model": model
        })

    return render(request, "home.html")