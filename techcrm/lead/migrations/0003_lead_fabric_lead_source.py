# Generated by Django 4.1.10 on 2023-08-08 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0002_lead_converted_to_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='fabric',
            field=models.CharField(choices=[('silk', 'silk'), ('cotton', 'cotton'), ('polyster', 'polyster'), ('wool', 'wool'), ('satin', 'satin'), ('velvet', 'velvet')], default='cotton', max_length=20),
        ),
        migrations.AddField(
            model_name='lead',
            name='source',
            field=models.CharField(choices=[('instagram', 'instagram'), ('google_ads', 'google_ads'), ('wom', 'wom'), ('facebook', 'facebook'), ('email_marketing', 'email_marketing'), ('others', 'others')], default='google_ads', max_length=50),
        ),
    ]