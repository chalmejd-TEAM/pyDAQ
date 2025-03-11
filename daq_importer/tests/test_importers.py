import unittest
from daq_importer.importers.mdf_importer import MDFImporter
import pandas as pd

class TestMDFImporter(unittest.TestCase):
    def test_load(self):
        importer = MDFImporter()
        df = importer.load("sample.mdf")
        self.assertIsInstance(df, pd.DataFrame)

if __name__ == "__main__":
    unittest.main()
