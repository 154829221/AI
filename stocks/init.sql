CREATE TABLE `stocks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_type` varchar(50) NOT NULL,
  `stock_code` varchar(10) NOT NULL,
  `date` varchar(20) NOT NULL,
  `open_price` double(20,5) NOT NULL,
  `close_price` double(20,5) NOT NULL,
  `max_price` double(20,5) NOT NULL,
  `min_price` double(20,5) NOT NULL,
  `trade_money` double(30,5) NOT NULL,
  `diff_money` double(20,5) NOT NULL,
  `diff_rate` double(20,5) NOT NULL,
  `swing` double(20,5) NOT NULL,
  `turnover` double(20,5) NOT NULL,
  `market` varchar(4) NOT NULL,
  `code` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `u_stock_type_stock_code_date` (`stock_type`,`stock_code`,`date`),
  KEY `index_date` (`date`),
  KEY `stock_type_date` (`stock_type`,`date`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

select * from stocks
where date in ("","","","","","","") and stock_type=""
if len()==7

