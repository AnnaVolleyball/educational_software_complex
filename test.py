import datetime

start = datetime.datetime.now()
end = start + datetime.timedelta(minutes=10)
r = 0


def makeQuiz(rightAnswer):
    global r
    if (end - datetime.datetime.now()).total_seconds() > 0:
        while True:
            answer = input()
            if answer == 'время':
                if (end - datetime.datetime.now()).total_seconds() > 0:
                    print(end - datetime.datetime.now())
                else:
                    print('Время вышло!')
            elif answer.lower() == rightAnswer:
                print('Верно!')
                r += 1
                break
            else:
                print('Увы, нет.')
                break


print("Сколько лет дедушке?\nА - 27\tБ - 54")
makeQuiz('б')
print("Какая фамилия у Ленина?\nА - Ленин\tБ - Ульянов")
makeQuiz('б')
if (end - datetime.datetime.now()).total_seconds() < 0:
    print(f'Время вышло!\nОчков набрано: {r}')
else:
    print(f'Всё!\nЕщё {(end - datetime.datetime.now())} секунд в запасе.\nОчков набрано: {r}')
