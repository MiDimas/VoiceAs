import pyttsx3
import speech_recognition as sr
import datetime
import pyautogui as pg

engine = pyttsx3.init()


def sayToMe(talk):
    engine.say(talk)
    engine.runAndWait()


sayToMe("Начинаю работу")
record = sr.Recognizer()

x = 0
script_end = "Жду следующей комманды"

while x == 0:
    try:
        with sr.Microphone(device_index=1) as source:
            print("Говори, приятель")
            audio = record.listen(source)

            result = record.recognize_google(audio, language="ru")
            result = result.lower()
            print(result)

            if result == "привет":
                sayToMe("здравствуйте")

            elif result == "скажи время":
                now = datetime.datetime.now()
                str_date = "Сейчас {}:{}".format(str(now.hour), str(now.minute))
                print(str_date)
                sayToMe(str_date)
                sayToMe(script_end)

            elif result == "выход" or result == "пока":
                print("Завершение работы")
                sayToMe("До свидания")
                x = 1

            elif result == "определи координаты":
                sayToMe("вычисляю координаты курсора")
                print(pg.position())
                sayToMe(script_end)

            elif result == "запусти chrome":
                sayToMe("Запускаю хром если он установлен")
                pg.hotkey("winleft")
                pg.typewrite("chrome\n", 0.5)
                pg.hotkey("ctrl", "t")
                pg.typewrite("https://github.com/MiDimas\n", 0.1)
                pg.hotkey("winleft", "up")
                sayToMe("это страница разработчика")

            elif result == "спасибо":
                sayToMe("Пожалуйста, жду следующей команды")

            elif result == "как ты" or result == "как дела":
                sayToMe("Всё хорошо, спасибо, теперь перейдем к делу")

            elif result == "как тебя выключить":
                sayToMe("Скажите пока или выход")
                sayToMe(script_end)

            else:
                print("Неверная команда")
                sayToMe("Попробуй другую команду")

    except sr.UnknownValueError:
        sayToMe("Не поняла")
        print("Голос не распознан")

    except sr.RequestError:
        sayToMe("Поломка")
        print("Что то сломалось")

    except pg.FailSafeException:
        sayToMe("убери руки от клавиатуры и мыши")
        print("ошибка ввода")
