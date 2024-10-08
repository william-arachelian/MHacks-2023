# Generated by Django 4.2.7 on 2023-11-19 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.IntegerField()),
                ('total_fat', models.IntegerField()),
                ('trans_fat', models.IntegerField()),
                ('sat_fat', models.IntegerField()),
                ('carbs', models.IntegerField()),
                ('sugar', models.IntegerField()),
                ('fiber', models.IntegerField()),
                ('cholesterol', models.IntegerField()),
                ('sodium', models.IntegerField()),
                ('protein', models.IntegerField()),
            ],
        ),
    ]
