#######################################################
# config_entity.py:
# Used to frame a data configs as an object, according
# to the configuration declared in config/config.yaml
#######################################################

from dataclasses import dataclass # used for defining a class with variables & types
from pathlib import Path

# Data ingestion configuration
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# Data validation configuration
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict # not in config.yaml, will be ingested with shcema.yaml

# Data transformation configuration
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

# Model trainer configuration
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float # from parameter.yaml
    l1: float # from parameter.yaml
    target_column: str # from schema.yaml

# Model evaluation configuration
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict # from params.yaml
    metric_file_name: Path # from config.yaml
    target_column: str 
    mlflow_uri: str # hard-coded in constructor