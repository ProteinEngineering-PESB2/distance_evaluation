import sys
import pandas as pd

print("Preparing imports")
sys.path.insert(0, '../')

from encoding_sequences.physicochemical_properties import physicochemical_encoder
from utils_module.constant_values import constant_values

# console params
print("Get params by console")
dataset = pd.read_csv(sys.argv[1])
dataset = dataset[:100]
property_to_use = sys.argv[2]
encoders = pd.read_csv(sys.argv[3])
encoders.index = encoders['residue']

path_export = sys.argv[4]
column_with_seq = sys.argv[5]
column_with_response = sys.argv[6]
column_with_id = sys.argv[7]

print("Instance object")
encoding_instance = physicochemical_encoder(dataset,
                 property_to_use,
                 encoders,
                 constant_values(),
                 column_with_seq,
                 column_with_id,
                 column_with_response)

print("Start encoding process")
name_export = "{}{}_encoding.csv".format(path_export, property_to_use)
is_export = True

encoding_instance.encoding_dataset(
    name_export,
    is_export)

print("End script")
