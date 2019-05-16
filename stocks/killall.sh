 ps -ef |grep python|grep 000404|grep -v grep |awk '{print $2}'|xargs kill;ps -ef |grep tmp|grep -v grep |awk '{print $2}'|xargs kill 
