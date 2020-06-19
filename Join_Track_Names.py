import pandas as pd
import sys

def output_track_name(filename: str):
    df = pd.read_csv(filename)
    romaji_list = list(df['Romaji'])
    english_list = list(df['English'])
    temp_drop_ext = filename.split(".")
    output_name = ".".join(temp_drop_ext[:-1])

    if(len(romaji_list) != len(english_list)):
        print("ERROR: Mismatch between Romaji and English list names. If a name is meant to be empty please indicate with \"-\".")
        quit(code=1)

    output_file = open(f"{output_name}.txt", "w")
    for idx in range(len(romaji_list)):
        romaji_name = romaji_list[idx].strip()
        english_name = english_list[idx].strip()
        track_name = f"{romaji_name} ({english_name})\n"
        output_file.write(track_name)
    
    print(f"Romaji/English track names from {filename} combined in {output_name}.txt")

def output_track_names():
    file_list = sys.argv
    del file_list[0] # remove csv_to_comma_txt.py from args

    if len(file_list) < 1:
        error = (
            f"ERROR: please specify which .csv files to process\n"
            f"Correct usage: python3 {__file__} \"bloom_into_you_names.csv\" \"Love Live names.csv\""
        )
        print(error)
        return

    for file_name in file_list:
        output_track_name(file_name)

if __name__ == "__main__":
    output_track_names()