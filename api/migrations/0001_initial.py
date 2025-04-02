# Generated by Django 5.0.4 on 2024-04-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('idOrder', models.AutoField(primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(blank=True)),
                ('guarantee', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True, default='', max_length=500)),
                ('price', models.FloatField(default=0.0)),
                ('phoneNumber', models.CharField(blank=True, default='', max_length=30)),
                ('nameCustomer', models.CharField(default='', max_length=100)),
                ('surnameCustomer', models.CharField(blank=True, default='', max_length=100)),
                ('pieceName', models.CharField(blank=True, default='', max_length=100)),
                ('status', models.CharField(default='in', max_length=3)),
                ('brandPhone', models.CharField(blank=True, default='', max_length=30)),
                ('modelPhone', models.CharField(default='', max_length=50)),
                ('defect', models.TextField(default='', max_length=100)),
                ('shipped', models.IntegerField(choices=[(0, 'Not shipped'), (1, 'Shipped'), (2, 'In shop')], default=0)),
                ('clientAdviser', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
    ]
