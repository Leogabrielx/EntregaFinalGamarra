# Generated by Django 4.2.5 on 2023-10-03 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_articulo_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppBlog.autor'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppBlog.categoria'),
        ),
    ]
