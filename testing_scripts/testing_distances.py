import pandas as pd
import sys
print("Preparing imports")
sys.path.insert(0, '../')

from distance_estimator.distance_calculator import distance_estimator
from utils_module.constant_values import constant_values

print("Console params")
input_data = pd.read_csv(sys.argv[1])
path_export = sys.argv[2]
column_with_response = sys.argv[3]
column_with_id = sys.argv[4]

distance_instance = distance_estimator(input_data,
                                       1,
                                       constant_values(),
                                       column_with_response,
                                       column_with_id)

name_export = "{}distance_evaluation.csv".format(path_export)
distance_instance.generate_matrix_distance(name_export=name_export,
                                           is_export=True)
