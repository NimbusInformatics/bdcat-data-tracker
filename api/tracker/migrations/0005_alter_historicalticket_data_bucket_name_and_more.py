# Generated by Django 4.0.2 on 2022-10-12 00:11

import django.core.validators
from django.db import migrations, models
import tracker.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_alter_historicalticket_aws_iam_alter_ticket_aws_iam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalticket',
            name='data_bucket_name',
            field=models.CharField(blank=True, default='', help_text='Name of Cloud Data Bucket', max_length=250, validators=[django.core.validators.MinLengthValidator(3, 'Bucket name must have at least 3 characters'), django.core.validators.MaxLengthValidator(63, 'Bucket can be no more than 63 characters'), django.core.validators.RegexValidator('^[a-z.0-9-]*$', 'Bucket name can only contain lower case letters, decimals, numbers, and hyphens'), django.core.validators.RegexValidator('^[a-z0-9].*[a-z0-9]$', ' Bucket name must begin and end in a letter or number'), django.core.validators.RegexValidator('^xn--', "Bucket name cannot begin with 'xn--'", inverse_match=True), django.core.validators.RegexValidator('-s3alias$', "Bucket name cannot end with '-s3alias'", inverse_match=True), django.core.validators.RegexValidator('\\.\\.', 'Bucket name cannot contain two or more consecutive periods', inverse_match=True), tracker.validators.NegateValidator(django.core.validators.validate_ipv4_address, 'Bucket name cannot be an ip address')], verbose_name='Data Bucket Name'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='data_bucket_name',
            field=models.CharField(blank=True, default='', help_text='Name of Cloud Data Bucket', max_length=250, validators=[django.core.validators.MinLengthValidator(3, 'Bucket name must have at least 3 characters'), django.core.validators.MaxLengthValidator(63, 'Bucket can be no more than 63 characters'), django.core.validators.RegexValidator('^[a-z.0-9-]*$', 'Bucket name can only contain lower case letters, decimals, numbers, and hyphens'), django.core.validators.RegexValidator('^[a-z0-9].*[a-z0-9]$', ' Bucket name must begin and end in a letter or number'), django.core.validators.RegexValidator('^xn--', "Bucket name cannot begin with 'xn--'", inverse_match=True), django.core.validators.RegexValidator('-s3alias$', "Bucket name cannot end with '-s3alias'", inverse_match=True), django.core.validators.RegexValidator('\\.\\.', 'Bucket name cannot contain two or more consecutive periods', inverse_match=True), tracker.validators.NegateValidator(django.core.validators.validate_ipv4_address, 'Bucket name cannot be an ip address')], verbose_name='Data Bucket Name'),
        ),
    ]
