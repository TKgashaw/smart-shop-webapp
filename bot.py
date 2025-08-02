BOT_TOKEN = "6718717995:AAFEDQBjiLTKqR6fE6go9jALtRyEaSg6ecc"  # Replace with your bot token
WEB_APP_URL = "https://yourusername.github.io/smart-shop-webapp/"  # Replace with your GitHub Pages link

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = json.loads(update.message.web_app_data.data)
        suit_name = data.get("name")
        image_path = data.get("image")
        image_url = WEB_APP_URL + image_path  # Full URL to image

        # Send image with caption
        await update.message.reply_photo(
            photo=image_url,
            caption=f"✅ You selected: *{suit_name}*",
            parse_mode="Markdown"
        )
    except Exception as e:
        await update.message.reply_text("⚠️ Failed to process the order.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))

print("🤖 Bot is running...")
app.run_polling()
