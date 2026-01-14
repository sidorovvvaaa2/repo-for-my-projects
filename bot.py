import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен вашего бота (ЗАМЕНИТЕ на свой!)
TOKEN = "8562799907:AAHnPD5uEFlXzWnBjeBay7yINn9q8upL8jk"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}! 👋\n"
        f"Я простой бот. Вот что я умею:\n"
        f"/start - приветствие\n"
        f"/help - помощь\n"
        f"/echo текст - повторю текст\n"
        f"/calc 2+2 - простой калькулятор\n"
        f"Просто отправь мне сообщение, и я его повторю!"
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🤖 *Доступные команды:*

/start - Начать работу с ботом
/help - Показать это сообщение
/echo [текст] - Повторить текст
/calc [выражение] - Калькулятор (например: /calc 2+2*3)

📝 *Просто отправьте:*
- Текст - я его повторю
- Картинку - я её сохраню
- Стикер - отправлю обратно

🛠 *Примеры:*
/echo Привет мир!
/calc (10+5)*2
"""
    await update.message.reply_text(help_text, parse_mode='Markdown')

# Команда /echo
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        text = ' '.join(context.args)
        await update.message.reply_text(f"Вы сказали: {text}")
    else:
        await update.message.reply_text("Напишите: /echo ваш текст")

# Команда /calc - простой калькулятор
async def calculator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Используйте: /calc 2+2 или /calc (10+5)*2")
        return
    
    try:
        expression = ' '.join(context.args)
        # Безопасное вычисление
        allowed_chars = set('0123456789+-*/(). ')
        if not all(c in allowed_chars for c in expression):
            raise ValueError("Разрешены только числа и +-*/()")
        
        # Вычисление
        result = eval(expression)
        await update.message.reply_text(f"🔢 {expression} = {result}")
    except Exception as e:
        await update.message.reply_text(f"❌ Ошибка: {str(e)}")

# Обработка текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.effective_user
    
    if text.lower() in ['привет', 'hello', 'hi']:
        await update.message.reply_text(f"Привет, {user.first_name}! 👋")
    elif text.lower() in ['как дела?', 'how are you?']:
        await update.message.reply_text("У меня всё отлично! А у вас? 😊")
    else:
        await update.message.reply_text(f"Вы написали: {text}")

# Обработка стикеров
async def handle_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sticker = update.message.sticker
    await update.message.reply_sticker(sticker.file_id)

# Обработка фото
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]  # Берем самую большую версию фото
    await update.message.reply_text("📸 Классное фото! Я его получил.")

# Обработка ошибок
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Ошибка: {context.error}")

def main():
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()
    
    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("echo", echo))
    application.add_handler(CommandHandler("calc", calculator))
    
    # Добавляем обработчики сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.Sticker.ALL, handle_sticker))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    # Обработчик ошибок
    application.add_error_handler(error_handler)
    
    # Запускаем бота
    print("🤖 Бот запущен! Нажмите Ctrl+C для остановки.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
