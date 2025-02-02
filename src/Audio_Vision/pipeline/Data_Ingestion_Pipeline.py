from Audio_Vision import logger
from Audio_Vision.config import ConfigurationManager
from Audio_Vision.components.Data_Ingestion import DataIngestion

STAGE_NAME = "DATA INGESTION"

class DataIngestionTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f"{"*"*20} Stage: {STAGE_NAME} started {"*"*20}")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{"*"*20} Stage: {STAGE_NAME} completed {"*"*20}")
    except Exception as e:
        raise e 