from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PersonneForm, VoitureForm

from .models import Personne, Voiture


def personne(request):
    if request.method == 'GET':
        form = PersonneForm()
        personnes = Personne.objects.all()
        context = {
            "form": form,
            "personnes": personnes
        }
        return render(request, 'personne.html', context)
    elif request.method == "POST":
        data = PersonneForm(request.POST)
        
        if data.is_valid():
            nom = data.cleaned_data.get("nom")
            prenom = data.cleaned_data.get("prenom")
            age = data.cleaned_data.get("age")
            genre = data.cleaned_data.get("genre")
            personne = Personne.objects.create(nom=nom,prenom=prenom,age=age,genre=genre)
            personne.save()
            return HttpResponse("Ajout reussi")
        return HttpResponse("Ajout échoué")
    
def delete_personne(request, id):
    Personne.objects.filter(id=id).first().delete()
    return HttpResponse("suppression réussie")

def modify_personne(request, id):
    try:
        personne = Personne.objects.get(id=id)
    except Personne.DoesNotExist:
        return HttpResponse("Personne non trouvée")

    if request.method == 'POST':
        form = PersonneForm(request.POST, instance=personne)
        
        if form.is_valid():
            form.save()
            return HttpResponse("Modification réussie")
        else:
            return HttpResponse("Le formulaire est invalide. Veuillez corriger les erreurs.")
    else:
        form = PersonneForm(instance=personne)
        context = {
            'form': form,
            'personne': personne,
        }
        return render(request, 'modify_personne.html', context)


def voiture(request):
    if request.method =="GET":
        context={
            "form": VoitureForm()
        }
        return render(request, "voiture.html",context)
    
    elif request.method == "POST":
        data = VoitureForm(request.POST)
        
        if data.is_valid():
            immatriculation = data.cleaned_data.get("immatriculation")
            marque = data.cleaned_data.get("marque")
            image = data.cleaned_data.get("image")
            proprietaire= data.cleaned_data.get("proprietaire")
            voiture = Voiture.objects.create(immatriculation=immatriculation,marque=marque,image=image,proprietaire=proprietaire)
            voiture.save()
            return HttpResponse("Ajout voiture reussi")
        return HttpResponse("Ajout voiture échoué")