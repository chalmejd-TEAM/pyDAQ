import pandas as pd
import scipy.io
from ..base_importer import BaseImporter

class MATImporter(BaseImporter):
    def load(self, file_path: str) -> pd.DataFrame:
        try:
            mat_data = scipy.io.loadmat(file_path)

            # Remove metadata keys that start with '__'
            cleaned_data = {k: v for k, v in mat_data.items() if not k.startswith("__")}

            # Convert to DataFrame (handles both struct and array cases)
            df = pd.DataFrame({k: v.flatten() if isinstance(v, (list, tuple)) else v for k, v in cleaned_data.items()})

            return df
        except Exception as e:
            raise ValueError(f"Error loading MAT file: {e}")
