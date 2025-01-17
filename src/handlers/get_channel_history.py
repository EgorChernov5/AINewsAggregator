from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def save_posts_from_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Сохраняет все посты из канала за текущий день в файл."""
    try:
        # Получаем текущую дату
        today = datetime.now().date()
        start_of_day = datetime(today.year, today.month, today.day)
        end_of_day = start_of_day + timedelta(days=1)

        # Получаем посты из канала
        posts = []
        async for message in context.bot.get_chat_history(chat_id=CHANNEL_USERNAME):
            # Проверяем, что пост был опубликован сегодня
            if start_of_day <= message.date <= end_of_day:
                post_data = {
                    "text": message.text,
                    "date": message.date.isoformat(),
                    "message_id": message.message_id,
                }
                posts.append(post_data)
            else:
                # Посты отсортированы по дате, поэтому можно прервать цикл, если дата выходит за пределы дня
                break

        # Сохраняем посты в файл
        with open("posts.json", "w", encoding="utf-8") as file:
            json.dump(posts, file, ensure_ascii=False, indent=4)

        await update.message.reply_text(f"Сохранено {len(posts)} постов за сегодня в файл posts.json.")
    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {e}")
