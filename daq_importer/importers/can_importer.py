import pandas as pd
import can
from ..base_importer import BaseImporter

class CANImporter(BaseImporter):
    """Importer for CAN log files (.asc and .blf)."""

    def load(self, file_path: str) -> pd.DataFrame:
        """
        Load data from a CAN log file (.asc or .blf) into a pandas DataFrame.

        :param file_path: Path to the CAN log file.
        :return: DataFrame containing the extracted CAN messages.
        """
        try:
            messages = self._load_can_log(file_path)
            data = [
                {
                    "Timestamp": msg.timestamp,
                    "CAN_ID": msg.arbitration_id,
                    "DLC": msg.dlc,
                    "Data": " ".join(f"{byte:02X}" for byte in msg.data),
                }
                for msg in messages
            ]
            return pd.DataFrame(data)

        except Exception as e:
            raise ValueError(f"Error loading CAN file: {e}")

    def _load_can_log(self, file_path: str):
        """Load messages from an ASC or BLF log file using python-can."""
        with can.BLFReader(file_path) if file_path.endswith(".blf") else can.ASCReader(file_path) as log:
            return list(log)
