# Generated by Django 2.0.5 on 2018-09-29 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_veiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=2000)),
                ('estado', models.CharField(max_length=15)),
                ('cep', models.CharField(max_length=15)),
            ],
        ),
    ]
