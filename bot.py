from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "6718717995:AAFEDQBjiLTKqR6fE6go9jALtRyEaSg6ecc"  # Replace with your bot token

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.web_app_data.data
    await update.message.reply_text(f"✅ Your order has been received:\n{data}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))

print("🤖 Bot is running...")
app.run_polling()
