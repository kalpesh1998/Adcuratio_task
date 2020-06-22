# Generated by Django 3.0.6 on 2020-06-20 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.TextField(blank=True, max_length=15, null=True)),
                ('invoice_date', models.DateField()),
                ('seller', models.TextField(blank=True, max_length=40, null=True)),
                ('seller_add', models.TextField(blank=True, max_length=100, null=True)),
                ('buyer_name', models.CharField(blank=True, max_length=32, null=True)),
                ('buyer_mobile', models.IntegerField()),
                ('items', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='uploader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='documents/')),
            ],
        ),
    ]