from nptdms import TdmsFile
import pandas as pd
from ..base_importer import BaseImporter

class TDMSImporter(BaseImporter):
    def load(self, file_path: str) -> pd.DataFrame:
        tdms_file = TdmsFile.read(file_path)
        data = {group.name: group.as_dataframe() for group in tdms_file.groups()}
        return pd.concat(data.values(), axis=1)
