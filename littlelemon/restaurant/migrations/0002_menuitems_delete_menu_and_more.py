# Generated by Django 4.2.4 on 2023-09-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='menu',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='BookingDate',
            new_name='booking_date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='No_of_guest',
            new_name='no_of_guest',
        ),
    ]
