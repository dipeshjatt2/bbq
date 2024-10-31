import base64
import time 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests 

def encode_event(e, t):
    r = f"{e}|{t}|{int(time.time())}"
    n = "tttttttttttttttttttttttttttttttt"
    i = n[:16]
    key = n.encode('utf-8') 
    iv = i.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(r.encode('utf-8'), AES.block_size))
    return base64.b64encode(base64.b64encode(encrypted)).decode('utf-8')

# replace your query id in the headers 
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'access-control-allow-origin': '*',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'lan': 'en',
    'origin': 'https://bbqapp.bbqcoin.ai',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://bbqapp.bbqcoin.ai/',
    'sec-ch-ua': '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'use-agen': 'query_id=AAEA7AAAAAAA_YXvLvmCa&user=%7B%22id%22%%2C%22first_name%22%3A%22%E3%85%A4%22%2C%22last_name%22%3A%22%E2%81%AA%E2%81%AC%22%2C%22username%22%3A%%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1730304409&hash=b5b7e6f18438a8dfd1ee61e50e80871638d137f091frj439frj775d07664e7b4f6',
    'user-agent': 'add your custom header here ',
    'x-requested-with': 'org.telegram.messenger',
}

user_id = '5203820046'#telegram user ID
taps = '3000000' #amount of taps
def bbq_tap():
    data = {
        'id_user':user_id,
        'mm': taps ,
        'game': encode_event(user_id,taps),
    }
    response = requests.post('https://bbqbackcs.bbqcoin.ai/api/coin/earnmoney', headers=headers, data=data)
    print(response.json())
bbq_tap()
