import requests
import json
#import os
import math
import config
import sqlite3
#from openpyxl import Workbook


gtx1050ti=config.gtx1050ti
gtx1060_3=config.gtx1060_3
gtx1060_6=config.gtx1060_6
gtx1070=config.gtx1070
gtx1070ti=config.gtx1070ti
gtx1080=config.gtx1080
gtx1080ti=config.gtx1080ti

# GPU
c11=config.c11
nist5=config.nist5
skein=config.skein
neoscrypt=config.neoscrypt
tribus=config.tribus
lyra2z=config.lyra2z
lyra2v2=config.lyra2v2
xevan=config.xevan
x16r=config.x16r
x16s=config.x16s
phi1612=config.phi1612
x17=config.x17
blake2s=config.blake2s
timetravel10=config.timetravel10
equihash=config.equihash
skunkhash=config.skunkhash
keccak=config.keccak
phi2=config.phi2
aeriumx=config.aeriumx
hexon=config.hexon
bcd=config.bcd
x13=config.x13
sha256d=config.sha256d
lbk3=config.lbk3

c11=(c11['gtx1050ti']*int(gtx1050ti))+(c11['gtx1060_3']*int(gtx1060_3))+(c11['gtx1060_6']*int(gtx1060_6))+(c11['gtx1070']*int(gtx1070))+(c11['gtx1070ti']*int(gtx1070ti))+(c11['gtx1080']*int(gtx1080))+(c11['gtx1080ti']*int(gtx1080ti))
nist5=(nist5['gtx1050ti']*int(gtx1050ti))+(nist5['gtx1060_3']*int(gtx1060_3))+(nist5['gtx1060_6']*int(gtx1060_6))+(nist5['gtx1070']*int(gtx1070))+(nist5['gtx1070ti']*int(gtx1070ti))+(nist5['gtx1080']*int(gtx1080))+(nist5['gtx1080ti']*int(gtx1080ti))
skein=(skein['gtx1050ti']*int(gtx1050ti))+(skein['gtx1060_3']*int(gtx1060_3))+(skein['gtx1060_6']*int(gtx1060_6))+(skein['gtx1070']*int(gtx1070))+(skein['gtx1070ti']*int(gtx1070ti))+(skein['gtx1080']*int(gtx1080))+(skein['gtx1080ti']*int(gtx1080ti))
neoscrypt=(neoscrypt['gtx1050ti']*int(gtx1050ti))+(neoscrypt['gtx1060_3']*int(gtx1060_3))+(neoscrypt['gtx1060_6']*int(gtx1060_6))+(neoscrypt['gtx1070']*int(gtx1070))+(neoscrypt['gtx1070ti']*int(gtx1070ti))+(neoscrypt['gtx1080']*int(gtx1080))+(neoscrypt['gtx1080ti']*int(gtx1080ti))
tribus=(tribus['gtx1050ti']*int(gtx1050ti))+(tribus['gtx1060_3']*int(gtx1060_3))+(tribus['gtx1060_6']*int(gtx1060_6))+(tribus['gtx1070']*int(gtx1070))+(tribus['gtx1070ti']*int(gtx1070ti))+(tribus['gtx1080']*int(gtx1080))+(tribus['gtx1080ti']*int(gtx1080ti))
lyra2z=lyra2z=(lyra2z['gtx1050ti']*int(gtx1050ti))+(lyra2z['gtx1060_3']*int(gtx1060_3))+(lyra2z['gtx1060_6']*int(gtx1060_6))+(lyra2z['gtx1070']*int(gtx1070))+(lyra2z['gtx1070ti']*int(gtx1070ti))+(lyra2z['gtx1080']*int(gtx1080))+(lyra2z['gtx1080ti']*int(gtx1080ti))
lyra2v2=(lyra2v2['gtx1050ti']*int(gtx1050ti))+(lyra2v2['gtx1060_3']*int(gtx1060_3))+(lyra2v2['gtx1060_6']*int(gtx1060_6))+(lyra2v2['gtx1070']*int(gtx1070))+(lyra2v2['gtx1070ti']*int(gtx1070ti))+(lyra2v2['gtx1080']*int(gtx1080))+(lyra2v2['gtx1080ti']*int(gtx1080ti))
xevan=(xevan['gtx1050ti']*int(gtx1050ti))+(xevan['gtx1060_3']*int(gtx1060_3))+(xevan['gtx1060_6']*int(gtx1060_6))+(xevan['gtx1070']*int(gtx1070))+(xevan['gtx1070ti']*int(gtx1070ti))+(xevan['gtx1080']*int(gtx1080))+(xevan['gtx1080ti']*int(gtx1080ti))
x16r=(x16r['gtx1050ti']*int(gtx1050ti))+(x16r['gtx1060_3']*int(gtx1060_3))+(x16r['gtx1060_6']*int(gtx1060_6))+(x16r['gtx1070']*int(gtx1070))+(x16r['gtx1070ti']*int(gtx1070ti))+(x16r['gtx1080']*int(gtx1080))+(x16r['gtx1080ti']*int(gtx1080ti))
x16s=(x16s['gtx1050ti']*int(gtx1050ti))+(x16s['gtx1060_3']*int(gtx1060_3))+(x16s['gtx1060_6']*int(gtx1060_6))+(x16s['gtx1070']*int(gtx1070))+(x16s['gtx1070ti']*int(gtx1070ti))+(x16s['gtx1080']*int(gtx1080))+(x16s['gtx1080ti']*int(gtx1080ti))
phi1612=(phi1612['gtx1050ti']*int(gtx1050ti))+(phi1612['gtx1060_3']*int(gtx1060_3))+(phi1612['gtx1060_6']*int(gtx1060_6))+(phi1612['gtx1070']*int(gtx1070))+(phi1612['gtx1070ti']*int(gtx1070ti))+(phi1612['gtx1080']*int(gtx1080))+(phi1612['gtx1080ti']*int(gtx1080ti))
x17=(x17['gtx1050ti']*int(gtx1050ti))+(x17['gtx1060_3']*int(gtx1060_3))+(x17['gtx1060_6']*int(gtx1060_6))+(x17['gtx1070']*int(gtx1070))+(x17['gtx1070ti']*int(gtx1070ti))+(x17['gtx1080']*int(gtx1080))+(x17['gtx1080ti']*int(gtx1080ti))
blake2s=(blake2s['gtx1050ti']*int(gtx1050ti))+(blake2s['gtx1060_3']*int(gtx1060_3))+(blake2s['gtx1060_6']*int(gtx1060_6))+(blake2s['gtx1070']*int(gtx1070))+(blake2s['gtx1070ti']*int(gtx1070ti))+(blake2s['gtx1080']*int(gtx1080))+(blake2s['gtx1080ti']*int(gtx1080ti))
timetravel10=(timetravel10['gtx1050ti']*int(gtx1050ti))+(timetravel10['gtx1060_3']*int(gtx1060_3))+(timetravel10['gtx1060_6']*int(gtx1060_6))+(timetravel10['gtx1070']*int(gtx1070))+(timetravel10['gtx1070ti']*int(gtx1070ti))+(timetravel10['gtx1080']*int(gtx1080))+(timetravel10['gtx1080ti']*int(gtx1080ti))
equihash=(equihash['gtx1050ti']*int(gtx1050ti))+(equihash['gtx1060_3']*int(gtx1060_3))+(equihash['gtx1060_6']*int(gtx1060_6))+(equihash['gtx1070']*int(gtx1070))+(equihash['gtx1070ti']*int(gtx1070ti))+(equihash['gtx1080']*int(gtx1080))+(equihash['gtx1080ti']*int(gtx1080ti))
skunkhash=(skunkhash['gtx1050ti']*int(gtx1050ti))+(skunkhash['gtx1060_3']*int(gtx1060_3))+(skunkhash['gtx1060_6']*int(gtx1060_6))+(skunkhash['gtx1070']*int(gtx1070))+(skunkhash['gtx1070ti']*int(gtx1070ti))+(skunkhash['gtx1080']*int(gtx1080))+(skunkhash['gtx1080ti']*int(gtx1080ti))
keccak=(keccak['gtx1050ti']*int(gtx1050ti))+(keccak['gtx1060_3']*int(gtx1060_3))+(keccak['gtx1060_6']*int(gtx1060_6))+(keccak['gtx1070']*int(gtx1070))+(keccak['gtx1070ti']*int(gtx1070ti))+(keccak['gtx1080']*int(gtx1080))+(keccak['gtx1080ti']*int(gtx1080ti))
phi2=(phi2['gtx1050ti']*int(gtx1050ti))+(phi2['gtx1060_3']*int(gtx1060_3))+(phi2['gtx1060_6']*int(gtx1060_6))+(phi2['gtx1070']*int(gtx1070))+(phi2['gtx1070ti']*int(gtx1070ti))+(phi2['gtx1080']*int(gtx1080))+(phi2['gtx1080ti']*int(gtx1080ti))
aeriumx=(aeriumx['gtx1050ti']*int(gtx1050ti))+(aeriumx['gtx1060_3']*int(gtx1060_3))+(aeriumx['gtx1060_6']*int(gtx1060_6))+(aeriumx['gtx1070']*int(gtx1070))+(aeriumx['gtx1070ti']*int(gtx1070ti))+(aeriumx['gtx1080']*int(gtx1080))+(aeriumx['gtx1080ti']*int(gtx1080ti))
hexon=(hexon['gtx1050ti']*int(gtx1050ti))+(hexon['gtx1060_3']*int(gtx1060_3))+(hexon['gtx1060_6']*int(gtx1060_6))+(hexon['gtx1070']*int(gtx1070))+(hexon['gtx1070ti']*int(gtx1070ti))+(hexon['gtx1080']*int(gtx1080))+(hexon['gtx1080ti']*int(gtx1080ti))
bcd=(bcd['gtx1050ti']*int(gtx1050ti))+(bcd['gtx1060_3']*int(gtx1060_3))+(bcd['gtx1060_6']*int(gtx1060_6))+(bcd['gtx1070']*int(gtx1070))+(bcd['gtx1070ti']*int(gtx1070ti))+(bcd['gtx1080']*int(gtx1080))+(bcd['gtx1080ti']*int(gtx1080ti))
x13=(x13['gtx1050ti']*int(gtx1050ti))+(x13['gtx1060_3']*int(gtx1060_3))+(x13['gtx1060_6']*int(gtx1060_6))+(x13['gtx1070']*int(gtx1070))+(x13['gtx1070ti']*int(gtx1070ti))+(x13['gtx1080']*int(gtx1080))+(x13['gtx1080ti']*int(gtx1080ti))
sha256d=(sha256d['gtx1050ti']*int(gtx1050ti))+(sha256d['gtx1060_3']*int(gtx1060_3))+(sha256d['gtx1060_6']*int(gtx1060_6))+(sha256d['gtx1070']*int(gtx1070))+(sha256d['gtx1070ti']*int(gtx1070ti))+(sha256d['gtx1080']*int(gtx1080))+(sha256d['gtx1080ti']*int(gtx1080ti))
lbk3=(lbk3['gtx1050ti']*int(gtx1050ti))+(lbk3['gtx1060_3']*int(gtx1060_3))+(lbk3['gtx1060_6']*int(gtx1060_6))+(lbk3['gtx1070']*int(gtx1070))+(lbk3['gtx1070ti']*int(gtx1070ti))+(lbk3['gtx1080']*int(gtx1080))+(lbk3['gtx1080ti']*int(gtx1080ti))


conn = sqlite3.connect('database.db')
cur = conn.cursor()
tbl='coins'
# Create table
try:
	cur.execute('''CREATE TABLE tbl
        (
        name text,
        ticker text,
        algoritm text,
        exchange text,
        reward real,
        difficult real,
        coins_day real,
        price real,
        day real,
        week real,
        month real)''')
except:
	"Warning: Table already exist!!!"
cur.execute('delete from tbl')

# Export to excel function
def xls_exp():
	wb = Workbook()
	ws = wb.active
	ws.append(["PAIR", "Last price"])

	cnt=0
	for i in bitt:
		if i=='result':
			for h in bitt[i]:

				print(h["MarketName"],"\t",h["Last"])
				#ws.append(bitt[h])
				cnt=cnt+1
	#print("Total pairs: ",cnt)
	wb.save(os.path.dirname(os.path.abspath(__file__)) + "/sample.xlsx")

#Exchanges===============================
def poloniex():
	url="https://poloniex.com/public?command=returnTicker"
	api = requests.get(url)
	# Парсим джексоном на блоки
	data = json.loads(api.text)
	return data

def criptopia():
	url="https://www.cryptopia.co.nz/api/GetMarkets"
	api = requests.get(url)
	# Парсим джексоном на блоки
	data = json.loads(api.text)
	return data

def crypto_bridge():
	url="https://api.crypto-bridge.org/api/v1/ticker"
	api = requests.get(url)
	# Парсим джексоном на блоки
	data = json.loads(api.text)
	return data

	
def bittrex():
	url="https://bittrex.com/api/v1.1/public/getmarketsummaries"
	api = requests.get(url)
	# Парсим джексоном на блоки
	data = json.loads(api.text)
	return data

def south_exchange():
	url="https://www.southxchange.com/api/prices"
	api = requests.get(url)
	# Парсим джексоном на блоки
	data = json.loads(api.text)
	return data

def stocks_exchange():
	url="https://app.stocks.exchange/api2/ticker"
	api = requests.get(url,timeout=15)
	# Парсим джексоном на блоки
	data = json.loads(api.text)
	return data

def graviex_exchange():
	url="https://graviex.net/api/v2/tickers.json"
	api = requests.get(url)
	# Парсим джексоном на блоки
	data = json.loads(api.text)
	return data

#Pools=================================================
def bsod_api():
	url="http://api.bsod.pw/api/currencies"
	api = requests.get(url)
	# Парсим джексоном на блоки
	data = json.loads(api.text)
	return data

#BTC price from bittrex exchange in $
def bittrex_btc_price():
	url="https://bittrex.com/api/v1.1/public/getmarketsummary?market=USDT-BTC"
	api = requests.get(url)
	# Парсим джексоном на блоки
	data = json.loads(api.text)

	for i in data:
		if i=='result':
			for h in data[i]:
					res=h["Last"]
	return int(res)
"""
def earn_per_day():
	d=round(coins_day*price,2)
	return d

def earn_per_week():
	w=round(coins_day*price,2)
	return w

def earn_per_month():
	m=round(coins_day*price,2)
	return m"""

def main():
	btc_price=bittrex_btc_price()
	bsod=bsod_api()
	bridge=crypto_bridge()
	grav=graviex_exchange()
	cri=criptopia()
	south=south_exchange()

	sql='INSERT INTO tbl VALUES (?,?,?,?,?,?,?,?,?,?,?)'
	sql_params='bsod[i]["name"],i,bsod[i]["algo"],exch,round(float(bsod[i]["reward"]),2),bsod[i]["difficulty"],coins_day,price,day,week,month,'

	print("\nBTC/USD price(Bittrex): ",btc_price,"$\n")
	
	cnt=0
	for i in (bsod.keys()):
		if bsod[i]["algo"]=="c11":
				hash_rate=c11
		elif bsod[i]["algo"]=="nist5":
				hash_rate=nist5
		elif bsod[i]["algo"]=="skein":
				hash_rate=skein
		elif bsod[i]["algo"]=="neoscrypt":
				hash_rate=neoscrypt
		elif bsod[i]["algo"]=="tribus":
				hash_rate=tribus
		elif bsod[i]["algo"]=="lyra2z":
				hash_rate=lyra2z
		elif bsod[i]["algo"]=="lyra2v2":
				hash_rate=lyra2v2
		elif bsod[i]["algo"]=="xevan":
				hash_rate=xevan
		elif bsod[i]["algo"]=="x16r":
				hash_rate=x16r
		elif bsod[i]["algo"]=="x16s":
				hash_rate=x16s
		elif bsod[i]["algo"]=="phi1612":
				hash_rate=phi1612
		elif bsod[i]["algo"]=="x17":
				hash_rate=x17
		elif bsod[i]["algo"]=="blake2s":
				hash_rate=blake2s
		elif bsod[i]["algo"]=="bitcore":
				hash_rate=timetravel10
		elif bsod[i]["algo"]=="equihash":
				hash_rate=equihash
		elif bsod[i]["algo"]=="skunkhash":
				hash_rate=skunkhash
		elif bsod[i]["algo"]=="keccak":
				hash_rate=keccak
		elif bsod[i]["algo"]=="phi2":
				hash_rate=phi2
		elif bsod[i]["algo"]=="aergo":
				hash_rate=aeriumx	
		elif bsod[i]["algo"]=="hex":
				hash_rate=hexon	
		elif bsod[i]["algo"]=="bcd":
				hash_rate=bcd		
		elif bsod[i]["algo"]=="x13":
				hash_rate=x13		
		elif bsod[i]["algo"]=="sha256d":
				hash_rate=sha256d		
		elif bsod[i]["algo"]=="lbk3":
				hash_rate=lbk3		

		else:
				hash_rate=0
		if bsod[i]["difficulty"]==0:
				bsod[i]["difficulty"]=0.9
		

		
		coins_day=round(86400*float(bsod[i]["reward"])*hash_rate/4294967296/bsod[i]["difficulty"]*1000000,2)


		for h in bridge:
			if h["id"]==(i+"_BTC") and (i!='STN') and (i!='AKL') and bsod[i]["algo"]!='scrypt' and bsod[i]["algo"]!='x11':
				price=round(float(h["bid"])*btc_price,5)
				day=round(coins_day*price,2)
				week=round(coins_day*price*7,2)
				month=round(coins_day*price*30,2)
				exch='Bridge'
				cnt+=1
				cur.execute(sql,(bsod[i]["name"],i,bsod[i]["algo"],exch,round(float(bsod[i]["reward"]),2),bsod[i]["difficulty"],coins_day,price,day,week,month,))
				conn.commit()
		
	#	stocks=stocks_exchange()	
	#	for g in stocks:
	#		if g["market_name"]==(i+"_BTC") and (i!='STN') and bsod[i]["algo"]!='scrypt' and bsod[i]["algo"]!='x11':
	#			price=round(float(g["bid"])*btc_price,5)
	#			day=round(coins_day*price,2)
	#			week=round(coins_day*price*7,2)
	#			month=round(coins_day*price*30,2)
	#			exch='Stocks'
	#			cnt+=1
	#			cur.execute(sql,(bsod[i]["name"],i,bsod[i]["algo"],exch,round(float(bsod[i]["reward"]),2),bsod[i]["difficulty"],coins_day,price,day,week,month,))
	#			conn.commit()

			
		
		for k in grav:
			if k==(i.lower()+"btc") and (i!='STN') and bsod[i]["algo"]!='scrypt' and bsod[i]["algo"]!='x11':
				price=round(float(grav[k]['ticker']['buy'])*btc_price,5)
				day=round(coins_day*price,2)
				week=round(coins_day*price*7,2)
				month=round(coins_day*price*30,2)
				exch='Graviex'
				cnt+=1
				cur.execute(sql,(bsod[i]["name"],i,bsod[i]["algo"],exch,round(float(bsod[i]["reward"]),2),bsod[i]["difficulty"],coins_day,price,day,week,month,))
				conn.commit()
			

		
		for u in cri:
			if u=='Data':
				for k in cri[u]:
					if k['Label']==(i+"/BTC") and (i!='STN')  and bsod[i]["algo"]!='scrypt' and bsod[i]["algo"]!='x11':
						price=round(float(k["BidPrice"])*btc_price,5)
						day=round(coins_day*price,2)
						week=round(coins_day*price*7,2)
						month=round(coins_day*price*30,2)
						exch='Criptopia'
						cnt+=1	
						cur.execute(sql,(bsod[i]["name"],i,bsod[i]["algo"],exch,round(float(bsod[i]["reward"]),2),bsod[i]["difficulty"],coins_day,price,day,week,month,))
						conn.commit()
							
		
		for k in south:
			if k["Market"]==(i+"/BTC") and (i!='STN') and bsod[i]["algo"]!='scrypt' and bsod[i]["algo"]!='x11':
				price=round(float(k['Bid'])*btc_price,5)
				day=round(coins_day*price,2)
				week=round(coins_day*price*7,2)
				month=round(coins_day*price*30,2)
				exch='South'
				cnt+=1
				cur.execute(sql,(bsod[i]["name"],i,bsod[i]["algo"],exch,round(float(bsod[i]["reward"]),2),bsod[i]["difficulty"],coins_day,price,day,week,month,))
				conn.commit()


				

	
	
	format="%-22s %-7s %-10s %-10s %-10s %-11s %-10s %-10s %-10s %-10s %-10s"
	f_str="%-15s%-6s%-5s%-15s%-6s%-5s%-15s%-7s%-5s"

	print (format % ("Name","Ticker","Algoritm","Exchange","Reward","Difficult","Coins/day","Price($)","Day($)","Week($)","Month($)\n"))
	for row in cur.execute("select  name ,ticker,algoritm,exchange,reward,difficult,coins_day,max(price),day,week,month  from tbl group by name  order by day desc"):
		print(format % (row))

	
	print ("\nTotal :", cnt)
	print(f_str %("\nc11 =",c11,"Mh/s\t","nist5 =",nist5,"Mh/s\t","skein =",skein,"Mh/s\n"))
	print(f_str %("neoscrypt =",neoscrypt,"Mh/s\t","tribus =",tribus,"Mh/s\t","lyra2z =",round(lyra2z,2),"Mh/s\n"))
	print(f_str %("lyra2v2 =",lyra2v2,"Mh/s\t","xevan =",xevan,"Mh/s\t","x16r =",x16r,"Mh/s\n"))
	print(f_str %("x16s =",x16s,"Mh/s\t","phi1612 =",phi1612,"Mh/s\t","x17 =",x17,"Mh/s\n"))
	print(f_str %("blake2s =",blake2s,"Mh/s\t","timetravel10 =",timetravel10,"Mh/s\t","equihash =",equihash*1000,"Sol/s\n"))
	print(f_str %("skunkhash =",skunkhash,"Mh/s\t","keccak =",keccak,"Mh/s\t","phi2 =",phi2,"Mh/s\n"))
	print("%-15s %-6s %-5s %-15s %-6s %-5s" %("aeriumx =",aeriumx,"Mh/s\t","hex =",hexon,"Mh/s\t"))

if __name__=="__main__":
	main()