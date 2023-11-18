#######################################################
# config_entity.py:
# Used to frame a data ingestion configs as an object
#######################################################

from dataclasses import dataclass # used for defining a class with variables & types
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path