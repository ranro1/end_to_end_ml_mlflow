## How to Run?

### Steps:

clone repo:
```bash
git clone https://github.com/ranro1/end_to_end_ml_mlflow.git
```

### Step 1: Create CONDA virtual environement and activate it. Do the commands below after opening CMD/Powershell from the repo folder in your File Explorer
```bash
conda create -n end_to_end_ml_proj python=3.9 -y
```

```bash
conda activate end_to_end_ml_proj 
```

### Step 2: install requirements.txt
```
pip install -r requirements.txt
```

### Step 3: run the app
```bash
python app.py
```

### Step 4: open up your local host and port
Usually:
```bash
localhost:8000 or http://127.0.0.1:8000/
```


### MLFLOW
##### from cmd:
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/ranro3/end_to_end_ml_mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=ranro3 \
MLFLOW_TRACKING_PASSWORD=4841ebe9c6cccbf89d4e5c07339d949acf33652e \
python script.py


To set as environement variables, run the following on windows command (must be run inside the virtual environement):
```bash
$env:MLFLOW_TRACKING_URI = 'https://dagshub.com/ranro3/end_to_end_ml_mlflow.mlflow'

$env:MLFLOW_TRACKING_USERNAME = 'ranro3'

$env:MLFLOW_TRACKING_PASSWORD = '4841ebe9c6cccbf89d4e5c07339d949acf33652e'
```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 886266282133.dkr.ecr.eu-north-1.amazonaws.com/mlproj_winery_quality

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = eu-north-1

    AWS_ECR_LOGIN_URI = 886266282133.dkr.ecr.eu-north-1.amazonaws.com

    ECR_REPOSITORY_NAME = mlproj_winery_quality