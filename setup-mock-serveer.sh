docker run -p 4770:4770 -p 4771:4771 -v $PWD/src/resources/protos/:/proto tkpd/gripmock /proto/Comp-b.proto
curl -X POST -d '{
    "service":"CompB",
    "method":"getData",
    "input":{
      "equals":{
        "firstName":"Jaydatt"
      }
    },
    "output":{
      "data":{
        "lastName":"Desai"
      }
    }
  }'
