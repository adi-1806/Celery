# Generated by Django 4.2 on 2023-04-10 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReadCsv', '0003_studentdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='owner',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]