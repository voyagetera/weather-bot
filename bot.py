from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "ĮČIA_ĮKELK_SAVO_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Vėjo botas veikia 🌬")

async def wind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💨 Vėjas: 12 m/s SW (testas)")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("wind", wind))

app.run_polling()
