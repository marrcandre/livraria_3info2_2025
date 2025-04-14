# Generated by Django 5.1.7 on 2025-04-14 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_livro'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.categoria'),
        ),
    ]
