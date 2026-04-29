from django.shortcuts import render, get_object_or_404, redirect
from .models import Dia, Concerto, Palco
from .forms import ConcertoForm, PalcoForm


def lista_dias(request):
    dias = Dia.objects.all().order_by("data")
    return render(request, "festival/lista_dias.html", {
        "dias": dias
    })


def concerto_detail(request, concerto_id):
    concerto = get_object_or_404(Concerto, id=concerto_id)
    return render(request, "festival/concerto_detail.html", {
        "concerto": concerto
    })


def editar_concerto(request, concerto_id):
    concerto = get_object_or_404(Concerto, id=concerto_id)

    if request.method == "POST":
        form = ConcertoForm(request.POST, instance=concerto)
        if form.is_valid():
            form.save()
            return redirect("concerto_detail", concerto_id=concerto.id)
    else:
        form = ConcertoForm(instance=concerto)

    return render(request, "festival/concerto_form.html", {
        "form": form,
        "concerto": concerto
    })


def criar_concerto(request):
    if request.method == "POST":
        form = ConcertoForm(request.POST)
        if form.is_valid():
            concerto = form.save()
            return redirect("concerto_detail", concerto_id=concerto.id)
    else:
        form = ConcertoForm()

    return render(request, "festival/concerto_form.html", {
        "form": form
    })


def apagar_concerto(request, concerto_id):
    concerto = get_object_or_404(Concerto, id=concerto_id)

    if request.method == "POST":
        concerto.delete()
        return redirect("lista_dias")

    return redirect("concerto_detail", concerto_id=concerto.id)


def lista_palcos(request):
    palcos = Palco.objects.all()
    return render(request, "festival/lista_palcos.html", {
        "palcos": palcos
    })


def editar_palco(request, palco_id):
    palco = get_object_or_404(Palco, id=palco_id)

    if request.method == "POST":
        form = PalcoForm(request.POST, instance=palco)
        if form.is_valid():
            form.save()
            return redirect("lista_palcos")
    else:
        form = PalcoForm(instance=palco)

    return render(request, "festival/palco_form.html", {
        "form": form,
        "palco": palco
    })