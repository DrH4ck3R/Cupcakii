from django.contrib import admin
from .models import Cliente, Categoria, Produto, Pedido, ItemPedido, Carro, CarroProduto, Pedido_order,Admin

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido

class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]

class CarroProdutoInline(admin.TabularInline):
    model = CarroProduto

class CarroAdmin(admin.ModelAdmin):
    inlines = [CarroProdutoInline]

admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Carro, CarroAdmin)
admin.site.register(Pedido_order)
admin.site.register(Admin)

