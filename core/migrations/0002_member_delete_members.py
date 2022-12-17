# Generated by Django 4.1.4 on 2022-12-17 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lanme', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('passwd', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='Members',
        ),
    ]
