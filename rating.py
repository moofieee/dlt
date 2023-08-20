import json
import requests
import pandas as pd




def get_data():
    url = "https://api.tokeninsight.com/api/v1/rating/coins"

    headers = {
        "accept": "application/json",
        "TI_API_KEY": "1aef28bfa8d6476d83d41d8c10c01c4c"
    }
    param = {'limit': 1500}

    response = requests.get(url, headers=headers, params=param)
    text = response.text
    dict = json.loads(text)
    data = dict['data']['items']
    
    score = []
    level = []
    symbol = []
    name = []
        
    for item in data:
        score.append(item['rating_score'])
        level.append(item['rating_level'])
        symbol.append(item['symbol'])
        name.append(item['name'])
        
    dict_df = {'name':name, 'symbol':symbol, "score":score, "level":level}
    df = pd.DataFrame(dict_df)
    
    return df


if __name__=="__main__":
    
    df = get_data()