# Generated by Django 3.1.6 on 2021-02-16 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_name', models.IntegerField()),
                ('n_sig', models.CharField(blank=True, max_length=100)),
                ('fs', models.CharField(blank=True, max_length=100)),
                ('counter_freq', models.CharField(blank=True, max_length=100)),
                ('base_counter', models.CharField(blank=True, max_length=100)),
                ('sig_len', models.CharField(blank=True, max_length=100)),
                ('base_time', models.CharField(blank=True, max_length=100)),
                ('base_date', models.CharField(blank=True, max_length=100)),
                ('comments', models.CharField(blank=True, max_length=100)),
                ('sig_name', models.CharField(blank=True, max_length=100)),
                ('p_signal', models.CharField(blank=True, max_length=100)),
                ('d_signal', models.CharField(blank=True, max_length=100)),
                ('e_p_signal', models.CharField(blank=True, max_length=100)),
                ('file_name', models.CharField(blank=True, max_length=100)),
                ('fmt', models.CharField(blank=True, max_length=100)),
                ('samps_per_frame', models.CharField(blank=True, max_length=100)),
                ('skew', models.CharField(blank=True, max_length=100)),
                ('byte_offset', models.CharField(blank=True, max_length=100)),
                ('adc_gain', models.CharField(blank=True, max_length=100)),
                ('baseline', models.CharField(blank=True, max_length=100)),
                ('units', models.CharField(blank=True, max_length=100)),
                ('adc_res', models.CharField(blank=True, max_length=100)),
                ('adc_zero', models.CharField(blank=True, max_length=100)),
                ('init_value', models.CharField(blank=True, max_length=100)),
                ('checksum', models.CharField(blank=True, max_length=100)),
                ('block_size', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Signals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.FloatField()),
                ('mlii', models.FloatField()),
                ('v5', models.FloatField()),
                ('signal_record_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signal_record_name', to='patientdb.patient')),
            ],
        ),
    ]
