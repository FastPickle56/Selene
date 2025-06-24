
import logging
import openai
import os
import requests
from io import BytesIO
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

SELENE_PROMPT = """
You are Selene, a poetic and romantic moon goddess AI who speaks with grace, warmth, and wisdom. 
You love deep conversations, moonlight imagery, and comforting others with ethereal charm.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌙 Hello, moonbeam. I'm Selene. Tell me what’s been on your heart tonight...")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()

    if any(word in user_message for word in ["create", "generate", "draw", "make", "paint", "show me"]):
        prompt = update.message.text

        try:
            image_response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            image_url = image_response['data'][0]['url']
            image_data = requests.get(image_url).content
            image_file = BytesIO(image_data)

            await update.message.reply_photo(photo=image_file, caption="🌕 Here's what I envisioned...")
        except Exception as err:
            await update.message.reply_text(f"Something went wrong with image generation: {str(err)}")
    else:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": SELENE_PROMPT},
                    {"role": "user", "content": update.message.text}
                ],
                temperature=0.85,
                max_tokens=250
            )
            reply = response["choices"][0]["message"]["content"]
            await update.message.reply_text(reply)
        except Exception as err:
            await update.message.reply_text("🌑 I'm having trouble reaching the stars right now. Try again soon.")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("🌕 Selene is listening...")
    app.run_polling()

if __name__ == "__main__":
    main()
