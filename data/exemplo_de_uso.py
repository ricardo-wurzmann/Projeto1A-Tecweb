from database import Database, Note

db = Database('banco')

db.add(Note(title='Receita de miojos', content='Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque em uma vasilha e aproveite seu snack :)'))

notes = db.get_all()
for note in notes:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')