# Generated by Django 5.1.1 on 2024-10-18 08:28

from django.db import migrations, models # type: ignore

class Migration(migrations.Migration):

    dependencies = [
        ('jugaripunt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='session_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
