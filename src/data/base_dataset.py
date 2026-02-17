from abc import ABC, abstractmethod
from torch.utils.data import Dataset


class BaseDeepfakeDataset(Dataset, ABC):

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def __getitem__(self, index: int):
        raise NotImplementedError
