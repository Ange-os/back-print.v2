# Generated by Django 5.1 on 2024-08-21 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_project', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=128)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layer_type', models.CharField(choices=[('TEXT', 'Texto'), ('IMAGE', 'Imagen'), ('SHAPE', 'Forma'), ('FILTRO', 'Filtro')], max_length=10)),
                ('content', models.TextField()),
                ('position', models.JSONField()),
                ('size', models.JSONField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='layers', to='print.project')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_template', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='templates', to='print.project')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='print.users')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='print.users'),
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_asset', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='assets/')),
                ('uploaded_at', models.DateField(auto_now_add=True)),
                ('layer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='print.layer')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='print.project')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='print.users')),
            ],
        ),
    ]
