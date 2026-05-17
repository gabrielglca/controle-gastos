import requests


def buscar_cotacao():
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"
        response = requests.get(url, timeout=5)
        data = response.json()
        dolar = float(data["USDBRL"]["bid"])
        euro = float(data["EURBRL"]["bid"])
        return {"dolar": dolar, "euro": euro}
    except Exception:
        return {"dolar": None, "euro": None}