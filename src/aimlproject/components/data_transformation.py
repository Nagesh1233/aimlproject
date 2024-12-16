import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.aimlproject.exception import CustomException
from src.aimlproject.logger import logging
import os 


@dataclass
class DataTransformationConfig:
    preprocesser_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
        def get_data_trnasformer_object(self):
            try:
                pass
            except:
                pass