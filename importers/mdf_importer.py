from asammdf import MDF
import pandas as pd
from ..base_importer import BaseImporter

class MDFImporter(BaseImporter):
    def load(self, file_path: str) -> pd.DataFrame:
        mdf = MDF(file_path)
        df = mdf.to_dataframe()
        return df
