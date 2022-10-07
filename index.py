# -*- coding: utf8 -*-
import requests
import json
imprt os
WEBHOOK = os.environ.get('WECHATWORK_WEBHOOK')

request_params = {
    "headers": {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    },
    "timeout": 10
}


def get_today_bonds():
    r = requests.get("http://data.hexin.cn/ipo/bond/cate/info/",
                     **request_params)

    today_bonds = []
    for bond in r.json():
        # print(f"{bond['zqName']}: 申购日期:{bond['sgDate']}")
        if bond['today'] == bond['sgDate']:
            today_bonds.append(bond)

    return today_bonds


def get_message():
    bonds = get_today_bonds()
    if len(bonds) > 0:
        description = f"今日有{len(bonds)}条鱼"

    message = {
        "msgtype": "news",
        "news": {
            "articles": [{
                "title":
                description,
                "description":
                ".",
                "url":
                "www.qq.com",
                "picurl":
                "https://i.loli.net/2020/11/18/3zogEraBFtOm5nI.jpg"
            }]
        }
    }

    return message


def send_message():
    headers = {"Content-Type": "text/plain"}
    send_url = WEBHOOK
    bonds = get_today_bonds()
    if len(bonds) > 0:
        send_data = get_message()
        res = requests.post(url=send_url, headers=headers, json=send_data)
        print(res.text)


def main_handler():
    send_message()

main_handler()
