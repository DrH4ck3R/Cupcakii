# Generated by Django 3.1.3 on 2023-11-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojaapp', '0010_auto_20231110_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido_order',
            name='desconto',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pedido_order',
            name='subtotal',
            field=models.PositiveIntegerField(),
        ),
    ]
