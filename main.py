import os, asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.getenv("8157069080:AAEzqkoT6UDH_5WElDLI-VEtF_ybpjqZ4cQ")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌎 Imperio", callback_data='menu_feds'),
         InlineKeyboardButton("🛡️ Seguridad", callback_data='menu_sec')],
        [InlineKeyboardButton("🎨 Creativo (/q)", callback_data='menu_tools'),
         InlineKeyboardButton("📊 Estadísticas", callback_data='menu_stats')]
    ]
    text = (
        "🎩 Sr Crew Bot Edición Pro\n\n"
        "✅ Online 24/7 en la nube"
    )

    if update.message:
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.callback_query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def quotly(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        await update.message.reply_text("❌ Responde a un mensaje")
        return
    await update.message.reply_text("🎨 Generando sticker...")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("q", quotly))
    app.add_handler(CallbackQueryHandler(start))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
