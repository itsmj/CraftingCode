# Generated by Django 3.1.3 on 2020-12-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=30)),
                ('courseimage', models.ImageField(upload_to='pic')),
                ('coursedesc', models.TextField()),
                ('courseprice', models.IntegerField()),
            ],
        ),
    ]