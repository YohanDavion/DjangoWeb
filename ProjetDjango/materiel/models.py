from django.db import models

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Salle(models.Model):
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.numero

class Materiel(models.Model):
    nom = models.CharField(max_length=100)
    accessoires = models.TextField()
    acheteur = models.ForeignKey(Enseignant, on_delete=models.PROTECT, related_name='materiels_achetes')
    responsable = models.ForeignKey(Enseignant, on_delete=models.PROTECT, related_name='materiels_responsables')
    salle = models.ForeignKey(Salle, on_delete=models.SET_NULL, null=True, blank=True)
    possesseur = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, blank=True, related_name='materiels_possedes')

    def __str__(self):
        return self.nom

class Passation(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    ancien_possesseur = models.ForeignKey(Enseignant, on_delete=models.PROTECT, related_name='passations_anciennes')
    nouveau_possesseur = models.ForeignKey(Enseignant, on_delete=models.PROTECT, related_name='passations_nouvelles')
    date = models.DateTimeField(auto_now_add=True)
    lieu = models.ForeignKey(Salle, on_delete=models.PROTECT)
    occasion = models.TextField()
    objectif_utilisation = models.TextField()
