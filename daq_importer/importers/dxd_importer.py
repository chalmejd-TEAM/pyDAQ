import dwdatareader as dw
import pandas as pd
from ..base_importer import BaseImporter

class DXDImporter(BaseImporter):
    def load(self, file_path: str) -> pd.DataFrame:
        with dw.open(file_path) as dataFile:
            channel_list = [channel for channel in dataFile]
            df = dataFile.dataframe(channel_list)
        return df
