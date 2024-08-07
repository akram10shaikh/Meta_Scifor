# Generated by Django 5.0.3 on 2024-06-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person_Detail',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('phone_no', models.IntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('aadhar_no', models.IntegerField()),
                ('pan_no', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('university_name', models.CharField(max_length=200)),
                ('date_of_addmission', models.DateField()),
                ('date_of_leaving', models.DateField()),
                ('father_name', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
    ]
