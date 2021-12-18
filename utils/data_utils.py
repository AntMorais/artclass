import pandas as pd
import numpy as np
import yaml 
import os

def read_class_txt(txt_file):
    # returns dictionary with key = id and value = label
    with open(txt_file) as f:
        lines = f.readlines()
        lines = [line.strip().split() for line in lines]
        classes_dict = dict(lines)
    return classes_dict 

if "__name__" == "__main__":
    path_to_class_info = "wikiart_csv"
    artist_class = read_class_txt(os.path.join(path_to_class_info, 'artist_class.txt'))
    genre_class = read_class_txt(os.path.join(path_to_class_info, 'genre_class.txt'))
    style_class = read_class_txt(os.path.join(path_to_class_info, 'style_class.txt'))
    yaml.dump("")
