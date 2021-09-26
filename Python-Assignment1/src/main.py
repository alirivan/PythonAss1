from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
qian = cg.get_coins_markets(vs_currency='usd')


shu = int(input())

def output(x):
    list = []
    for _ in range(x):
        list.append((int(qian[_]['market_cap']), qian[_]['name']))

    for i in range(x):
        print(list[i][1], list[i][0])

output(shu)