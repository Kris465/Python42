class Note:
    notes = {"Первая заметка":
             "Это текст заметки. Здесь вы можете создавать новые заметки, читать их и удалять не нужные (для этого используйте 'создать' 'прочитать' и 'удалить')"}

    def create_note(notes):
        name = input("Введите название вашей заметки: ")
        text = ''

        notes[name] = text

    def read_note(notes, name):
        text = notes[name]
        print(name)
        print(text)

    def update_note(notes, choice, name):
        if choice.lower() == 'перезаписать':
            text = input('Введите новый текст заметки:\n')
            notes[name] = text
        if choice.lower() == 'редактировать':
            pass
