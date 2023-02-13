### These labels affect how your app is viewed in Tanzu Observability and K8S
export K8S_NAMESPACE=observability-system
export K8S_APPLICATION=otel-vanilla-demo-app
export K8S_CLUSTER=otel-test-gke-cluster-021323
export K8S_LOCATION=k8s-cluster
export K8S_ENVIRONMENT=dev
export K8S_REPOSITORY=projects.registry.vmware.com/tanzu_observability_keights_saas/vanilla-demo-app/

### Update with your Tanzu Observability by Wavefront info
export WAVEFRONT_BASE64_TOKEN=[BASE 64 ENCODED API TOKEN]
export WAVEFRONT_URL=https://[YOUR CLUSTER].wavefront.com/api

### Define for Tanzu Application Service Deploy
### otherwise leave empty
export TASDOMAIN=""
#example: export TASDOMAIN=-service.apps.internal

### Use default to deploy a proxy to the K8S namespace
### Edit for For Docker or Tanzu Application Service deploy
export WF_PROXY_HOST=${K8S_NAMESPACE}-wavefront-proxy  


