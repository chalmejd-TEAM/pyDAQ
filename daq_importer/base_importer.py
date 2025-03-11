from abc import ABC, abstractmethod
import pandas as pd


class BaseImporter(ABC):
    """Abstract base class for all file importers."""

    @abstractmethod
    def load(self, file_path: str) -> pd.DataFrame:
        """Load data from the specified file."""
        pass
