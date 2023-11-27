# Generated by Django 3.1.3 on 2023-11-02 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lojaapp', '0002_auto_20231102_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.cliente')),
            ],
        ),
        migrations.RemoveField(
            model_name='carroproduto',
            name='carro',
        ),
        migrations.RemoveField(
            model_name='carroproduto',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='pedido_order',
            name='carro',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='image',
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='cupcakes'),
        ),
        migrations.DeleteModel(
            name='Carro',
        ),
        migrations.DeleteModel(
            name='CarroProduto',
        ),
        migrations.DeleteModel(
            name='Pedido_order',
        ),
        migrations.AddField(
            model_name='pedido',
            name='produtos',
            field=models.ManyToManyField(through='lojaapp.ItemPedido', to='lojaapp.Produto'),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.pedido'),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojaapp.produto'),
        ),
    ]
