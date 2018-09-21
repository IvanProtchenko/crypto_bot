use crypto;

CREATE TABLE `items` (
`name` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT ''
)  ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin

CREATE TABLE `history` (
`name` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT 'DEFAULT',
`price` double(16,8) NOT NULL DEFAULT '0.0',
`amount` double(16,8) NOT NULL DEFAULT '0.0',
`time` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin

CREATE TABLE `history_depth` (
`name` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT 'DEFAULT',
`amount` double(16,8) NOT NULL DEFAULT '0.0',
`time` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin

CREATE TABLE `history_1m` (
`name` varchar(255) COLLATE utf8_bin NOT NULL DEFAULT 'DEFAULT',
`price_min` double(16,8) NOT NULL DEFAULT '0.0',
`price_max` double(16,8) NOT NULL DEFAULT '0.0',
`amount` double(16,8) NOT NULL DEFAULT '0.0',
`time` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin


{"globalTradeID":390237812,"tradeID":25457603,
"date":"2018-09-15 10:44:58","type":"buy",
"rate":"6524.00000000","amount":"0.00100000","total":"6.52400000"}

time.mktime(time.strptime('2018-09-15 10:44:58', '%Y-%m-%d %H:%M:%S'))

текущий курс для всех
https://bitforex.com/server/market.act?cmd=searchTickers&type=all


https://bitforex.com/napi/getCurTradeCoinInfoData?tradeType=1&commodityCode=BTC&currencyCode=USDT


#
Информация о том какие пары торгуются
https://api.bitforex.com/api/v1/market/symbols

#
Ticker Information
https://api.bitforex.com/api/v1/market/ticker

symbol 	String 	Description 	- 	Trading pairs such as coin-usd-btc, coin-usd-eth, etc.

Depth information
https://api.bitforex.com/api/v1/market/depth?symbol=coin-usdt-btc&size=600
symbol 	String 	Yes 	- 	Trading pairs such as coin-usd-btc, coin-usd-eth, etc.
size 	int 	No (defaults to 5) 	- 	Orders Depth Quantity 1-200


https://api.bitforex.com/api/v1/market/trades?symbol=coin-usdt-btc&size=600

symbol 	String 	Yes 	- 	Trading pairs such as coin-usd-btc, coin-usd-eth, etc.
size 	int 	No (default is 1) 	- 	The number of transactions is 1-600
