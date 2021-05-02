# Generated by Django 3.2 on 2021-05-02 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('merchant_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('products', models.TextField()),
                ('total_weight', models.IntegerField()),
                ('destinations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='percel.destination')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=100)),
                ('percel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='percel.merchant')),
            ],
        ),
    ]