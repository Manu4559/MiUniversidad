# Generated by Django 3.0.7 on 2022-05-04 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
