# Generated by Django 3.2.16 on 2023-02-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20230205_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='token',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='jwt认证token'),
        ),
    ]
