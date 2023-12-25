from pydantic import BaseModel
import pandas as pd

class DataSetName(BaseModel):
    name:str

def get_data_from_CSV(dataset_name:DataSetName)->pd.DataFrame:
    try:
        df = pd.read_csv(f"data/{dataset_name.name}.csv")
        return df
    except Exception as e:
        raise Exception(f"An error occurred when reading the dataset:{e}")
    