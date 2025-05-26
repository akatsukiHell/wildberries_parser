from typing import Optional
import requests

article = input(str("Введите артикул: "))

def get_wb_info(article: str) -> Optional[dict]:
    url = f"https://card.wb.ru/cards/detail?&dest=-1257786&nm={article}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    else:
        data = response.json()['data']['products']
        if data:
            return {data[0]['name']: data[0]['priceU'] // 100}
        else:
            return None



if __name__ == "__main__":
    print(get_wb_info(article))