# Generated by Django 2.2.3 on 2019-07-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desh', '0002_auto_20190714_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='compalin',
            name='status',
            field=models.CharField(choices=[('Solved', 'Solved'), ('Inprogress', 'Inprogress')], default='Inprogress', max_length=20),
        ),
    ]
