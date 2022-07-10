import os
import pathlib
import pandas as pd

root_dir = "data"

def txt_to_csv(path: str, saving_dir="new_csv_data", engine="python"):
    """
    Args:
        path (str): root path of the .txt files you want to decode them to csv
        saving_dir (str, optional): dir where the new .csv file are going to be saved.
                                    Defaults to "new_csv_data".
                                    
        engine (str, optional): due to tokenizing error the engine must be python
    """
    
    path = pathlib.Path(path)
    save = pathlib.Path(saving_dir)
    for i, file in enumerate(pathlib.Path.iterdir(path)):
        df = pd.read_csv(file,sep='delimiter', header=None, engine=engine)
        s = os.path.join(save, f"one_{i}.csv")
        df.to_csv(s)
        
if __name__ == "__main__":
    txt_to_csv(root_dir)