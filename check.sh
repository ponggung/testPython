python="/usr/local/src/anaconda3/bin/python"
dir="/home/user/project"

for i in {1..59}
do
    sleep 1
    SERVICE='Foo.py'
    if ps ax | grep -v grep | grep $SERVICE > /dev/null
    then
        echo "$SERVICE service running, everything is fine"
    else
        echo "$SERVICE is not running"
        cd $dir ; $python $SERVICE &>/dev/null 2>&1
    fi
done