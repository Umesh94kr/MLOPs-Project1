from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    # what we are going to get out of data ingestion
    trained_file_path:str 
    test_file_path:str