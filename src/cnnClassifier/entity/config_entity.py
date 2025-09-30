from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path = Path("artifacts/data_ingestion")
    source_URL: str = "https://drive.google.com/file/d/1z0mreUtRmR-P-magILsDR3T7M6IkGXtY/view?usp=sharing"
    local_data_file: Path = root_dir / "Chest-CT-Scan-data.zip"
    unzip_dir: Path = root_dir / "unzipped"