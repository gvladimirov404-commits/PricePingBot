from telegram.ext import Updater, CommandHandler
from config import TOKEN
import requests

def start(update, context):
    update.message.reply_text("🚀 PricePingBot ready!\nUse /set bitcoin 70000")

def set_alert(update, context):
    try:
        coin = context.args[0].lower()
        price = float(context.args[1])

        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        data = requests.get(url).json()

        current = data[coin]["usd"]

        update.message.reply_text(
            f"{coin.upper()} current price: {current} USD\nAlert set at {price}"
        )

    except:
        update.message.reply_text("Usage: /set bitcoin 70000")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("set", set_alert))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
