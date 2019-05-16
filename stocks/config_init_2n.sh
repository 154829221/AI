days=`python init_days_1n.py`  
sed "s#XXXXXX#$days#g"  config.py.temp >  config.py
