# Ts-Bots


import os
import pytz
import time
import datetime

from pyrogram import Client

user_session_string = os.environ.get("user_session_string")
bots = [i.strip() for i in os.environ.get("bots").split(' ')]
update_channel = os.environ.get("update_channel")
status_message_ids = [int(i.strip()) for i in os.environ.get("status_message_id").split(' ')]
api_id = int(os.environ.get("api_id"))
api_hash = os.environ.get("api_hash")
user_client = Client(session_name=str(user_session_string), api_id=api_id, api_hash=api_hash)


def main():
    with user_client:
        while True:
            print("[INFO] starting to check uptime..")
            edit_text = f"🤖 𝙋𝙔𝙍𝙊𝙂𝙍𝘼𝙈𝙈𝙀𝙍𝙎 𝘽𝙤𝙩 𝙎𝙩𝙖𝙩𝙪𝙨 🤖\n\n__( 𝐴𝑙𝑙 𝑏𝑜𝑡𝑠 𝑠𝑡𝑎𝑡𝑢𝑠 𝑎𝑟𝑒 𝑐ℎ𝑒𝑐𝑘𝑒𝑑 𝑎𝑢𝑡𝑜𝑚𝑎𝑡𝑖𝑐𝑎𝑙𝑙𝑦 𝑒𝑣𝑒𝑟𝑦 𝑓𝑜𝑢𝑟 ℎ𝑜𝑢𝑟𝑠. 𝐼𝑓 𝑎𝑛𝑦 𝑖𝑠𝑠𝑢𝑒 𝑝𝑙𝑒𝑎𝑠𝑒 𝑟𝑒𝑝𝑜𝑟𝑡 𝑖𝑡. )__\n\n\n"
            for bot in bots:
                print(f"[INFO] checking @{bot}")
                snt = user_client.send_message(bot, '/start')

                time.sleep(15)

                msg = user_client.get_history(bot, 1)[0]
                if snt.message_id == msg.message_id:
                    print(f"[WARNING] @{bot} is down")
                    edit_text += f"𝗕𝗼𝘁 𝗡𝗮𝗺𝗲    {bot} \n𝗨𝘀𝗲𝗿𝗡𝗮𝗺𝗲  @{bot}\n𝗦𝘁𝗮𝘁𝘂𝘀      ❌\n\n"
                    #user_client.send_message("me",
                                             #f"@{bot} was down")
                else:
                    print(f"[INFO] all good with @{bot}")
                    edit_text += f"𝗕𝗼𝘁 𝗡𝗮𝗺𝗲    {bot} \n𝗨𝘀𝗲𝗿𝗡𝗮𝗺𝗲  @{bot}\n𝗦𝘁𝗮𝘁𝘂𝘀      ✅\n\n"
                user_client.read_history(bot)

            time_now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            formatted_time = time_now.strftime("%d %B %Y %I:%M %p")

            edit_text += f"**Updated on {formatted_time} (IST)**"

            for status_message_id in status_message_ids:
                user_client.edit_message_text(int(update_channel), status_message_id,
                                         edit_text)
                time.sleep(5)
            print(f"[INFO] everything done! sleeping for 3 hours...")

            time.sleep(864000)


if __name__ == "__main__":
   main()
