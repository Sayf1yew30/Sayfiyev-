from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN ='AAEW4TKPkDQzBoK_OcVUFRPp22aICneDIVc'

# Stol bron qilish uchun menyu yaratish
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Stol bron qilish", callback_data='book_table')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Salom! Restoranimizga xush kelibsiz. Stol bron qilish uchun quyidagi tugmani bosing:', reply_markup=reply_markup)

# Stol bron qilish jarayoni
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    query.answer()
    
    if query.data == 'book_table':
        keyboard = [
            [InlineKeyboardButton("Bugun", callback_data='date_today')],
            [InlineKeyboardButton("Ertaga", callback_data='date_tomorrow')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Bron qilish sanasini tanlang:", reply_markup=reply_markup)
    
    elif query.data in ['date_today', 'date_tomorrow']:
        keyboard = [
            [InlineKeyboardButton("12:00", callback_data='time_12')],
            [InlineKeyboardButton("18:00", callback_data='time_18')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Bron qilish vaqtini tanlang:", reply_markup=reply_markup)
    
    elif query.data in ['time_12', 'time_18']:
        keyboard = [
            [InlineKeyboardButton("100,000 UZS", callback_data='price_100')],
            [InlineKeyboardButton("200,000 UZS", callback_data='price_200')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Bron qilish narxini tanlang:", reply_markup=reply_markup)
    
    elif query.data in ['price_100', 'price_200']:
        keyboard = [
            [InlineKeyboardButton("Naqd pul", callback_data='payment_cash')],
            [InlineKeyboardButton("Karta", callback_data='payment_card')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="To'lov usulini tanlang:", reply_markup=reply_markup)
    
    elif query.data in ['payment_cash', 'payment_card']:
        await query.edit_message_text(text="Stol bron qilindi! Rahmat.")

async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

