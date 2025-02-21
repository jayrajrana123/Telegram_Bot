from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace with your bot token
BOT_TOKEN = "8195586551:AAHoVFXlrmULnF42bGygWRUp5_bDH8QE-Fw"

# Replace with your ZIP file link
ZIP_FILE_LINK = "https://www.mediafire.com/file/ip6821qrbppktd1/PIETDS-CSE%25282nd_SEM%2529.zip/file"

# Replace with your UPI Payment Link
UPI_PAYMENT_LINK = "upi://pay?pa=8320708629@ptsbi&pn=JayrajsinhRana"

async def start(update: Update, context: CallbackContext) -> None:
    message = (
        "🎉 **Welcome!** 🎉\n\n"
        "📂 **Download your ZIP file here:**\n"
        f"[Click Here]({ZIP_FILE_LINK})\n\n"
        "💖 **If you like my service, help me expand by contributing!** 💖\n"
        f"🔗 **UPI Payment Link:** [Click to Pay]({UPI_PAYMENT_LINK})\n\n"
        "🙏 **Thank you for your support!** 🙌\n\n"
        "💡 *Bot Created By: Jayrajsinh Rana, ByteForce*"
    )
    
    await update.message.reply_text(message, parse_mode="Markdown", disable_web_page_preview=True)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
