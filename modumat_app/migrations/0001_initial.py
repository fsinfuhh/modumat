# Generated by Django 3.1.3 on 2020-11-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shorthand', models.CharField(max_length=20)),
                ('module_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
