from typing import Dict, Type
from src.data.base_dataset import BaseDeepfakeDataset

_DATASET_REGISTRY: Dict[str, Type[BaseDeepfakeDataset]] = {}


def register_dataset(name: str):
    def decorator(cls: Type[BaseDeepfakeDataset]):
        _DATASET_REGISTRY[name] = cls
        return cls
    return decorator


def get_dataset(name: str):
    if name not in _DATASET_REGISTRY:
        raise ValueError(f"Dataset '{name}' not registered.")
    return _DATASET_REGISTRY[name]
