# Generated by Django 4.0.4 on 2022-05-23 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisites',
            name='inn',
            field=models.CharField(help_text='Индивидуальный номер налогоплательщика компании', max_length=12, unique=True, verbose_name='ИНН'),
        ),
    ]
