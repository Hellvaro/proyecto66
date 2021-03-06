# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 23:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenBanda', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='bandas', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('nombreBanda', models.CharField(max_length=100)),
                ('descripcionBanda', models.TextField(max_length=400)),
                ('miembros', models.TextField(max_length=100)),
                ('anioFormacion', models.IntegerField()),
                ('historia', models.TextField(max_length=700)),
                ('discografia', models.TextField(max_length=650)),
                ('videoBanda', embed_video.fields.EmbedVideoField()),
                ('contacto', models.CharField(max_length=200)),
                ('bandaCreacion', models.DateTimeField(auto_now_add=True)),
                ('beneficio1', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-bandaCreacion'],
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreComuna', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEstilo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreInstrumento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenLocal', models.ImageField(blank=True, height_field='height_field', upload_to='locales', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('nombreLocal', models.CharField(max_length=80)),
                ('descripcion', models.TextField(max_length=700)),
                ('buscaBanda', models.BooleanField(verbose_name=False)),
                ('buscaMusico', models.BooleanField(verbose_name=False)),
                ('contacto', models.CharField(max_length=200)),
                ('horarios', models.TextField(default='', max_length=200)),
                ('localCreacion', models.DateTimeField(auto_now_add=True)),
                ('beneficio1', models.BooleanField(default=False)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appmusicoenvivo.Comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Musico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenMusico', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='musicos', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('nombreMusico', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('expFormacion', models.TextField(max_length=450)),
                ('dispEnsayo', models.TextField(max_length=200)),
                ('dispConciertos', models.TextField(max_length=200)),
                ('dispInmediata', models.BooleanField()),
                ('equipado', models.BooleanField()),
                ('descripcionEquipo', models.TextField(blank=True, max_length=450)),
                ('contacto', models.CharField(max_length=200)),
                ('aniosExperiencia', models.IntegerField()),
                ('descripcionPersonal', models.TextField(blank=True, max_length=400)),
                ('videoMusico', embed_video.fields.EmbedVideoField()),
                ('buscaBanda', models.BooleanField()),
                ('influencias', models.TextField(max_length=400)),
                ('clasesParticulares', models.BooleanField()),
                ('musicoCreacion', models.DateTimeField(auto_now_add=True)),
                ('beneficio1', models.BooleanField(default=False)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appmusicoenvivo.Comuna')),
                ('estilo', models.ManyToManyField(to='appmusicoenvivo.Estilo')),
                ('instrumento', models.ManyToManyField(to='appmusicoenvivo.Instrumento')),
                ('usuario', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-musicoCreacion'],
            },
        ),
        migrations.CreateModel(
            name='Tipo_Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipoLocal', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='local',
            name='tipo_Local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appmusicoenvivo.Tipo_Local'),
        ),
        migrations.AddField(
            model_name='local',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='banda',
            name='comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appmusicoenvivo.Comuna'),
        ),
        migrations.AddField(
            model_name='banda',
            name='estilo',
            field=models.ManyToManyField(to='appmusicoenvivo.Estilo'),
        ),
        migrations.AddField(
            model_name='banda',
            name='musicos',
            field=models.ManyToManyField(blank=True, to='appmusicoenvivo.Instrumento'),
        ),
        migrations.AddField(
            model_name='banda',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
