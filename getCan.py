import json
import requests


def getCandlesBrute(url):
    response = requests.get(url)


    if response.status_code == 200:
        try:

            data = response.json()
            return data["data"]
        except ValueError:
            print("Erro ao converter resposta em JSON")
    else:
        print(f"Falha na requisição. Status code: {response.status_code}")
    
if __name__ == "__main__":
    link = 'https://api.binomo.com/candles/v1/Z-CRY%2FIDX/2024-09-08T18:00:00/5?locale=br'
    print(type(getCandlesBrute(link)))