from fastapi import FastAPI
print("hello")
app = FastAPI()
'''
item_venda = {
    1: {"item": "coca-cola", "preco_unitario":5, "quantidade":5},
    2: {"item": "cerveja 600ml", "preco_unitario":10, "quantidade":5},
    3: {"item": "vinho 750ml", "preco_unitario":30, "quantidade":5},
    4: {"item": "gin", "preco_unitario":100, "quantidade":5},
}

@app.get('/')
def home():
    return {"APP de vendas com FastAPI"}

@app.get('/vendas/{id_venda}')
def selecionar_venda_por_id(id_venda: int):
    if id_venda in item_venda:
        return item_venda[id_venda]
    else:
        return {'Erro': 'ID da venda nao existe.'}
'''
# GET METHOD
@app.get('/getdata/{nome_do_usuario}')
def get_data(nome_do_usuario: str):
    return {
        'nome': nome_do_usuario
        }

# POST METHOD
@app.post('/postdata/')
def post_data(nome_do_usuario: str):
    return {
        'nome': nome_do_usuario
    }

# PUT METHOD
lista_de_nomes = []
@app.put('/putdata/{nome_do_usuario}')
def put_data(nome_do_usuario: str):
    lista_de_nomes.append(nome_do_usuario)
    return {
        'nome_do_usuario':lista_de_nomes
    }
    
# DELETE METHOD
@app.delete('/deletedata/{nome_do_usuario}')
def delete_data(nome_do_usuario: str):
    lista_de_nomes.remove(nome_do_usuario)
    return {
        'nome_do_usuario':lista_de_nomes
    }