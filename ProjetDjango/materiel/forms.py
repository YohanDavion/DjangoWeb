from django import forms
from models import Materiel, Enseignant, Passation


class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = ['nom', 'accessoires', 'acheteur', 'responsable', 'salle']


class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom']


class PassationForm(forms.ModelForm):
    class Meta:
        model = Passation
        fields = ['materiel', 'ancien_possesseur', 'nouveau_possesseur', 'lieu', 'occasion', 'objectif_utilisation']
