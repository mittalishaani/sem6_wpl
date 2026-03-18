from django.shortcuts import render, redirect


def first_page(request):

    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        subject = request.POST.get("subject")

        # Save data in session
        request.session['name'] = name
        request.session['roll'] = roll
        request.session['subject'] = subject

        return redirect('second')

    return render(request, "firstPage.html")


def second_page(request):

    name = request.session.get('name')
    roll = request.session.get('roll')
    subject = request.session.get('subject')

    data = f"Name: {name}, Roll: {roll}, Subject: {subject}"

    return render(request, "secondPage.html", {"data": data})