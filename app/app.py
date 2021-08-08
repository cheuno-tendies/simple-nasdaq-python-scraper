from flask import Flask,render_template, Response
import socket
import requests
import json

app = Flask(__name__)
        

def _url(ticker):
        return  f"https://api.nasdaq.com/api/quote/{ticker}/option-chain"        

def fetch():
    print("Fetching from Nasdaq")
    # url = "https://api.nasdaq.com/api/quote/TSLA/option-chain?assetclass=stocks&limit=3&fromdate=2021-08-13&todate=2021-08-20&excode=oprac&callput=callput&money=all&type=all&action=finish"
    params = {
            "assetclass": "stocks",
            "limit": "1000",
            "fromdate": "2021-08-06",
            "todate": "2021-08-06",
            "excode": "oprac",
            "callput": "callput",
            "money": "all",
            "type": "all",
        }
    print("Fetching from Nasdaq...")
    
    headers = {
        'authority': 'api.nasdaq.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'accept': 'application/json, text/plain, */*',
        'dnt': '1',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'origin': 'https://www.nasdaq.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.nasdaq.com/',
        'accept-language': 'en-CA,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    }
    print("Fetching from Nasdaq...")
    r = requests.get(_url("TSLA"), params=params, headers=headers)
    try:
        return Response(json.dumps(r.json()), mimetype='application/json')
    except:
        return r.content

@app.route("/")
def index():
    try:
        # return render_template('index.html', hostname=host_name, ip=host_ip)
        return fetch()
    except Exception as e:
        return e

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
