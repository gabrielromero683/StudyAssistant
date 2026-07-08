import random


motivational_quotes = [
    "Nunca dejes de aprender.",
    "Cada día es una oportunidad para mejorar.",
    "El esfuerzo de hoy será el éxito de mañana.",
    "Los pequeños pasos también cuentan."
]


def show_menu():
    print("\n===== Study Assistant =====")
    print("1. Agregar una nota")
    print("2. Ver notas")
    print("3. Frase motivadora")
    print("4. Salir")


def add_note():
    note = input("Escribe tu nota: ")

    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(note + "\n")

    print("✅ Nota guardada correctamente.")


def show_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.readlines()

        if not notes:
            print("No hay notas guardadas.")
            return

        print("\nTus notas:")

        for note in notes:
            print("-", note.strip())

    except FileNotFoundError:
        print("Todavía no has guardado ninguna nota.")


def show_quote():
    print("\n💡", random.choice(motivational_quotes))


while True:
    show_menu()

    option = input("Selecciona una opción: ")

    if option == "1":
        add_note()

    elif option == "2":
        show_notes()

    elif option == "3":
        show_quote()

    elif option == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Esa opción no existe.")