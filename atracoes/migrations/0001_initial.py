# Generated by Django 2.2.7 on 2019-11-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('horario_func', models.TextField()),
                ('idade_minima', models.IntegerField()),
            ],
        ),
    ]
