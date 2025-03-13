import pandas as pd
from ..base_importer import BaseImporter


class CSVImporter(BaseImporter):
    def load(self, file_path: str) -> pd.DataFrame:
        try:
            df = pd.read_csv(file_path)
            return df
        except Exception as e:
            raise ValueError(f"Error loading CSV file: {e}")