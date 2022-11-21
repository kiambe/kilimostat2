# Generated by Django 4.1.3 on 2022-11-16 07:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
                ('code', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DomainElement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('domainelement', models.CharField(max_length=256, null=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kilimodata.domain')),
            ],
        ),
        migrations.CreateModel(
            name='ElementItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flags',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemSpecify',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
                ('itemCategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kilimodata.itemcategory')),
            ],
        ),
        migrations.CreateModel(
            name='SubCounty',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('lat', models.CharField(blank=True, max_length=256, null=True)),
                ('lng', models.CharField(blank=True, max_length=256, null=True)),
                ('category', models.CharField(blank=True, max_length=256, null=True)),
                ('code', models.CharField(blank=True, max_length=256, null=True)),
                ('loccode', models.CharField(blank=True, max_length=256, null=True)),
                ('county_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kilimodata.county')),
            ],
        ),
        migrations.CreateModel(
            name='SubSector',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UoM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('lat', models.CharField(blank=True, max_length=256, null=True)),
                ('lng', models.CharField(blank=True, max_length=256, null=True)),
                ('category', models.CharField(blank=True, max_length=256, null=True)),
                ('code', models.CharField(blank=True, max_length=256, null=True)),
                ('loccode', models.CharField(blank=True, max_length=256, null=True)),
                ('county_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kilimodata.county')),
                ('subcounty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kilimodata.subcounty')),
            ],
        ),
        migrations.CreateModel(
            name='KilimoData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('referenceperiod', models.PositiveIntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2090)])),
                ('value', models.FloatField()),
                ('datasource', models.CharField(max_length=256, null=True)),
                ('doneby', models.CharField(max_length=256, null=True)),
                ('validated', models.BooleanField()),
                ('publish', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kilimodata.county')),
                ('domainelement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kilimodata.domainelement')),
                ('elementitem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kilimodata.elementitem')),
                ('flagdescription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kilimodata.flags')),
                ('itemspecify', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kilimodata.itemspecify')),
                ('subsector', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kilimodata.subsector')),
                ('uom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kilimodata.uom')),
            ],
        ),
        migrations.CreateModel(
            name='DataEntryOfficer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nationalid', models.CharField(max_length=256, null=True)),
                ('firstname', models.CharField(max_length=256, null=True)),
                ('lastname', models.CharField(max_length=256, null=True)),
                ('telephone', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=256, null=True)),
                ('designation', models.CharField(max_length=256, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='kilimodata.institution')),
            ],
        ),
    ]
