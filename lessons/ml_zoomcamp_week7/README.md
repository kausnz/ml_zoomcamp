# Notes
To check who is blocking a port 
```shell
lsof -i tcp:3000
```

Start serving in dev mode
```shell
bentoml serve service.py:cred_risk_svc
```

Start locust. A locustfile.py should be in the dir.
```shell
locust -H http://localhost:3000
```

Build a bento for our application (note - this doesn't create the docker image)
```shell
bentoml build 
```

Build docker image from bento
* here I'm using the latest tag. Change is necessary.
```shell
bentoml containerize credit_risk_classifier:latest
```

## AWS

After creating an elastic container repo (ECR) using the web console in AWS:

1. Create a tag to the remote repo. E.g.
```shell
docker tag credit_risk_classifier:ingvrcsrmcnd26cp 627970965316.dkr.ecr.us-east-1.amazonaws.com/credit-risk-classifier-repo:latest
```
2. Login to the remote repo.
```shell
aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com
```
E.g. `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 627970965316.dkr.ecr.us-east-1.amazonaws.com`
3. Push the image to the remote repo. E.g.
```shell
docker push 627970965316.dkr.ecr.us-east-1.amazonaws.com/credit-risk-classifier-repo:latest
```
