from django.urls import path
from index.views import *

urlpatterns = [
    path("", index, name='index'),
    path('funcionarios', funcionarios, name='funcionarios'),
    path('<int:produto_id>/', detalhando_produto, name='produto_detalhado'),
    path('produtos', exibindo_produtos, name='exibindo_produtos')
]
