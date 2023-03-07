BUILD_NUM=$1

if [[ -z "$BUILD_NUM" ]];then
   echo "Please provide build number. Exiting...."
   exit 1
fi

deploymentFile=k8s-config/myapp-deployment.yaml
deploymentBackupFile=.myapp-deployment.yaml
serviceFile=k8s-config/myapp-service.yaml

# build image
docker build -t localhost:5001/flask-app:${BUILD_NUM}.0 .

# save image
docker push -t localhost:5001/flask-app:${BUILD_NUM}.0

# delete & create config
cd config-map-file && sh create-config-map.sh
cd ..

# delete deployment
kubectl -n flask-app-dev delete -f k8s-config

# update deployment
sed -e "s/BUILD_NUM/$BUILD_NUM/g" $deploymentFile > $deploymentBackupFile

# create deployment
kubectl -n flask-app-dev apply -f $deploymentBackupFile
kubectl -n flask-app-dev apply -f $serviceFile
