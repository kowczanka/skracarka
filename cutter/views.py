from django.shortcuts import render, redirect
from cutter.models import Link

def index(request):
    if request.method == "POST":
        link = request.POST['link']     #kiedy link będzie wysłany formularzem post (przez funckję), to tutaj metodą request go przechwycimy.
        shortened = Link.objects.create(target=link)  #nazwa objects nadana jest przez pythona, bo mamy Link w klasie w models. powoduje dodanie do bazy
        return render(                                  # dodaje je do bazy, ale niżej, jak robimy zliczanie wejść na stronę to link.save() zapisuje dane.
            request,
            'index_post.html',
            {"short_link": f"http://localhost:8000/{shortened.id}/"})     # automatycznie nadaje się ID podczas dodawania do bazy.
    else:
        return render(request, 'index.html')


def przekierowanko(request, link_id):
    link = Link.objects.get(id=link_id)
    link.count += 1
    link.save()
    return redirect(link.target)

def list_of_links(request):
    return render(request, "list.html", {'links': Link.objects.all()})      #.objects.all() zwraca nam wszystkie objekty z bazy