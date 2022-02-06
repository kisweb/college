from django import forms

from .models import Classeroom, Agent, Student

class ClasseForm(forms.ModelForm):
       
        class Meta:
            model = Classeroom
            fields = '__all__'




'''
        refClasse = forms.IntegerField(label='Référence', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number',}))
        libClasse = forms.CharField(label='Classe', widget=forms.Select(attrs={'class': 'form-control', 'type': 'select',}))
        niveau = forms.CharField(label='Niveau', widget=forms.TextInput(attrs={'class': 'form-control',}))
        nbTables = forms.CharField(label='Nombre de tables', widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number',}))
        surveillant = forms.CharField(label='Surveillant de la classe', widget=forms.TextInput(attrs={'class': 'form-control',}))
        profPrincipal = forms.CharField(label='Professeur principal', widget=forms.TextInput(attrs={'class': 'form-control',}))
        responsable = forms.CharField(label='Responsable de classe', widget=forms.TextInput(attrs={'class': 'form-control',}))
 '''