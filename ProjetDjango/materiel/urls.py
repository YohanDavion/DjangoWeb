from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enregistrer_materiel/', views.enregistrer_materiel, name='enregistrer_materiel'),
    path('enregistrer_enseignant/', views.enregistrer_enseignant, name='enregistrer_enseignant'),
    path('changer_possesseur/', views.changer_possesseur, name='changer_possesseur'),
    path('voir_materiel_salle/<int:salle_id>/', views.voir_materiel_salle, name='voir_materiel_salle'),
    path('voir_emplacement_materiel/<int:materiel_id>/', views.voir_emplacement_materiel, name='voir_emplacement_materiel'),
    path('voir_materiel_enseignant/<int:enseignant_id>/', views.voir_materiel_enseignant, name='voir_materiel_enseignant'),
    path('voir_emprunteur_materiel/<int:materiel_id>/', views.voir_emprunteur_materiel, name='voir_emprunteur_materiel'),
    path('voir_responsable_materiel/<int:materiel_id>/', views.voir_responsable_materiel, name='voir_responsable_mater')]
