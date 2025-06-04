
import telebot
from telebot import types
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "your-bot-token")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME", "@unlock254")
MPESA_NUMBER = os.getenv("MPESA_NUMBER", "+254792770877")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Yo! 👋 Welcome to dollarsign — your plug for premium unlock tools. Try /price /buy /howto")

@bot.message_handler(commands=['price'])
def send_price(message):
    text = "🔓 Unlock Tools:\n- TFT Premium Unlock: 500 KES\n- Auto-updater Add-on: 250 KES\n🚀 Trusted by gamers across 254!"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['buy'])
def send_buy(message):
    msg = f"💸 To buy:\nM-Pesa: {MPESA_NUMBER}\nSend payment then DM this bot with a screenshot 📥"
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['howto'])
def send_howto(message):
    bot.send_message(message.chat.id, "📘 How to Use:\n1. Pay\n2. Receive the tool\n3. Run it\n4. Enjoy all unlocks\nDM @unlock254 for support.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    txt = message.text.lower()
    if "safe" in txt or "legit" in txt:
        bot.reply_to(message, "✅ 100% safe. Tested and working. No bans, no cap.")
    elif "how" in txt and "work" in txt:
        bot.reply_to(message, "🧠 We use a stealth tool that bypasses premium locks. Easy to run, safe to use.")
    elif "proof" in txt:
        bot.send_message(message.chat.id, "📸 Posting proof soon... stay tuned!")

bot.polling()
