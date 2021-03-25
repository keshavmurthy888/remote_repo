# Generated by Django 3.1.7 on 2021-03-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=50)),
                ('USN', models.IntegerField(max_length=10)),
                ('PHONE_NUMBER', models.CharField(max_length=10)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('GENDER', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Student_Detail',
                'verbose_name_plural': 'Student_Details',
            },
        ),
    ]
