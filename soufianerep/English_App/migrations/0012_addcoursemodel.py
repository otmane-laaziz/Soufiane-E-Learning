# Generated by Django 4.1.1 on 2022-11-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('English_App', '0011_alter_contactposts_options_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=50)),
                ('courseBody', models.TextField()),
            ],
        ),
    ]
