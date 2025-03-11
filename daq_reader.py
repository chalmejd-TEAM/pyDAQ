from .utils.file_utils import detect_importer
from .importers.mdf_importer import MDFImporter
from .importers.tdms_importer import TDMSImporter
from .importers.mat_importer import MATImporter
from .importers.csv_importer import CSVImporter


class DAQReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        importer_class = detect_importer(file_path)

        if importer_class:
            self.importer = globals()[importer_class]()
        else:
            raise ValueError(f"Unsupported file format: {file_path}")

    def load_data(self):
        return self.importer.load(self.file_path)
