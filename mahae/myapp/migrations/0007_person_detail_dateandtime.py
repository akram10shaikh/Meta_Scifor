# Generated by Django 5.0.3 on 2024-06-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_document_ready'),
    ]

    operations = [
        migrations.AddField(
            model_name='person_detail',
            name='dateandtime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]