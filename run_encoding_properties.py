import pandas as pd
import argparse
import os

# console params sections, use argparse to process input console line
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataset", help="input dataset in csv format to encoding sequences", required=True)
parser.add_argument("-e", "--encoders", help="input dataset with clustered encoders", required=True)
parser.add_argument("-p", "--path", help="Path export to save encoding results", required=True)
parser.add_argument("-f", "--fft", help="Use FFT 1, 0 not use FFT", choices=[0, 1], default=0, type=int)
parser.add_argument("-g", "--group_id", help="Group ID to use as encoder property",
                    choices=['Group_0', 'Group_1', 'Group_2', 'Group_3', 'Group_4', 'Group_5', 'Group_6', 'Group_7'],
                    default='Group_0')

# compile
args = parser.parse_args()

# get values in variables
dataset = pd.read_csv(args.dataset)
dataset_encoders = pd.read_csv(args.encoders)
path_export = args.path
use_fft = args.fft
group_id = args.group_id

dict_encoder = {}
for i in range(len(dataset_encoders['residue'])):
    dict_encoder.update({dataset_encoders['residue'][i]: i})

print("Creating directory")
command = "mkdir {}encoding_{}".format(path_export, group_id)
print(command)
os.system(command)
