import random

# список вопросов и ответов
questions = [
    {
        "question": "Как называется знаменитый ученый, автор теории относительности?",
        "answers": ["Исаак Ньютон", "Альберт Эйнштейн", "Никола Тесла", "Чарльз Дарвин"],
        "correct_answer": "Альберт Эйнштейн"
    },
    {
        "question": "Как называется столица России?",
        "answers": ["Санкт-Петербург", "Екатеринбург", "Москва", "Новосибирск"],
        "correct_answer": "Москва"
    },
    {
        "question": "Как называется знаменитый город-государство в Италии?",
        "answers": ["Рим", "Венеция", "Милан", "Сан-Марино"],
        "correct_answer": "Сан-Марино"
    },
    {
        "question": "Какой летательный аппарат был первым, который поднялся"
                    " в воздух при помощи собственных движущихся элементов?",
        "answers": ["Самолет", "Аэростат", "Вертолет", "Дирижабль"],
        "correct_answer": "Самолет"
    },
    {
        "question": "В каком году произошла Октябрьская революция в России?",
        "answers": ["1919", "1917", "1923", "1915"],
        "correct_answer": "1917"
    },
    {
        "question": "Как называется самое большое озеро в мире?",
        "answers": ["Онежское", "Виктория", "Байкал", "Мичиган"],
        "correct_answer": "Байкал"
    },
    {
        "question": "Какая планета находится четвертой от Солнца?",
        "answers": ["Марс", "Юпитер", "Венера", "Меркурий"],
        "correct_answer": "Марс"
    },
    {
        "question": "Как называется знаменитый часовой башенный механизм в Лондоне?",
        "answers": ["Биг-Бен", "Эффельова башня", "Токийский башмак", "Галилеев башня"],
        "correct_answer": "Биг-Бен"
    },
    {
        "question": "Как называется главный герой романа \"Мастер и Маргарита\" Михаила Булгакова?",
        "answers": ["Мю-Мю", "Эдип", "Иван-дурак", "Воланд"],
        "correct_answer": "Воланд"
    },
    {
        "question": "Как называется головной убор национального костюма шотландцев?",
        "answers": ["Кепи", "Фуражка", "Берет", "Кильт"],
        "correct_answer": "Кильт"
    }
]

# определяем функцию для задавания вопросов
def ask_question(question):
    print(question["question"])
    random.shuffle(question["answers"])
    for i in range(len(question["answers"])):
        print(f"{i+1}. {question['answers'][i]}")
    answer = input("Введите номер правильного ответа: ")
    if answer == "50":
      print(f"Помощь зала оставила вам выбор из вариантов: {question['correct_answer']}"
            f" и {random.choice([i for i in question['answers'] if i!=question['correct_answer']])}")
      answer = input("Введите номер правильного ответа: ")
    return answer == str(question["answers"].index(question["correct_answer"]) + 1)

# определяем функцию для игры
def play_game():
    money = 0
    for i in range(len(questions)):
        if ask_question(questions[i]):
            money += 100000
            print("Правильно!", money)
        else:
            print("Неправильно!")
            break
    print(f"Вы выиграли {money} рублей!")

play_game()