set up k8s in debian

install docker via: <https://docs.docker.com/engine/install/debian/>

add current user to docker user:

```bash
sudo usermod -aG docker $USER && newgrp docker
```

install <https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fdebian+package>

start minikube

```bash
minikube start
```

run kubectl from minikube


```bash
minikube kubectl -- get pods -A
```
```bash
alias kubectl="minikube kubectl --"
```

dashboard
```bash
minikube dashboard
```
