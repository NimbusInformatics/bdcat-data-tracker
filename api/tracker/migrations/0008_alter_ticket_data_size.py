# Generated by Django 4.0 on 2021-12-21 17:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_ticket_data_unit_alter_ticket_data_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='data_size',
            field=models.CharField(blank=True, default='', help_text='Please provide an estimated size of your data set(s)', max_length=100, validators=[django.core.validators.RegexValidator('^[0-9]{1,5}$', 'Data Size must be a number')], verbose_name='Data Size'),
        ),
    ]