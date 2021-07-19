# Generated by Django 3.2.4 on 2021-07-15 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
