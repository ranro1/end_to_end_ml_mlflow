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


