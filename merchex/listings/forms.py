from django import forms
from listings.models import Band
from listings.models import Title

class ContactUsForm(forms.Form):
    nom = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):    # generer automatiquement un formulaire a partir d'un modele avec un ModelForm
    class Meta:
        model = Band    # cette classe specifie le modele pour lequel ce formulaire sera utilise, et les champs de ce modele a inclure dans ce formulaire(dans ce cas, c'est tous)
       # fields = '__all__'
        exclude = ('active', 'official_homepage') # si vous voulez exclure certains des autres champs(non nullables) du formulaire, vous devrez d'abord leur donner une valeur par defaut, ou les rendre nullables.

class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = '__all__'
        