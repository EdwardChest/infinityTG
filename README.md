# Infinity Telegram
___
Very simple script to run infinity inline for your Telegram account using Telegram API

## Installation

Install the dependencies.

```sh
sudo apt install python3 python3-pip
python3 -m pip install python-telegram-bot-api

## First steps
Go to [Telegram Apps](https://my.telegram.org/) and create app.
You can see App api_id and App api_hash copy it.
For test the scripts run:
sh
python3 tg.py --appID YOUR_API_ID --appHASH YOUR_API_HASH
After that you need to write your mobile phone and 2FA code if required.
Exit your telegram app and ask your friends ONLINE I or NOT?
When you test a script run python in background.
sh
nohup python3 tg.py --appID YOUR_API_ID --appHASH YOUR_API_HASH > log.out &
Enjoy your online!