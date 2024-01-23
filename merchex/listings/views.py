

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Title
from listings.forms import ContactUsForm, BandForm, TitleForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def band_list(request):
    bands = Band.objects.all()
    return render(request, 
            'listings/band_list.html',
            {'bands': bands})
def band_detail(request, band_id):  
    band = Band.objects.get(id=band_id) # on insere cette ligne pour obtenir le Band avec cet id
    return render(request, 'listings/band_detail.html', {'band': band}) # on passe l'id au modele
def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid(): 
        # creer une nouvelle band et la sauvegarder dans la db    
            band = form.save() # la methode form.save() ne fait pas qu'enregistrer le nouvel objet dans la db : elle renvoie egalement cet objet, ce qui signifie que nous pouvons l'utiliser a l'etape suivante, ou nous redirigeons immediatement vers le groupe nouvellement cree.
            return redirect('band-detail', band.id)  # redige vers la page de detail du groupe que nous venons de creer, nous pouvons fournir les arguments du motif url comme arguments a la fonction de redirection.
    else:    
        form = BandForm()
        return render(request, 'listings/band_create.html', {'form': form}) 
def band_update(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:   
        form = BandForm(instance=band) 
        return render(request, 'listings/band_update.html', {'form': form})
def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    else:
        return render(request, 'listings/band_delete.html', {'band': band})

def about(request):
    return render(request, 'listings/about-us.html')

def listings_list(request):
    titles = Title.objects.all()
    return render(request, 
            'listings/listings_list.html',
            {'titles': titles})
def listings_detail(request, title_id):
    title = Title.objects.get(id=title_id)
    return render(request, 'listings/listings_detail.html', {'title': title})
def listings_create(request):
    if request.method == 'POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            title = form.save()
            return redirect('listing-detail', title.id)
    else:
        form = TitleForm()
        return render(request, 'listings/listings_create.html', {'form': form})
def listings_update(request, title_id):
    title = Title.objects.get(id=title_id)
    if request.method == 'POST':
        form = TitleForm(request.POST, instance=title)
        if form.is_valid():
            form.save()
            return redirect('listing-detail', title.id)
    else:
        form = TitleForm(instance=title)
        return render(request, 'listings/listings_update.html', {'form': form})
def listings_delete(request, title_id):
    title = Title.objects.get(id=title_id)
    if request.method == 'POST':
        title.delete()
        return redirect('listing-list')
    else:
        return render(request, 'listings/listings_delete.html', {'title': title})

def redirection(request):
    return render(request, 'listings/redirection.html')

def contact(request):
    
    if request.method == 'POST':    
        form = ContactUsForm(request.POST)
        if form.is_valid():    # si tout les champs de notre formulaire contiennent des donnees valides alors form.is_valid() renvoi True et nous appelons send_mail pour envoyer notre e-mail
            send_mail(
                subject=f'Message from{form.cleaned_data["name"] or "anonyme"}via MerchEx Contact Us form', # form cleaned_data est un dict contenant les donnees du formulaire apres qu'elles 
# ont subi le processus de validation. Lorsque nous sommes prets a faire quelque chose avec les donnees de notre formulaire, nous pouvons acceder a chacun des champs via form.cleaned_data['name_of_field] mais nous devons d'abord appeler form.is_valid() 
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=['admin@merchex.xyz'],)
            return redirect(redirection) # lorsque le formulaire est valide et que le courriel a ete envoye, cette redirection guidera le navigateur de la page du formulaire vers une page de 
# de confirmation. c'est une page qui a un motif URL avec le nom email-sent. 
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact-us.html', {'form': form})
 
