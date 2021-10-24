import telebot
import requests
import json
import time



url = "https://api.wazirx.com/api/v2/tickers"

source  = requests.get(url)

data1 = (source.json())


ltcinrbuy = float(data1['ltcinr']['buy'])
wrxinrbuy = float(data1['wrxinr']['buy'])
shibinrbuy = float(data1['shibinr']['buy'])	

print(shibinrbuy)
bot = telebot.TeleBot("2066017477:AAFSOhyH3k7EUpxXcakrleeqbD_qMVENj4Y",parse_mode='MARKDOWN')
def profit(buyprice,currentbuy):
	calc = (currentbuy - buyprice)
	calc = calc/buyprice * 100
	return calc
m = json.load(open('data.json'))

origwrx = float(m['origwrx']) #our_buy_price
origshib = float(m['origshib'])#our_buy_price
origltc = float(m['origltc'])#our_buy_price
shib = float("{:.2f}".format(profit(origshib,shibinrbuy)))
print(shib)
ltc = float("{:.2f}".format(profit(origltc,ltcinrbuy)))
print(ltc)
wrx = float("{:.2f}".format(profit(origwrx,wrxinrbuy)))
print(wrx)
#iotx = float("{:.2f}".format(profit(oriiotx,iotxinrbuy)))
#print(floatf)

def shibcheck():
	if shib<=-3 or shib>=3:
		global tempbtt
		#tempbtt+=btt
		hi = f'```💹Time to Trade Shib={shib}%‼️```'
		return hi

def wrxcheck():
	if wrx<=-3 or wrx>=3:
		global tempwrx
		#tempwrx+=wrx
		return f'```💹Time to Trade WRX={wrx}%‼️```'
def litcheck():
	if ltc<=-3 or ltc>=3:
		global templit
		#tempwrx+=wrx
		return f'```💹Time to Trade LTC={ltc}%‼️```'

print(shibcheck())
print(wrxcheck())
print(litcheck())
final = str(shibcheck()).replace(" ", "")+'\n'+str(wrxcheck()).replace(" ", "")+'\n'+str(litcheck()).replace(" ", "")
print(final)
final = final.replace('None', '')
#price = f'WRX={s}'
try:
	bot.send_message("1031221294","{}".format(final))
except:
	print('dull market')
