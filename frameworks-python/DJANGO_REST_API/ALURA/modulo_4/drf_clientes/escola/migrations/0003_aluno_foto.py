# Generated by Django 4.1.7 on 2023-03-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_aluno_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]