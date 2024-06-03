from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Enseignant, Salle, Materiel, Passation
from .forms import MaterielForm, EnseignantForm, PassationForm

def index(request):
    return render(request, 'materiel/index.html')

def enregistrer_materiel(request):
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MaterielForm()
    return render(request, 'materiel/enregistrer_materiel.html', {'form': form})

def enregistrer_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EnseignantForm()
    return render(request, 'materiel/enregistrer_enseignant.html', {'form': form})

def changer_possesseur(request):
    if request.method == 'POST':
        form = PassationForm(request.POST)
        if form.is_valid():
            passation = form.save()
            passation.materiel.possesseur = passation.nouveau_possesseur
            passation.materiel.save()
            return redirect('index')
    else:
        form = PassationForm()
    return render(request, 'materiel/changer_possesseur.html', {'form': form})

def voir_materiel_salle(request, salle_id):
    salle = get_object_or_404(Salle, pk=salle_id)
    materiels = Materiel.objects.filter(salle=salle)
    return render(request, 'materiel/voir_materiel_salle.html', {'salle': salle, 'materiels': materiels})

def voir_emplacement_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, pk=materiel_id)
    return render(request, 'materiel/voir_emplacement_materiel.html', {'materiel': materiel})

def voir_materiel_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, pk=enseignant_id)
    materiels_responsables = Materiel.objects.filter(responsable=enseignant)
    materiels_possedes = Materiel.objects.filter(possesseur=enseignant)
    return render(request, 'materiel/voir_materiel_enseignant.html', {'enseignant': enseignant, 'materiels_responsables': materiels_responsables, 'materiels_possedes': materiels_possedes})

def voir_emprunteur_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, pk=materiel_id)
    possesseur = materiel.possesseur
    return render(request, 'materiel/voir_emprunteur_materiel.html', {'materiel': materiel, 'possesseur': possesseur})

def voir_responsable_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, pk=materiel_id)
    responsable = materiel.responsable
    return render(request, 'materiel/voir_responsable_materiel.html', {'materiel': materiel, 'responsable': responsable})

def voir_historique_emprunt(request, materiel_id):
    materiel = get_object_or_404(Materiel, pk=materiel_id)
    passations = Passation.objects.filter(materiel=materiel).order_by('-date')
    return render(request, 'materiel/voir_historique_emprunt.html', {'materiel': materiel, 'passations': passations})
