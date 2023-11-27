# Generated by Django 3.1.3 on 2023-11-02 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lojaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carros', to='lojaapp.cliente'),
        ),
        migrations.AlterField(
            model_name='carroproduto',
            name='carro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='lojaapp.carro'),
        ),
        migrations.AlterField(
            model_name='pedido_order',
            name='carro',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pedido', to='lojaapp.carro'),
        ),
    ]
