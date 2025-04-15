# Generated by Django 5.1.7 on 2025-04-15 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_livro_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='coautor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='livros_coautor', to='core.autor'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='livros_autor', to='core.autor'),
        ),
    ]
