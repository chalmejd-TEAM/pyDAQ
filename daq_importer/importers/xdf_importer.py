import pandas as pd
import pyxdf
from ..base_importer import BaseImporter


class XDFImporter(BaseImporter):
    """Importer for AVL XDF files."""

    def load(self, file_path: str) -> pd.DataFrame:
        """
        Load data from an AVL XDF file into a pandas DataFrame.

        :param file_path: Path to the .xdf file.
        :return: DataFrame containing the extracted signals.
        """
        try:
            streams, _ = pyxdf.load_xdf(file_path)

            # Flatten the XDF structure into a single DataFrame
            data = {}
            for stream in streams:
                name = stream.get("name", f"Stream_{len(data)}")
                time_series = stream["time_series"]
                timestamps = stream["time_stamps"]

                # Store each stream in a separate column
                for i, signal in enumerate(zip(*time_series)):
                    col_name = f"{name}_Signal_{i}"
                    data[col_name] = signal
                data[f"{name}_Timestamps"] = timestamps

            return pd.DataFrame(data)

        except Exception as e:
            raise ValueError(f"Error loading XDF file: {e}")
