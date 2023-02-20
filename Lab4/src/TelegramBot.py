import telepot
import time

bot = telepot.Bot('6084477926:AAEZevNrxh4TnXVsVrf-wwoZ5_ahN1fhfKE')
chat_id = 1248386917


def handle_command(msg):
    command = msg['text']
    chat_id = msg['chat']['id']
    if command == 'Open':
        print("Open")
    elif command == 'Close':
        print("Close")
    elif command == 'Battery':
        print("Battery Level")
    elif command == "Check Fuel Level":
        print("Fuel Level")
    elif command == "Temp":
        print("Fuel Level")
    elif command == "Start Engine":
        print("Engine Start")
    elif command == "Off Engine":
        print("Engine OFF")
    else:
        bot.sendMessage(chat_id, 'invalid command')


def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        handle_command(msg)


bot.message_loop(handle_message)
while True:
    time.sleep(10)