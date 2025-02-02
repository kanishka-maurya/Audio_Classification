from Audio_Vision import logger
from Audio_Vision.config import ConfigurationManager
from Audio_Vision.components.Data_Preprocessing import DataPreprocessing

STAGE_NAME = "DATA PREPROCESSING"

class DataPreprocessingTrainingPipeline():
    def __init__(self):
        pass

    def DataPreprocessingTrainingPipeline(self):
        config = ConfigurationManager()
        data_preprocessing_config = config.get_data_preprocessing_config()
        data_preprocessing = DataPreprocessing(config = data_preprocessing_config)
        data_preprocessing.data_preprocessing()

if __name__ == '__main__':
    try:
        logger.info(f"{"*"*20} Stage: {STAGE_NAME} started {"*"*20}")
        obj = DataPreprocessingTrainingPipeline()
        obj.main()
        logger.info(f"{"*"*20} Stage: {STAGE_NAME} completed {"*"*20}")
    except Exception as e:
        raise e 