# Generated by Django 3.1.1 on 2020-09-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_remove_recordsmodel_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordsmodel',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
