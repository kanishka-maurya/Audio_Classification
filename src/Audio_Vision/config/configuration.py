from Audio_Vision.utils.common import read_yaml, create_directories
from pathlib import Path
from Audio_Vision.entity.config_entity import DataIngestionConfig, DataPreprocessingConfig

class ConfigurationManager():
    def __init__(self):
        self.config_filepath = Path("config/config.yaml")
        self.params_filepath = Path("params.yaml")

        self.config = read_yaml(self.config_filepath)
        self.params = read_yaml(self.params_filepath)

        create_directories([self.config.artifacts_root]) 

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=  config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        config = self.config.data_preprocessing
        params = self.params

        create_directories([config.root_dir])

        data_preprocessing_config = DataPreprocessingConfig(
            root_dir =  config.root_dir,
            input_data_dir = config.input_data_dir,
            preprocessed_audios_dir = config.preprocessed_audios_dir,
            dataframe_dir = config.dataframe_dir,
            num_samples = params.num_samples,
            max_overlays = params.max_overlays,
            metadata_mapping = params.metadata_mapping
        )
        return data_preprocessing_config