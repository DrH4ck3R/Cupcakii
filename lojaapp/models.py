from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    data_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Categoria(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titulo

class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="cupcakes", default='path/to/default/image.jpg')
    preco_mercado = models.PositiveIntegerField()
    venda = models.PositiveIntegerField()
    descricao = models.TextField()
    garantia = models.CharField(max_length=300, null=True, blank=True)
    return_devolucao = models.CharField(max_length=300, null=True, blank=True)
    visualizacao = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ManyToManyField(Produto, through='ItemPedido')
    criado_em = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Pedido {self.id} - {self.cliente.nome}'

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Item do pedido {self.pedido.id} - {self.produto.titulo}'
    
    
class Carro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Carro " + str(self.id)

class CarroProduto(models.Model):
    carro = models.ForeignKey(Carro,on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    avaliacao = models.PositiveIntegerField()
    quantidade = models.PositiveIntegerField()
    subtotal= models.PositiveIntegerField()
    
    def __str__(self):
        return "Carro:" + str(self.carro.id) + "CarroProduto:" + str(self.id)
    
PEDIDO_STATUS=(
    ("Pedido Recebido","Pedido Recebido"),
    ("Pedido Processando","Pedido Processando"),
    ("Pedido Caminho","Pedido Caminho"),
    ("Pedido Completado","Pedido Completado"),
    ("Pedido Cancelado","Pedido Cancelado"),
)


METHOD=(
    ("Dinheiro Na Entrega","Dinheiro Na Entrega"),
    ("Khalti","Khalti"),
)

class Pedido_order(models.Model):
    carro = models.OneToOneField(Carro, on_delete=models.CASCADE)  
    ordenando_por = models.CharField(max_length=200)
    endereco_envio = models.CharField(max_length=200)
    telefone = models.CharField(max_length=12)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    desconto = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField()
    pedido_status = models.CharField(max_length=50, choices=PEDIDO_STATUS)
    criado_em = models.DateTimeField(auto_now_add=True)
    pagamento_method = models.CharField(max_length=20, choices=METHOD, default="Dinheiro Na Entrega")
    pagamento_completo = models.BooleanField(default=False,null=True, blank=True)
    

    def __str__(self):
        return "Pedido_order:" + str(self.id)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=200)
    image = models.ImageField(upload_to="admins")
    tel = models.CharField(max_length=20)
    def __str__(self):
        return self.user.username
    
class Icon(models.Model):
    image = models.ImageField(upload_to='Icon/')    
    
