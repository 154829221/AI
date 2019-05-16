for j in `ls *.txt`;do
idlist=`cat $j |awk '{print $2}'`
type=`echo $j |sed 's#.txt##g'`
for i in $idlist;do echo ./getdata.py $type $i;done
done
