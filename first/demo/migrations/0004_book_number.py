# Generated by Django 3.0.4 on 2020-03-05 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_booknumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.BookNumber'),
        ),
    ]
