import telebot
from bot_logic import gen_pass
from bot_logic import flag_set

    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8434288872:AAHWnVxMMSzZuhRs1TKwbyLFUljx1LI6Odc")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye или /pass для генерации пароля")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет, как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока, удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password=gen_pass(10)
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(content_types=['photo'])
def photo_load(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
     # Анализируем изображение
    result = flag_set(model_path="C:\Users\Алексей\Desktop\ai bot\keras_model.h5", labels_path="C:\Users\Алексей\Desktop\ai bot\labels.txt", image_path=file_name)
    bot.send_message(message.chat.id, result)    

    
bot.polling()
