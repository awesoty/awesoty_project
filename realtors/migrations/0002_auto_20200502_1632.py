# Generated by Django 3.0.5 on 2020-05-02 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='descriptions',
            new_name='description',
        ),
    ]
