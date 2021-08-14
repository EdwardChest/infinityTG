from telethon import TelegramClient, events, functions
import argparse

# ARGUMENTS
parser = argparse.ArgumentParser(description='Infinity online for Telegram')
parser.add_argument('--appID', type=str,
                    help='App api_id from your application')
parser.add_argument('--appHASH', type=str,
                    help='App api_hash from your application')

args = parser.parse_args()

# CLIENT
client = TelegramClient('infinity', args.appID, args.appHASH)


@client.on(events.UserUpdate)
async def handler(event):
    if event.online or event.last_seen or event.recently:
        await client(functions.account.UpdateStatusRequest(
            offline=False
        ))

client.start()
print('[INFINITY] Running')
client.run_until_disconnected()
