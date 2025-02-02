from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig():
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataPreprocessingConfig():
    root_dir: Path
    input_data_dir: Path
    preprocessed_audios_dir: Path
    dataframe_dir: Path
    num_samples: int
    max_overlays: int
    metadata_mapping: dict