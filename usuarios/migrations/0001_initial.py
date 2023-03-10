# Generated by Django 4.1.4 on 2022-12-28 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('cod_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('cod_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=50, null=True)),
                ('documento', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('rol', models.CharField(blank=True, max_length=40, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('genero', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('cod_depto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_departamento', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_actualiza', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('cod_municipio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('act_usua', models.CharField(blank=True, max_length=8, null=True)),
                ('act_hora', models.CharField(blank=True, max_length=19, null=True)),
                ('cod_depto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.departamento')),
            ],
            options={
                'verbose_name': 'Division Politica',
                'verbose_name_plural': 'Division Politica',
            },
        ),
        migrations.CreateModel(
            name='Artesano',
            fields=[
                ('cod_artesano', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('cod_categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.categoria')),
                ('cod_depto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.departamento')),
                ('cod_municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.municipio')),
            ],
        ),
    ]
