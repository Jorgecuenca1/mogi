# Generated by Django 4.2.10 on 2024-02-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagina',
            name='imagen',
            field=models.ImageField(default=1, help_text='Imagen ', upload_to='', verbose_name='Imagen '),
            preserve_default=False,
        ),
    ]
