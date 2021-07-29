from telethon import TelegramClient, events, sync
import re
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 790914
api_hash = '35163124bc01cdfe9a9cf846d662d82e'

client = TelegramClient('test', api_id, api_hash)


@client.on(events.NewMessage(func=lambda e: e.is_private))
async def handler(event):
    print(event.chat_id)






client.start()
s = client.get_entity(1027587059)
messages =  client.get_messages(s, limit = 10000 )
print(len(messages))
client.run_until_disconnected()