# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_id', models.PositiveIntegerField()),
                ('customer_name', models.CharField(max_length=100)),
                ('link_man', models.CharField(max_length=40)),
                ('telephone', models.CharField(max_length=11)),
                ('mobilephone', models.CharField(max_length=11)),
                ('foregift', models.FloatField()),
                ('reg_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='materInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('equipment_id', models.PositiveIntegerField()),
                ('equipment_name', models.CharField(max_length=100)),
                ('specification', models.CharField(max_length=50)),
                ('equipment_type', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('amount', models.PositiveIntegerField()),
                ('left_amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='materRentInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill_id', models.PositiveIntegerField()),
                ('bill_sequence_number', models.CharField(max_length=50)),
                ('lease_out_date', models.DateTimeField()),
                ('add_information', models.CharField(max_length=50)),
                ('lease_out_amount', models.PositiveIntegerField()),
                ('price_id', models.PositiveIntegerField()),
                ('customer_id', models.PositiveIntegerField()),
                ('equipment_id', models.PositiveIntegerField()),
                ('money', models.FloatField()),
                ('is_settled', models.BooleanField(default=False)),
                ('settled_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='priceInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price_id', models.PositiveIntegerField()),
                ('valid_date', models.DateTimeField()),
                ('site_name', models.CharField(max_length=100)),
                ('sequence_number', models.CharField(max_length=50)),
                ('equipment_name', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=50)),
                ('unitprice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='settleInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('settle_record_id', models.PositiveIntegerField()),
                ('customer_id', models.PositiveIntegerField()),
                ('last_settle_date', models.DateTimeField()),
                ('money', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='systemClientInoformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.PositiveIntegerField()),
                ('user_name', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=50)),
                ('stock', models.BooleanField(default=False)),
                ('data_input', models.BooleanField(default=False)),
                ('data_search', models.BooleanField(default=False)),
                ('account_settlement', models.BooleanField(default=False)),
                ('print_settlement', models.BooleanField(default=False)),
                ('print_checkup', models.BooleanField(default=False)),
                ('finance', models.BooleanField(default=False)),
                ('data_erase', models.BooleanField(default=False)),
                ('user_admin', models.BooleanField(default=False)),
            ],
        ),
    ]
