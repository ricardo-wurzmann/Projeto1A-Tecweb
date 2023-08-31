import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name + '.db')
        self.create_note_table()

    def create_note_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY,
                title TEXT,
                content TEXT NOT NULL
            );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add(self, note):
        query = "INSERT INTO note (title, content) VALUES (?, ?);"
        self.conn.execute(query, (note.title, note.content))
        self.conn.commit()

    def get_all(self):
        notes = []
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        for row in cursor:
            note = Note(id=row[0], title=row[1], content=row[2])
            notes.append(note)
        return notes

    def update(self, entry):
        query = "UPDATE note SET title = ?, content = ? WHERE id = ?;"
        self.conn.execute(query, (entry.title, entry.content, entry.id))
        self.conn.commit()

    def delete(self, note_id):
        query = "DELETE FROM note WHERE id = ?;"
        self.conn.execute(query, (note_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def get_by_id(self, note_id):
        query = "SELECT id, title, content FROM note WHERE id = ?;"
        cursor = self.conn.execute(query, (note_id,))
        row = cursor.fetchone()
        if row:
            note = Note(id=row[0], title=row[1], content=row[2])
            return note
        return None

# Exemplo de uso da classe Database
if __name__ == "__main__":
    db = Database("banco")  # Cria uma conexão com o banco de dados my_database.db

    new_note = Note(title="Título da Nota", content="Conteúdo da Nota")
    db.add(new_note)  # Insere a nota no banco de dados

    db.delete(1) 

    all_notes = db.get_all()  
    for note in all_notes:
        print(note.id, note.title, note.content)

    db.close_connection()  # Fecha a conexão com o banco de dados
