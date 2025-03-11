import os

def get_file_extension(file_path: str) -> str:
    return os.path.splitext(file_path)[-1].lower()

def detect_importer(file_path: str):
    ext = get_file_extension(file_path)
    mapping = {
        ".mdf": "MDFImporter",
        ".mf4": "MDFImporter",
        ".asc": "CANImporter",
        ".blf": "CANImporter",
        ".tdms": "TDMSImporter",
        ".mat": "MATImporter",
        ".csv": "CSVImporter",
        ".xdf": "XDFImporter",
        ".pak": "PAKImporter",
        ".dxd": "DXDImporter",
    }
    return mapping.get(ext, None)
