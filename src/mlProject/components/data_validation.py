###########################################################
# data_validation.py:
# Contains a class called DataValidation that represents
# a data validation object, which validates the data
# according to schema.yaml
###########################################################

import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

        
    def validate_all_columns(self) -> bool:
        """
        Checks that the columns and their data types in the .csv file are exactly as declared in schema.yaml  

        Args:
            None
        
        Returns:
            bool: if the data is valid or not
        """
        # try:
        validation_status = None

        cols_validation_counter = 0
        
        data = pd.read_csv(self.config.unzip_data_dir) # read the .csv file
        all_cols = list(data.columns)

        all_schema_dict = self.config.all_schema # dict for both columns and data types


        for col in all_cols:
            if col not in all_schema_dict.keys(): # if column is not in schema.yaml
                validation_status = False
                with open(self.config.STATUS_FILE, "a") as f:
                    f.write(f"Column: '{col}' not is SCHEMA. Validation status: {validation_status}\n")

            else:
                if data[col].dtype != all_schema_dict[col]: # if column is in schema.yaml but with different data type
                    validation_status = False
                    with open(self.config.STATUS_FILE, "a") as f:
                        f.write(f"Column: '{col}' data type not in SCHEMA. Validation status: {validation_status}\n")
                
                else: # both column name and data type are valid
                    validation_status = True
                    cols_validation_counter+=1
                    with open(self.config.STATUS_FILE, "a") as f:
                        f.write(f"Column: '{col}' validation status: {validation_status}\n")
        
        if cols_validation_counter==len(all_cols):
            with open(self.config.STATUS_FILE, "a") as f:
                f.write("Valid")

        return validation_status
        
        # except Exception as e:
            # raise e
