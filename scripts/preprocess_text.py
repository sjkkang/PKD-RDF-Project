import os
import re
import json
from pathlib import Path

def clean_text(text):
    """Text cleaning function: Remove special characters and unnecessary whitespace"""
    text = re.sub(r'\s+', ' ', text)  # Remove multiple whitespace
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    return text.strip()

def preprocess_file(input_path, output_path):
    """Preprocess a single file and save"""
    with open(input_path, 'r', encoding='utf-8') as infile:
        text = infile.read()
    
    cleaned_text = clean_text(text)
    
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(cleaned_text)
    print(f"Processed: {input_path} -> {output_path}")

def preprocess_all(input_dir, output_dir):
    """Preprocess all files in data directory and save to new directory"""
    os.makedirs(output_dir, exist_ok=True)
    
    for file in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, file)
        if os.path.isfile(input_path):
            preprocess_file(input_path, output_path)
    
if __name__ == "__main__":
    input_directory = "data"
    output_directory = "data/processed"
    preprocess_all(input_directory, output_directory)
