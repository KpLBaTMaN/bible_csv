# Convert Bible Json to Database
import json
import pandas as pd
from os import listdir
from os.path import isfile, join

def read_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]
    

def main():
    """
    - Load json
    - Convert json to DataFrame
    - Export to csv
    """
    folder_path_read = "./jsonfiles/"
    folder_path_export = "./csvfiles/"
    data_files = read_files(folder_path_read)
    
    for file in data_files:
        print("loading: ", file)
        bible_path = f'{folder_path_read}{file}'
        bible_json = [json.loads(line) for line in open(bible_path,'r')]
        df_bible = pd.DataFrame(bible_json)
        print("exporting: ", file)
        df_bible.to_csv(f"{folder_path_export}{file}.csv")
        
    print("Exported to csv: ", data_files)
    print("Finished :)")
        
        

if __name__ == "__main__":
   main()

    