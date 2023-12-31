import json
import sqlite3
from data.database import Database, Note

def extract_route(request):
    request = request.split(" ")
    if request[1].startswith('/'):
        request = request[1].replace("/", "", 1)
    return request

def read_file(caminho):
    with open(caminho, mode='rb') as file:
        x = file.read()
    return x

def load_data(db):
    data_base = Database(db)
    dic = data_base.get_all()
    print(dic)
    return dic
    
def load_template(index):
    with open('templates/' + index, "r", encoding="UTF-8" ) as arquivo:
        return arquivo.read()



'''def load_template(arquivo):
    if arquivo[0:9] != "templates/":
        arquivo = 'templates/' + arquivo
    with open(arquivo, 'r') as file:
        conteudo = file.read()
    return conteudo'''
    #with open('templates/' + index, "r" ) as arquivo:
        #return arquivo.read()
    
def adiciona_nota(anotacao):
    db = Database('banco')
    titulo = anotacao['titulo']
    detalhes = anotacao['detalhes']
    db.add(Note(title=titulo, content=detalhes))


def delete_nota(note_id):
    db = Database('banco')
    db.delete(Note(id=note_id))

def build_response(body='', code=200, reason='OK', headers=''):
    response = f'HTTP/1.1 {code} {reason}\n'
    if headers:
        response += headers + '\n'
    response += '\n' + body
    return response.encode()