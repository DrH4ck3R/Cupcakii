from os import stat
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ClienteRegistrarView
from.import views
from django.urls import path
from django.urls import reverse







from .views import *


app_name = "lojaapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("sobre/", SobreView.as_view(), name="sobre"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("todos-produtos/", TodosProdutosView.as_view(), name="Todosprodutos"),
    path("produtos/<slug:slug>/", ProdutosDetalheView.as_view(), name="produtosdetalhe"),
    path("addcarro-<int:pro_id>/", AddCarroView.as_view(), name="addcarro"),
    path("meu-carro/", MeuCarroView.as_view(), name="meucarro"),
    path("manipular-carro/<int:cp_id>/", ManipularCarroView.as_view(), name="manipularcarro"),
    path("limpar-carro/", LimparCarroView.as_view(), name="limparcarro"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("clienteregistrar/", ClienteRegistrarView.as_view(), name="clienteregistrar"),
    path('clientesair/', ClienteSairView.as_view(), name='clientesair'),
    path('clienteentrar/', ClienteEntrarView.as_view(), name='clienteentrar'),
    path('clienteperfil/', ClientePerfilView.as_view(), name='clienteperfil'),
    path('clienteperfil/pedido-<int:pk>/', ClientePerfilDetalheView.as_view(), name='clientepedidodetalhe'),
    path('admin-login/', AdminLoginView.as_view(), name='adminlogin'),
    path('admin-home/', AdminHomeView.as_view(), name='adminhome'),
    path('admin-pedido/<int:pk>/', AdminPedidoDetalheView.as_view(), name='adminpedidodetalhe'),
    path('admin-todos-pedidos/', AdminPedidoListaView.as_view(), name='adminpedidolista'),
    path("admin-pedido-<int:pk>/-mudar", AdminPedidoMudarStatusView.as_view(), name='adminpedidomudar'),
    path("pesquisar/", PesquisarView.as_view(), name='pesquisar'),
    path("pagamento/", PagamentoView.as_view(), name='pagamento'),
    
    

    

    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)