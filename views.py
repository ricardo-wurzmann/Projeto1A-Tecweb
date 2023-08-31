from data.database import Database, Note
from utils import load_data, load_template, adiciona_nota, build_response, delete_nota
import string

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        partes = request.split('\n\n')
        corpo = partes[1]       
        params = {}
        for chave_valor in corpo.split('&'):
            chave_valor = chave_valor.replace("+", ' ')
            post = chave_valor.find("=")
            params[chave_valor [:post]] = chave_valor[post+1:]
            
        adiciona_nota(params)

        return build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template('components/note.html')

    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]

    print('?'*100)
    print(notes_li)

    notes = '\n'.join(notes_li)
    print(notes)

    response_body = load_template('index.html').format(notes=notes)
    return build_response(body=response_body)


    '''for index, dados in enumerate(load_data('banco.db')):
        id_txt = str(index+1)
        txt = 'POST / delete' + id_txt
        if request.startswith(txt):
            delete_nota(id_txt)
            return build_response(code=303, reason="See other", headers="Location: /")'''



def delete_note(route):
    note_id = int(route.split()[-1])
    db = Database("banco")  # Crie uma instância do Database
    if db.delete(note_id):
        db.close_connection()
        return build_response(code=303, reason="See Other", headers="Location: /")
    else:
        db.close_connection()
        return build_response(code=404, reason="Not Found")

def edit_note(route):
    note_id = int(route.split()[-1])
    db = Database("banco")  # Crie uma instância do Database


def create_note(request):
    if request.startswith('POST /create'):
        # Processar os dados do formulário enviado
        content_length = int(request.headers['Content-Length'])
        post_data = request.split('\r\n\r\n', 1)[1]
        params = {}
        for item in post_data.split('&'):
            key, value = item.split('=')
            params[key] = value

        titulo = params.get('titulo')
        detalhes = params.get('detalhes')

        # Criar uma nova nota usando a classe Database
        new_note = Note(title=titulo, content=detalhes)
        db = Database("banco")
        db.add(new_note)
        db.close_connection()

        return build_response(code=303, reason='See Other', headers='Location: /')


