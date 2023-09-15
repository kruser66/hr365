from typing import Annotated
import httpx
from fastapi import FastAPI, Query, Request
from pydantic import PositiveInt


app = FastAPI(title='Конвертер валют')


async def exchangerate(currency_from: str, currency_to: str, value: int = 1):
    '''Конвертирование валют, подробности - https://exchangerate.host/#/docs'''
    params = {
        'from': currency_from,
        'to': currency_to,
        'amount': value,
        'places': 2  # округление до двух знаков
    }
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.exchangerate.host/convert', params=params)

    return response.json()


async def support_symbols():
    '''Доступные валютные символы, подробности - https://exchangerate.host/#/docs'''
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.exchangerate.host/symbols')

    return response.json()['symbols']


@app.get('/api/symbols')
async def fetch_supported_symbols():
    return await support_symbols()


@app.get('/api/rates')
async def convert_currency(
        request: Request,
        currency_from: Annotated[str, Query(alias='from')] = "USD",
        currency_to: Annotated[str, Query(alias='to')] = "RUB",
        value: PositiveInt = 1,
        ):
    pass

    response = await exchangerate(
        currency_from=currency_from,
        currency_to=currency_to,
        value=value
    )
    conversion_result = response['result']

    return {'result': conversion_result} if conversion_result else {
                'error': 'Conversion is failed. Check supported symbols',
                'url': request.url_for("fetch_supported_symbols")
            }
