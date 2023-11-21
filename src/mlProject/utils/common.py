#####################################################
# common.py: 
# Funcionalitis we'll be using throught the project
#####################################################

import os
from box.exceptions import BoxValueError # used for creating custome exceptions
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations # makes sure that the types that were declared
                                      # in the function definition remains, by throwing
                                      # an error if the function received a different
                                      # object type than the one declared.
from box import ConfigBox # enables to access different objects as attributes 
                          # (no need to for bracket, use . instead). Very helpful
                          # with accessing config files.
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(yaml_path: Path) -> ConfigBox:
    """
    Reads yaml file and returns:

    Args:
        yaml_path (Path): Path to the yaml file
    
    Raises:
        ValueError: if yaml file is empty

    Returns:
        ConfigBox: ConfigBox object

    """
    try:
        with open(yaml_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {yaml_path} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_dirs(path_to_dirs: list, verbose=True):
    """
    Creates directories from a list

    Args:
        path_to_dirs (list): list of path of directories
        verbose (bool, optional): if True, log actions
    
    Returns:
        None
    """

    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Folder {path} was created successfully")


@ensure_annotations
def save_to_json(path: Path, data: dict):
    """
    Saves json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4) 

    logger.info(f"json file saved at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads json file

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dictionary
    """

    with open(path) as json_file:
        content = json.load(json_file)
    
    logger.info(f"json file: {path} was successfully loaded")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves binary file.

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file

    Returns:
        None
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"binay file: {path} was saved successfully")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loades binary file.

    Args:
        path (Path): path to binary file
    
    Returns:
        Any: the data in the binary file
    """

    data = joblib.load(filename=path)
    logger.info(f"binay file: {path} was loaded successfully")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets size of file in KB.

    Args:
        path (Path) path to file
    
    Returns:
        str: size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"The file {path} has a size of ~{size_in_kb} KB"