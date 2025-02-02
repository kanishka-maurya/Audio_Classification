import os
import random
import pandas as pd
from pydub import AudioSegment
from Audio_Vision import logger
from Audio_Vision.entity.config_entity import DataPreprocessingConfig
from Audio_Vision.utils.common import create_directories

class DataPreprocessing():
    def __init__(self, config: DataPreprocessingConfig):
        self.config = config

    def data_preprocessing(self):
        
        data_dir = self.config.input_data_dir  
        output_dir = self.config.preprocessed_audios_dir
        dataframe_dir = self.config.dataframe_dir
 
        metadata_mapping = self.config.metadata_mapping
        all_audio_files = os.listdir(data_dir)
        class_audio_map = {}
        for file in all_audio_files:
            if file.endswith(".wav"):
                class_id = file.split("_")[0]  
                class_audio_map.setdefault(class_id, []).append(file)

        num_samples = self.config.num_samples  
        max_overlays = self.config.max_overlays  

        data = []
        for i in range(num_samples):
            num_overlay = random.randint(2, max_overlays)  
            selected_classes = random.sample(list(class_audio_map.keys()), num_overlay)  

            mixed_audio = None
            labels_numeric = []
            labels_text = []

            for cls in selected_classes:
                audio_file = random.choice(class_audio_map[cls])  
                audio_path = os.path.join(data_dir, audio_file)
                sound = AudioSegment.from_wav(audio_path)  
                if mixed_audio is None:
                    mixed_audio = sound  
                else:
                    mixed_audio = mixed_audio.overlay(sound)  

                labels_numeric.append(cls) 
                labels_text.append(metadata_mapping.get(cls, "unknown"))  

            output_filename = f"mixed_{i}.wav"
            output_path = os.path.join(output_dir, output_filename)
            create_directories([output_dir]) 
            mixed_audio.export(output_path, format="wav")
            data.append({"file_path": output_path, "labels_numeric": labels_numeric, "labels_text": labels_text})

        df = pd.DataFrame(data)
        df.to_csv(os.path.join(dataframe_dir, "preprocessed_data.csv"), index=False)
        logger.info("Multi-label dataset with metadata mapping created successfully!")
