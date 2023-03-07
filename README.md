
### Python flask app to demo reading environment variables and config file
####     environment variables are introduced through k8s config map and secret
####     file is added to the container using volume and file content is read from config map


### Output response from the app end point
```
$ curl http://localhost:8500/vars |jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   144  100   144    0     0  28800      0 --:--:-- --:--:-- --:--:-- 28800
{
  "ENV_FILE_MYVAR": "env_value_from_file",
  "ENV_LITERAL_MYVAR": "env_value_from_literal",
  "ENV_SECRET_PASS": "password",
  "ENV_SECRET_USER": "username"
}

```

### Sample kind cluster config file is available taken from kind documentation
`$ ./kind-config/kind-cluster-w-internal-registry.sh`
#### this script will install a local registry and create one node kind cluster

### Create a name space for the application
`$ kubectl apply -f k8s-config-init/k8s-flask-app-namespace.yaml`
