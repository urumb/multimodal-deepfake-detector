from dataclasses import dataclass
from pathlib import Path
from typing import Any
import yaml


# =========================
# Config Dataclasses
# =========================

@dataclass(frozen=True)
class ProjectConfig:
    name: str
    seed: int
    device: str


@dataclass(frozen=True)
class LoggingConfig:
    level: str
    save_dir: str


@dataclass(frozen=True)
class DataConfig:
    batch_size: int
    num_workers: int
    image_size: int


@dataclass(frozen=True)
class TrainingConfig:
    epochs: int
    learning_rate: float
    device: str


@dataclass(frozen=True)
class Config:
    project: ProjectConfig
    data: DataConfig
    training: TrainingConfig
    logging: LoggingConfig


# =========================
# Loader
# =========================

def load_config(config_path: str) -> Config:
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(path, "r") as f:
        raw = yaml.safe_load(f)

    return Config(
        project=ProjectConfig(**raw["project"]),
        data=DataConfig(**raw["data"]),
        training=TrainingConfig(**raw["training"]),
        logging=LoggingConfig(**raw["logging"]),
    )
