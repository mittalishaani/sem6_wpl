from django.shortcuts import render

# Grocery items with prices
ITEMS = {
    "Wheat": 40,
    "Jaggery": 60,
    "Dal": 80
}

def grocery(request):

    selected_items = {}

    # When Add Item button is clicked
    if request.method == "POST":
        selected = request.POST.getlist("items")

        for item in selected:
            selected_items[item] = ITEMS[item]

    context = {
        "items": ITEMS,
        "selected_items": selected_items
    }

    return render(request, "grocery.html", context)