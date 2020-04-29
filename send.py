import telegram 
import ko_gen as kg
from config import TELEGRAM_TOKEN

def send(chat_id, t):
  bot.sendMessage(chat_id, t)

bot = telegram.Bot(token=TELEGRAM_TOKEN)

updates = bot.getUpdates()

for u in updates :   # 내역중 메세지를 출력합니다.
  msg = u.message
  print('메시지 발생 채팅방 아이디: %s, 수신 메시지: %s'%(msg.chat.id, msg.text))
  generator_msg = kg.make_str(msg.text)
  print('생성된 메시지: %s'%(generator_msg))
  send(msg.chat.id, generator_msg)