# Generated by Django 5.1.5 on 2025-03-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleblog', '0033_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
