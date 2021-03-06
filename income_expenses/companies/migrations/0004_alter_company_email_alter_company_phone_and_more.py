# Generated by Django 4.0.4 on 2022-05-31 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_alter_company_email_alter_company_site_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, help_text='Основная электронная почта компании', max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(blank=True, help_text='Основной телефон компании', max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='company',
            name='site',
            field=models.URLField(blank=True, help_text='Сайт компании', verbose_name='Сайт'),
        ),
        migrations.AlterField(
            model_name='requisites',
            name='position_director',
            field=models.CharField(blank=True, default='Директор', help_text='Наименование должности руководителя компании (напр. Директор, Генеральный директор и т.п.', max_length=50, verbose_name='Должность руководителя'),
        ),
    ]
