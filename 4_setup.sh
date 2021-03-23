k3d cluster create paloma --volume $(pwd)/resources/protos:/protos

k3d image import -c paloma tkpd/gripmock:latest

kubectl apply -f mock-server-deployment.yml

# kubectl port-forward pod/gripmock-deployment-64797f78dc-dzw7m 4771:4771 4770:4770
