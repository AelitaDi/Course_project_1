import os
from unittest.mock import patch

import pandas as pd
from src.utils import get_data_from_excel


# PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tests", "test_operations.xlsx")


@patch("src.utils.pd.read_excel")
def test_get_data_from_excel(mock_read_excel, empty_df):
    mock_read_excel.return_value = empty_df
    assert get_data_from_excel("test.xlsx").equals(empty_df)
    mock_read_excel.assert_called_once_with("test.xlsx")
