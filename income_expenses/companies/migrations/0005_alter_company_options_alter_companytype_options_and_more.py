# Generated by Django 4.0.4 on 2022-06-01 04:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_company_email_alter_company_phone_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name'], 'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
        migrations.AlterModelOptions(
            name='companytype',
            options={'ordering': ['name'], 'verbose_name': 'Тип компании', 'verbose_name_plural': 'Типы компаний'},
        ),
        migrations.AlterModelOptions(
            name='requisites',
            options={'ordering': ['inn'], 'verbose_name': 'Реквизиты', 'verbose_name_plural': 'Реквизиты'},
        ),
        migrations.AddField(
            model_name='company',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='Автоматически задается при создании', verbose_name='Дата и время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, help_text='Автоматически задается при изменении', verbose_name='Дата и время изменения'),
        ),
        migrations.AddField(
            model_name='companytype',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='Автоматически задается при создании', verbose_name='Дата и время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companytype',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, help_text='Автоматически задается при изменении', verbose_name='Дата и время изменения'),
        ),
        migrations.AddField(
            model_name='requisites',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='Автоматически задается при создании', verbose_name='Дата и время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requisites',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, help_text='Автоматически задается при изменении', verbose_name='Дата и время изменения'),
        ),
    ]
