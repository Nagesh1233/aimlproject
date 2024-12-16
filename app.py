from src.aimlproject.logger import logging
from src.aimlproject.exception import CustomException
from src.aimlproject.components.data_ingestion import DataIngestion
from src.aimlproject.components.data_ingestion import DataIngestionConfig
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
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)


    
    