# Generated by Django 4.2.6 on 2023-10-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_heading', models.CharField(default='', max_length=50, null=True)),
                ('Task_description', models.CharField(default='', max_length=300, null=True)),
            ],
        ),
    ]
