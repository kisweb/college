# Generated by Django 4.0.2 on 2022-02-05 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eleves', '0005_remove_student_datenaisssance_student_datenaissance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='affectation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleves.affectation', unique=True),
        ),
    ]
