import pandas as pd
import re

def parse_logs(file_path):
    print(f"--- Extraction des données du fichier : {file_path} ---")
    parsed_data = []

    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] "(?P<method>\w+) (?P<url>.*?) HTTP/.*?" (?P<status>\d+)'
    )
    
    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.search(line)
            if match:
                parsed_data.append(match.groupdict())
    
    df = pd.DataFrame(parsed_data)
    return df

if __name__ == "__main__":
    df_logs = parse_logs("sample_logs.txt")
    print("\n Voici vos données structurées prêtes à être analysées :")
    print(df_logs)