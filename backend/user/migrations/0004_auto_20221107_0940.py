# Generated by Django 3.2 on 2022-11-07 06:40

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_code_send_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Code sent date'),
        ),
        migrations.AddField(
            model_name='user',
            name='email_confirmation_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Email confirmation code'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Запись удалена'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_email_confirmed',
            field=models.BooleanField(default=True, verbose_name='Email confirmed'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_phone_confirmed',
            field=models.BooleanField(default=True, verbose_name='Phone number confirmed'),
        ),
        migrations.AddField(
            model_name='user',
            name='new_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='New email'),
        ),
        migrations.AddField(
            model_name='user',
            name='new_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='New phone number'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_code_send_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Code sent date'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_confirmation_code',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone confirmation code'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='', max_length=128, region=None, verbose_name='Phone number'),
        ),
    ]