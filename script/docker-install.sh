curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun

sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
    "registry-mirrors": [
        "https://0yiqg6lp.mirror.aliyuncs.com",
        "https://dockerhub.azk8s.cn"
    ],
  "insecure-registries" : [
    "0yiqg6lp.mirror.aliyuncs.com",
    "dockerhub.azk8s.cn"
  ]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker