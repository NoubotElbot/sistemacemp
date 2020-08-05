# Generated by Django 2.2.12 on 2020-08-05 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal'),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='imagenpublicacion',
            name='publicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Publicacion'),
        ),
        migrations.AddField(
            model_name='animaltratamiento',
            name='animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal'),
        ),
        migrations.AddField(
            model_name='animaltratamiento',
            name='tratamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Tratamiento'),
        ),
        migrations.AddField(
            model_name='animal',
            name='especie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='animal.Especie'),
        ),
        migrations.AddField(
            model_name='animal',
            name='id_adoptante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='animaltratamiento',
            unique_together={('animal', 'tratamiento', 'fecha_tratamiento')},
        ),
    ]
