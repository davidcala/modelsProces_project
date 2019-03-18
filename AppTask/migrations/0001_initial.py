# Generated by Django 2.1.7 on 2019-03-18 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Inactivo', 'Inactivo'), ('Activo', 'Activo')], default=1, max_length=20, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, default='', verbose_name='Descripción')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_category', to='AppTask.Category', verbose_name='Categoría Padre')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Inactivo', 'Inactivo'), ('Activo', 'Activo')], default=1, max_length=20, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')),
                ('product_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Código Producto')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Precio')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Stock')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='AppTask.Category', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Inactivo', 'Inactivo'), ('Activo', 'Activo')], default=1, max_length=20, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, default='', verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Etiqueta',
                'verbose_name_plural': 'Etiquetas',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='product_tags', to='AppTask.Tag'),
        ),
    ]
