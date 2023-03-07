# delete cm from literal
kubectl -n flask-app-dev delete configmap app-config-literal --ignore-not-found
kubectl -n flask-app-dev delete configmap app-config-file --ignore-not-found
kubectl -n flask-app-dev delete secret credentials --ignore-not-found

# create cm from literal
kubectl -n flask-app-dev create configmap app-config-literal --from-literal ENV_LITERAL_MYVAR=env_value_from_literal --from-literal ENV_LITERAL_MYVAR2="env value from literal with spaces"

# create cm from file
kubectl -n flask-app-dev create configmap app-config-file --from-file=app-env.properties

# create secret from file
kubectl -n flask-app-dev create -f secret.yaml
