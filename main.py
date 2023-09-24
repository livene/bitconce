import time
import requests

headers = {
    'Authorization': 'Bearer '
}

url = "https://bitconce.top/api/getExchangeOrders/"
response = requests.get(url, headers=headers)
print(response.json())
min_r = int(input("Min rub: "))
max_r = int(input("Max rub: "))
while True:
    response = requests.get(url, headers=headers)
    if response.json()["status"] == "success":

        bank_name = response.json()['orders'][-1]["direction"][23:]
        rubles_order = int(response.json()['orders'][-1]["rub_amount"]) # -1 потому что новые ордера, нужные нам сбер, тиньк
        # появляются в конце списка и проходить весь массив неэффективно
        if (len(response.json()["orders"]) > 0) and (bank_name == "Tinkoff RUB") and (min_r <= rubles_order <= max_r):
            url_post = "https://bitconce.top/api/setUserExchageOrder/"
            payload = {"exchange_id": str(response.json()['orders'][-1]["exchange_id"])}
            response = requests.post(url_post, headers=headers, data=payload)
            print(response.json()[response])
    time.sleep(60 / 150)
