# Generated by Django 2.2.12 on 2020-07-15 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0003_auto_20200715_1342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagenpublicacion',
            options={'verbose_name': 'Imagen Publicacion', 'verbose_name_plural': 'Imagenes Publicaciones'},
        ),
        migrations.AlterModelOptions(
            name='publicacion',
            options={'verbose_name': 'Publicacion', 'verbose_name_plural': 'Publicaciones'},
        ),
        migrations.AlterModelTable(
            name='imagenpublicacion',
            table='IMAGEN_PUBLICACION',
        ),
        migrations.AlterModelTable(
            name='publicacion',
            table='PUBLICACION',
        ),
    ]