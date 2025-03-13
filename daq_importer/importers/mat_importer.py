import pandas as pd
import scipy.io
import h5py
from ..base_importer import BaseImporter


class MATImporter(BaseImporter):
    """Importer for MATLAB .mat files (supports v7.3+ and older versions)."""

    def load(self, file_path: str) -> pd.DataFrame:
        """
        Load data from a MATLAB .mat file into a pandas DataFrame.

        :param file_path: Path to the .mat file.
        :return: DataFrame containing the extracted data.
        """
        try:
            # Try loading with SciPy (works for v7.2 and older)
            try:
                mat_data = scipy.io.loadmat(file_path, struct_as_record=False, squeeze_me=True)
                return self._process_mat_data(mat_data)
            except NotImplementedError:
                pass  # If scipy fails, fall back to h5py

            # Use h5py for MATLAB v7.3+ files
            with h5py.File(file_path, "r") as mat_data:
                return self._process_hdf5_data(mat_data)

        except Exception as e:
            raise ValueError(f"Error loading MAT file: {e}")

    def _process_mat_data(self, mat_data: dict) -> pd.DataFrame:
        """Process MATLAB .mat data (v7.2 and older)."""
        cleaned_data = {k: v for k, v in mat_data.items() if not k.startswith("__")}
        df = pd.DataFrame({k: v.flatten() if hasattr(v, "flatten") else v for k, v in cleaned_data.items()})
        return df

    def _process_hdf5_data(self, mat_data: h5py.File) -> pd.DataFrame:
        """Process MATLAB v7.3+ HDF5 .mat data."""
        extracted_data = {}

        def extract_hdf5(name, obj):
            if isinstance(obj, h5py.Dataset):  # Only extract dataset objects
                extracted_data[name] = obj[()]

        mat_data.visititems(extract_hdf5)
        return pd.DataFrame.from_dict(extracted_data, orient="columns")

