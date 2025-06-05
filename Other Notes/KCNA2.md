# KCNA Exam Study Guide (Questions 1-50)

## Section 1: Kubernetes Fundamentals (1-20)

### Q1. What is Kubernetes?
**Answer:**  
Kubernetes (K8s) is an open-source **container orchestration platform** that automates:
- Deployment
- Scaling
- Management of containerized applications

**Key Features:**
- Self-healing (restarts failed containers)
- Load balancing
- Secret/configuration management

**Example:**  
Running a microservices-based e-commerce app with:
- Frontend (React containers)
- Backend (Node.js containers)
- Database (PostgreSQL containers)

---

### Q2. What is a Pod?
**Answer:**  
The smallest deployable unit in Kubernetes that:
- Contains **1+ containers** sharing:
  - Network namespace (same IP)
  - Storage volumes
- Has a unique cluster IP

**Example YAML:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-pod
spec:
  containers:
  - name: nginx
    image: nginx:1.21
    ports:
    - containerPort: 80
```

**Key Facts:**
- Ephemeral (gets recreated if deleted)
- Typically managed by higher-level objects (Deployments)

---

### Q3. What is a Node?
**Answer:**  
A worker machine (physical/virtual) where Pods run, with these components:

1. **Kubelet** - Agent communicating with control plane
2. **Container Runtime** (Docker/containerd) - Runs containers
3. **kube-proxy** - Manages network rules

**Node Types:**
- **Worker Nodes** - Run application workloads
- **Control Plane Nodes** - Run Kubernetes management services

**Command to check Nodes:**
```bash
kubectl get nodes
```

---

### Q4. What is the Control Plane?
**Answer:**  
The "brain" of Kubernetes consisting of:

| Component          | Function                                                                 |
|--------------------|--------------------------------------------------------------------------|
| API Server         | Entry point for all REST commands (`kubectl` talks to this)              |
| Scheduler          | Assigns Pods to Nodes based on resources                                 |
| Controller Manager | Ensures cluster state matches specifications (e.g., replica count)       |
| etcd               | Highly available key-value store for cluster data                       |

**Diagram:**
```
Control Plane (Master)
├── API Server
├── Scheduler
├── Controller Manager
└── etcd
```

---

### Q5. What is `kubectl`?
**Answer:**  
The command-line interface for interacting with Kubernetes clusters.

**Essential Commands:**

| Command                          | Purpose                                  |
|----------------------------------|------------------------------------------|
| `kubectl get pods`               | List all Pods                            |
| `kubectl describe pod <name>`    | Show detailed Pod info                   |
| `kubectl logs <pod-name>`        | View container logs                      |
| `kubectl apply -f config.yaml`   | Deploy resources from YAML               |

**Example Workflow:**
```bash
# Create a Pod
kubectl apply -f pod.yaml

# Verify
kubectl get pods

# Debug
kubectl logs my-pod -c my-container
```

---

### Q6. What is a Namespace?
**Answer:**  
Logical isolation mechanism for organizing resources (like virtual clusters).

**Common Namespaces:**
- `default` - Where resources go if no NS specified
- `kube-system` - For Kubernetes system components
- `kube-public` - Readable by all users

**Example Creating NS:**
```bash
kubectl create namespace staging
```

**Example YAML Reference:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  namespace: staging  # Assign to specific NS
```

---

### Q7. What is `kubelet`?
**Answer:**  
The primary **node agent** that:
1. Receives Pod specs from API Server
2. Ensures containers are running/healthy
3. Reports Node status back to control plane

**Key Responsibilities:**
- Starts/Stops containers
- Mounts volumes
- Runs liveness/readiness probes

---

### Q8. What is `kube-proxy`?
**Answer:**  
Maintains network rules to enable communication:
- Implements `Service` concepts (ClusterIP, NodePort)
- Uses iptables/IPVS for load balancing

**Example Flow:**
1. User accesses Service IP
2. `kube-proxy` redirects to a backend Pod

---

### Q9. What is `etcd`?
**Answer:**  
Distributed, consistent key-value store that holds:
- Cluster state (all objects)
- Configuration data
- Service discovery info

**Characteristics:**
- Uses Raft consensus algorithm
- Typically runs on control plane nodes
- Requires backups for disaster recovery

---

### Q10. What is a Container Runtime?
**Answer:**  
Software that runs containers, such as:
1. **Docker** (historically common)
2. **containerd** (default in newer K8s)
3. **CRI-O** (Red Hat's lightweight runtime)

**Configured in `/var/lib/kubelet/kubeadm-flags.env`:**
```
--container-runtime=remote
--container-runtime-endpoint=unix:///run/containerd/containerd.sock
```

---

## Section 2: Kubernetes Objects (21-40)

### Q21. What is a Deployment?
**Answer:**  
Manages stateless applications by:
- Maintaining desired replica count
- Enabling rolling updates/rollbacks
- Scaling Pods up/down

**Example YAML:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.23
        ports:
        - containerPort: 80
```

**Key Commands:**
```bash
# Scale deployment
kubectl scale deploy/nginx-deployment --replicas=5

# Update image
kubectl set image deploy/nginx-deployment nginx=nginx:1.24
```

---

### Q22. What is a Service?
**Answer:**  
Abstracts Pods behind:
- Stable IP/DNS name
- Load balancing

**Types:**

| Type          | Description                          | Example Use Case              |
|---------------|--------------------------------------|-------------------------------|
| ClusterIP     | Internal VIP (default)               | Frontend → Backend comms      |
| NodePort      | Exposes on Node's static port        | Development/testing           |
| LoadBalancer  | Cloud-provided external LB           | Production web apps           |

**Example (ClusterIP):**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

---

### Q23. What is a ConfigMap?
**Answer:**  
Stores non-confidential configuration as key-value pairs.

**Creation Methods:**
1. **From literal:**
   ```bash
   kubectl create configmap app-config --from-literal=DB_HOST=mysql
   ```
2. **From file:**
   ```bash
   kubectl create configmap app-config --from-file=config.properties
   ```

**Usage in Pod:**
```yaml
env:
- name: DB_HOST
  valueFrom:
    configMapKeyRef:
      name: app-config
      key: DB_HOST
```

---

### Q24. What is a Secret?
**Answer:**  
Stores sensitive data (passwords, tokens) encoded in base64.

**Example Creation:**
```bash
# Encode data first
echo -n 'password123' | base64

# Create Secret
kubectl create secret generic db-creds \
  --from-literal=username=admin \
  --from-literal-password=cGFzc3dvcmQxMjM=
```

**Mounting in Pod:**
```yaml
volumes:
- name: creds-volume
  secret:
    secretName: db-creds
```

---

### Q25. What is a PersistentVolume (PV)?
**Answer:**  
Cluster-wide storage resource provisioned by admins.

**Example (NFS PV):**
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-nfs
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteMany
  nfs:
    server: nfs-server.example.com
    path: "/exports/data"
```

---

### Q26. What is a PersistentVolumeClaim (PVC)?
**Answer:**  
User's request for storage that binds to a PV.

**Example:**
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-web
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
```

**Usage in Pod:**
```yaml
volumes:
- name: web-storage
  persistentVolumeClaim:
    claimName: pvc-web
```

---

### Q27. What is a StatefulSet?
**Answer:**  
Manages stateful applications with:
- Stable, unique network identifiers
- Persistent storage
- Ordered deployment/scaling

**Example (MongoDB):**
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mongo
spec:
  serviceName: "mongo"
  replicas: 3
  selector:
    matchLabels:
      app: mongo
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
      - name: mongo
        image: mongo:5.0
        ports:
        - containerPort: 27017
        volumeMounts:
        - name: mongo-data
          mountPath: /data/db
  volumeClaimTemplates:
  - metadata:
      name: mongo-data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 10Gi
```

---

### Q28. What is an Ingress?
**Answer:**  
Manages external HTTP(S) access to Services with:
- Host/path-based routing
- TLS termination
- Load balancing

**Example YAML:**
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
spec:
  rules:
  - host: "example.com"
    http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: web-service
            port:
              number: 80
  tls:
  - hosts:
    - example.com
    secretName: tls-cert
```

---

### Q29. What is an Ingress Controller?
**Answer:**  
Implements Ingress rules (requires separate installation). Popular options:
- NGINX Ingress Controller
- Traefik
- AWS ALB Ingress Controller

**Installation Example (NGINX):**
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
```

---

### Q30. What is a NetworkPolicy?
**Answer:**  
Defines how Pods communicate with each other.

**Example (Isolate frontend/backend):**
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-allow-frontend
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
```
