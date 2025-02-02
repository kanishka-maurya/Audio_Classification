from Audio_Vision import logger
from Audio_Vision.pipeline.Data_Ingestion_Pipeline import DataIngestionTrainingPipeline
from Audio_Vision.pipeline.Data_Preprocessing_Pipeline import DataPreprocessingTrainingPipeline

STAGE_NAME = "DATA INGESTION"
try:
    logger.info(f"{"*"*20} Stage {STAGE_NAME} started {"*"*20}")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{"*"*20} Stage {STAGE_NAME} completed {"*"*20}")
except Exception as e:
     raise e 


STAGE_NAME = "DATA PREPROCESSING"
try:
    logger.info(f"{"*"*20} Stage: {STAGE_NAME} started {"*"*20}")
    obj = DataPreprocessingTrainingPipeline()
    obj.main()
    logger.info(f"{"*"*20} Stage: {STAGE_NAME} completed {"*"*20}")
except Exception as e:
    raise e 