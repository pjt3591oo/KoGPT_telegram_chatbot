from telegram.ext import Updater, MessageHandler, Filters 
import ko_gen as kg
from config import TELEGRAM_TOKEN

print('start telegram chat bot')

def get_message(bot, update) :
  print('입력받은 문장: %s'%(update.message.text))
  g_m = kg.make_str(update.message.text)
  print('생성된 문장: %s'%(g_m))
  update.message.reply_text(g_m)
    
updater = Updater(TELEGRAM_TOKEN)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()