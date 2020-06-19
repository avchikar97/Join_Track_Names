# Join_Track_Names

A quick Python script to combine Romaji and English track names to reduce the amount of copy-pasting. Combines the track names on a single line with format "{romaji_name} ({english_name})" and outputs to a file of the same input name except with a .txt extension.

bloom_into_you_names.csv is an example of proper input and bloom_into_you_names.txt is an example of the script output.

### Requirements
- python 3.6+ (can be installed [here](https://www.python.org/downloads/))
- pip3
- pandas

### Steps to run:
1. Run `pip3 install -r requirements.txt` to install required packages
2. Run `python3 csv_to_comma_txt.py "bloom_into_you_names.csv" "Love Live names.csv"` --- the script can take as many CSVs as you want (minimum 1)
3. Observe output in bloom_into_you_names.txt and Love Live names.txt
