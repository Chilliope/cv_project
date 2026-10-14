from django.shortcuts import get_object_or_404, render
from .models import Profil

def index(request) :
    profil = get_object_or_404(Profil, pk=1)

    context = {
        "profil": profil,
        "keahlian": profil.keahlian_set.all(),
        "pendidikan": profil.pendidikan_set.all(),
        "proyek": profil.proyek_set.all(),
    }

    return render(request, "cv/index.html", context)