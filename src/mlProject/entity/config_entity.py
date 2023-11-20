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