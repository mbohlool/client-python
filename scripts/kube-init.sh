#!/bin/bash

# Copyright 2017 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -x

# Install docker if needed
path_to_executable=$(which docker)
if [ -x "$path_to_executable" ] ; then
    echo "Found Docker installation"
else
    curl -sSL https://get.docker.io | sudo bash
fi
docker --version
sudo docker ps
docker ps

if ! which minikube > /dev/null 2>&1; then

    echo "Cannot find minikube. Starting minikube CI version ..."

    # Copied from https://github.com/kubernetes/minikube#linux-ci-installation-which-supports-running-in-a-vm-example-w-kubectl-installation

    curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube
    curl -Lo kubectl https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && chmod +x kubectl && sudo mv kubectl /usr/local/bin/

    export MINIKUBE_WANTUPDATENOTIFICATION=false
    export MINIKUBE_WANTREPORTERRORPROMPT=false
    export MINIKUBE_HOME=~
    export CHANGE_MINIKUBE_NONE_USER=true
    mkdir ~/.kube || true
    touch ~/.kube/config

    export KUBECONFIG=~/.kube/config
    sudo -E ./minikube start --vm-driver=none --use-vendored-driver

    # this for loop waits until kubectl can access the api server that minikube has created
    for i in {1..150} # timeout for 5 minutes
    do
       kubectl get po
       if [ $? -ne 1 ]; then
          break
      fi
      sleep 2
    done

else

    echo "Found minikube, make sure it is tarted before running this script."
    export KUBECONFIG=~/.kube/config

fi

# kubectl commands are now able to interact with minikube cluster
echo "Dump Kubernetes Objects..."
kubectl cluster-info
kubectl get componentstatuses
kubectl get configmaps
kubectl get daemonsets
kubectl get deployments
kubectl get events
kubectl get endpoints
kubectl get horizontalpodautoscalers
kubectl get ingress
kubectl get jobs
kubectl get limitranges
kubectl get nodes
kubectl get namespaces
kubectl get pods
kubectl get persistentvolumes
kubectl get persistentvolumeclaims
kubectl get quota
kubectl get resourcequotas
kubectl get replicasets
kubectl get replicationcontrollers
kubectl get secrets
kubectl get serviceaccounts
kubectl get services
kubectl get componentstatuses
kubectl get nodes
kubectl describe nodes

./minikube logs

echo "Running tests..."
set -x -e
# Yield execution to venv command
$*
