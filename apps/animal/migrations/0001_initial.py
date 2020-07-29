# Generated by Django 2.2.12 on 2020-07-29 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, max_length=350, null=True, verbose_name='Descripcion del animal')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha nacimiento')),
                ('sexo', models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], max_length=10, verbose_name='Sexo')),
                ('tamaño', models.CharField(choices=[('Pequeño', 'Pequeño'), ('Mediano', 'Mediano'), ('Grande', 'Grande')], max_length=10, verbose_name='Tamaño')),
                ('esterilizado', models.BooleanField(default=False, verbose_name='Esterilizado')),
                ('fecha_llegada', models.DateField(verbose_name='Fecha de llegada a la sede')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Peso kg')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creacion registro')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Ultima modificacion')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagen')),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animales',
                'db_table': 'ANIMAL',
            },
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_especie', models.CharField(max_length=30, verbose_name='Especie')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Especie',
                'verbose_name_plural': 'Especies',
                'db_table': 'ESPECIE',
            },
        ),
        migrations.CreateModel(
            name='EstadosSolicitud',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estado', models.CharField(max_length=15)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Estado solicitud',
                'verbose_name_plural': 'Estados de solicitudes',
                'db_table': 'ESTADO_SOLICITUD',
            },
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Tratamiento')),
                ('descripcion', models.TextField(max_length=200, verbose_name='Descripcion')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creacion registro')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Ultima modificacion')),
            ],
            options={
                'verbose_name': 'Tratamiento',
                'verbose_name_plural': 'Tratamientos',
                'db_table': 'TRATAMIENTO',
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Solicitud')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal')),
                ('estado_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.EstadosSolicitud')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud Animal',
                'verbose_name_plural': 'Solicitudes Animales',
                'db_table': 'SOLICITUD',
            },
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField(blank=True, max_length=400)),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
                'db_table': 'PUBLICACION',
            },
        ),
        migrations.CreateModel(
            name='ImagenPublicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruta_imagen', models.ImageField(blank=True, null=True, upload_to='publicacion')),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Publicacion')),
            ],
            options={
                'verbose_name': 'Imagen Publicacion',
                'verbose_name_plural': 'Imagenes Publicaciones',
                'db_table': 'IMAGEN_PUBLICACION',
            },
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
        migrations.CreateModel(
            name='AnimalTratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_tratamiento', models.DateField(verbose_name='Fecha de aplicacion')),
                ('comentario', models.TextField(blank=True, max_length=200, verbose_name='Comentario')),
                ('estado', models.CharField(choices=[('Vigente', 'Vigente'), ('Concluido', 'Concluido')], default='Vigente', max_length=10, verbose_name='Estado tratamiento')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal')),
                ('tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Tratamiento')),
            ],
            options={
                'verbose_name': 'Animal tratamiento',
                'verbose_name_plural': 'Animales tratados',
                'db_table': 'ANIMAL_TRATAMIENTO',
                'unique_together': {('animal', 'tratamiento', 'fecha_tratamiento')},
            },
        ),
    ]
