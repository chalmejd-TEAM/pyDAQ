import unittest
from importers.mdf_importer import MDFImporter

class TestMDFImporter(unittest.TestCase):
    def test_load(self):
        importer = MDFImporter()
        df = importer.load("sample.mdf")
        self.assertIsInstance(df, pd.DataFrame)

if __name__ == "__main__":
    unittest.main()
