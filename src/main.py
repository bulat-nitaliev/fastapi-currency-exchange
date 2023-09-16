from fastapi import FastAPI, Query
import requests


app = FastAPI()


def request():
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        response = requests.get(url)
        data = response.json().get('rates')
        curr = [i for i in data]
        return curr,data

curr, data = request()


@app.get("/exchange_rate")
async def get_exchange_rate():

    return {"result":data}


@app.get('/api/rates')
async def rates(from_: str = Query("country", enum=curr),
                        to: str = Query("country", enum=curr),
                        value:int=1):
    from_cur = data[from_]
    to_curr = data[to]
    result = round((to_curr/from_cur)*value,2)

    return {"result":result}
    