# Generated by Django 3.2.18 on 2023-06-11 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.IntegerField()),
                ('boofrom', models.CharField(max_length=50)),
                ('bookTo', models.CharField(max_length=50)),
                ('dep_date', models.DateField()),
            ],
        ),
    ]
