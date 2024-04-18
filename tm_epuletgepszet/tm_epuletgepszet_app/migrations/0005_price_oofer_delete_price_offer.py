# Generated by Django 5.0.4 on 2024-04-18 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm_epuletgepszet_app', '0004_alter_price_offer_name_alter_price_offer_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price_oofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Price_offer',
        ),
    ]