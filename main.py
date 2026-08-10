from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = "8640329086:AAHq0Zf2wVGID6ARP8TJkSJP4kE9j8sx93w"

async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    req = update.chat_join_request
    await req.approve()
    print(f"Approved {req.from_user.id}")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(ChatJoinRequestHandler(approve_request))

print("Bot running...")
app.run_polling()
