from src.aimlproject.logger import logging
from src.aimlproject.exception import CustomException
from src.aimlproject.components.data_ingestion import DataIngestion
from src.aimlproject.components.data_ingestion import DataIngestionConfig
from src.aimlproject.components.data_transformation import DataTransformationConfig,DataTransformation
from src.aimlproject.components.model_tranier import ModelTrainerConfig,ModelTrainer
import sys



if __name__=="__main__":
    logging.info("Logging has started")
    
    
#if __name__ == "__main__":
        #logging.basicConfig(level=logging.INFO)'''
        
#try:
    #a = 1/0
   # except Exception as e:
    #logging.info("An error occurred: Division by zero")
   # raise CustomException(e, error_detail=sys)'''
            

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        
        #datat_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_array,test_array,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)
        
        #model tranier
        
        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_array,test_array))
        
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)


    
    