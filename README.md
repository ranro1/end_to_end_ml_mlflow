# End-to-End ML Project
This project demonstrates the process of deploying an ML model to production. The model predicts wine quality according to some given parameters. Tools and technologies used:
- CI/CD is done with GitHub actions
- Docker image is stored in AWS ECR
- The deployment environment used is AWS EC2
- The web app is done with Flask
- MLFlow is used to track experiments.

Below is a preview of both the home page and the prediction page:
### Home Page
![home page](https://github.com/ranro1/end_to_end_ml_mlflow/assets/42174030/4fa75f56-0476-459e-acb0-b5b40ddaf217)

### Prediction
![prediction](https://github.com/ranro1/end_to_end_ml_mlflow/assets/42174030/ebe82866-5a0e-4aea-9423-7c21bcefcc4c)




## How to Run? (locally)
### Step 1: Clone and create a CONDA virtual environment.
From now on, run the commands below in CMD/Powershell opened from the repo folder in your File Explorer. 
```bash
conda create -n end_to_end_ml_proj python=3.9 -y
```

```bash
conda activate end_to_end_ml_proj 
```

### Step 2: Install requirements.txt
```
pip install -r requirements.txt
```

### Step 3: Run the App
```bash
python app.py
```

### Step 4: Open Localhost and Port
In `app.py` the URL is: `localhost:8080` or `http://127.0.0.1:8080/`

## How to train?
MLFlow is used in this project as an experiment tracker and optimization. Dagshub is used to integrate it with the code.
### MLFLOW
Run in cmd: ```mlflow ui```

### Dagshub [dagshub](https://dagshub.com/)
Used to integrate MLFlow with the project. Dagshub connects to the git repository and MLFlow. To define the connection, open a new repository and gather the following information:
	* MLFLOW_TRACKING_URI = 
	* MLFLOW_TRACKING_USERNAME =
	* MLFLOW_TRACKING_PASSWORD = 

Set these variables as environment variables and run the following on Windows command (must be run inside the virtual environment):
```bash
$env:MLFLOW_TRACKING_URI = '<from_the_information_above>'

$env:MLFLOW_TRACKING_USERNAME = '<from_the_information_above>'

$env:MLFLOW_TRACKING_PASSWORD = '<from_the_information_above>'
```

* NOTE: In the code, there is a direct reference to the above environment variables.
