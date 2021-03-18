export PWD=pwd
CONTAINER_ID=`docker run -p 4770:4770 -p 4771:4771 -v $PWD/../src/resources/protos/:/proto tkpd/gripmock $1`

until [ "`/usr/bin/docker inspect -f {{.State.Status}} mock-server`"=="running" ]; do
    sleep 0.1;
done;

value=`cat $2`
curl -X POST -d '$value'  http://localhost:4771/add
