# Generated by Django 4.2.18 on 2025-01-15 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=101)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_em_estoque', models.IntegerField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
