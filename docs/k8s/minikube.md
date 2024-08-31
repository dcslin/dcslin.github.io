set up k8s in debian

install docker via: <https://docs.docker.com/engine/install/debian/>

add current user to docker user:

```bash
sudo usermod -aG docker $USER && newgrp docker
```

install minikube via: <https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fdebian+package>

run kubectl from minikube

```bash
minikube start

minikube kubectl -- get pods -A

alias kubectl="minikube kubectl --"

```

run dashboard
```bash
minikube dashboard
```



debian command:
```bash
sudo systemctl reboot
sudo systemctl shutdown
```