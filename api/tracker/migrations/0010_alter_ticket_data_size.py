# Generated by Django 4.0 on 2021-12-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_remove_ticket_data_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='data_size',
            field=models.CharField(blank=True, default='', help_text='Please provide an estimated size of your data set(s)', max_length=100, verbose_name='Data Size'),
        ),
    ]