<h3>This assignment is practise on deploying an nginx service through kubernetes.</h3>

Steps: 
1. minikube start
2. minikube addons enable ingress
3. kubectl apply -f "*.yaml"
4. curl http://$(minikube ip)/
```sh
minikube start

😄  minikube v1.32.0 on Ubuntu 20.04 (docker/amd64)
✨  Automatically selected the docker driver. Other choices: ssh, none
📌  Using Docker driver with root privileges
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
💾  Downloading Kubernetes v1.28.3 preload ...
    > preloaded-images-k8s-v18-v1...:  403.35 MiB / 403.35 MiB  100.00% 93.74 M
    > gcr.io/k8s-minikube/kicbase...:  453.90 MiB / 453.90 MiB  100.00% 77.07 M
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparing Kubernetes v1.28.3 on Docker 24.0.7 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🔎  Verifying Kubernetes components...
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```
```sh
minikube addons enable ingress

💡  ingress is an addon maintained by Kubernetes. For any concerns contact minikube on GitHub.
You can view the list of minikube maintainers at: https://github.com/kubernetes/minikube/blob/master/OWNERS
    ▪ Using image registry.k8s.io/ingress-nginx/controller:v1.9.4
    ▪ Using image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20231011-8b53cabe0
    ▪ Using image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v20231011-8b53cabe0
🔎  Verifying ingress addon...
🌟  The 'ingress' addon is enabled
```
```sh
kubectl apply -f "*.yaml"

deployment.apps/app-1-dep created
ingress.networking.k8s.io/app-1-ingress created
service/app-1-svc created
deployment.apps/app-2-dep created
ingress.networking.k8s.io/app-2-ingress created
service/app-2-svc created
configmap/nginx-config created
deployment.apps/nginx-dep created
ingress.networking.k8s.io/nginx-ingress created
service/nginx-svc created
```
```sh
curl http://$(minikube ip)/

Hello World from [app-1-dep-86f67f4f87-6zcj6]!
Hello World from [app-2-dep-7f686c4d8d-nxm6q]!
Hello World from [app-1-dep-86f67f4f87-6zcj6]!
Hello World from [app-1-dep-86f67f4f87-6zcj6]!
Hello World from [app-1-dep-86f67f4f87-6zcj6]!
Hello World from [app-2-dep-7f686c4d8d-nxm6q]!
Hello World from [app-1-dep-86f67f4f87-6zcj6]!
Hello World from [app-1-dep-86f67f4f87-6zcj6]!
Hello World from [app-1-dep-86f67f4f87-6zcj6]!
Hello World from [app-1-dep-86f67f4f87-6zcj6]!
```