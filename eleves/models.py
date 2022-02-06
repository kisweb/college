from datetime import datetime
from django.db import models
import uuid

# Create your models here.

SEXES = (('M', 'Homme'), ('H', 'Homme'), ('F', 'Femme'))

class Affectation(models.Model):
    ANNEE = (('2020-2021', '2021'), ('2021-2022', '2022'), ('2022-2023', '2023'))

    annee = models.CharField(max_length=9, choices=ANNEE)
    classe = models.ForeignKey('Classeroom', on_delete=models.CASCADE)

    def __str__(self):
        return self.annee + ' ' + self.classe.libClasse 


class Agent(models.Model):
    
    matricule = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    prenoms = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    dateNaisssance = models.DateField(verbose_name='Date de naissance', blank=True)
    lieuNaissance = models.CharField(max_length=200, verbose_name='Lieu de naissance', blank=True)
    sexe = models.CharField(max_length=1, choices=SEXES)

    class Admin:
        list_display = ['prenoms', 'nom', 'dateNaissance', 'lieuNaissance']

    def __str__(self):
        return self.prenoms + ' ' + self.nom


class Classeroom(models.Model):
    MESCLASSES = (
        ('3A', '3è MA'),
        ('3B', '3è MB'),
        ('4A', '4è MA'),
        ('4B', '4è MB'),
        ('5A', '5è MA'),
        ('5B', '5è MB'),
        ('6A', '6è MA'),
        ('6B', '6è MB'),
    )
    
    NIVEAU = (
        ('3è', 'Troisième'), ('4è', 'Quatrième'), ('5è', 'Cinquième'), ('6è', 'Sixième')
    )

    refClasse = models.IntegerField('Référence', unique=True)
    libClasse = models.CharField('Classe',  max_length=25, choices=MESCLASSES, unique=True)
    niveau = models.CharField('Niveau', max_length=25, choices=NIVEAU)
    nbTables = models.IntegerField('Nombre de tables')
    surveillant = models.CharField('Surveillant', max_length=200, blank=True)
    profPrincipal = models.CharField('Prof principal', max_length=200, blank=True)
    responsable = models.CharField('Responsable', max_length=200, blank=True)

    class Admin:
        list_display = ['libClasse', 'niveau', 'responsable', 'profPrincipal']

    def __str__(self):
        return self.libClasse


class Student(models.Model):
    SEXE_VAL = (
        ('M', 'Masculin'),
        ('F', 'Féminin')
    )
    matricule = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    prenoms = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    dateNaissance = models.DateField(verbose_name='Date de naissance', blank=True, null=True)
    lieuNaissance = models.CharField(max_length=200, verbose_name='Lieu de naissance', blank=True, null=True)
    sexe = models.CharField(max_length=1, choices=SEXE_VAL)

    class Admin:
        list_display = ['prenoms', 'nom']

    def __str__(self):
        return '%s %s' % (self.prenoms, self.nom)


class Inscription(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    affectation = models.ForeignKey('Affectation', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s' % (self.student.prenoms, self.student.nom, self.affectation.classe.libClasse)


class Absence(models.Model):
    TYPE = ['Absence', 'Retard', 'Sortie']
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    dateDeb = models.DateField('Début', default=datetime.today)
    dateFin = models.DateField('Fin', default=datetime.today)
    heureDeb = models.TimeField('De', default=datetime.now)
    heureFin = models.TimeField('A', default=datetime.now)
    type = models.CharField('Type Absence', max_length=25, blank=True)
    justified = models.BooleanField('Justifiée', default=False)
    comment = models.TextField('Commentaires', blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.student.prenoms, self.student.nom)
