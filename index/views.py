from django.shortcuts import render
import requests
import json

def index(request):
    return render(request, 'index.html')

def funcionarios(request):
    return render(request, 'funcionarios.html')

def produtos(request):
    return render(request, 'produtos.html')

def detalhando_produto(request, produto_id):
    r = requests.get('http://18.231.157.213/api/products/'+str(produto_id), auth=('Publico', 'usuariopublico'))
    produto = json.loads(r.content)
    
    produtos_a_exibir = {
        'produto': produto,
        'url': produto['url'],
        'product_code': produto['product_code'],
        'product_name': produto['product_name'],
        'description': produto['description'],
        'standard_cost': produto['standard_cost'],
        'list_price': produto['list_price'],
        'reorder_level': produto['reorder_level'],
        'target_level': produto['target_level'],
        'quantity_per_unit': produto['quantity_per_unit'],
        'discontinued': produto['discontinued'],
        'minimun_reorder_quantity': produto['minimun_reorder_quantity'],
        'category': produto['category'],
        'attachaments': produto['attachaments'],
        'status': produto['status'],
        'UnitsInStock': produto['UnitsInStock'],
        'supplyers_ids': produto['supplyers_ids'],
    }

    
    return render(request, 'detalhe_produto.html', produtos_a_exibir)