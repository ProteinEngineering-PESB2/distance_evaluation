import sys
print("Preparing imports")
sys.path.insert(0, '../')

from utils_module.utils_functions import utils_functions

fasta_data = sys.argv[1]
name_export = sys.argv[2]

utils_instance = utils_functions()
df_data = utils_instance.fasta_to_csv(fasta_data, '|')

utils_instance.export_csv(df_data, name_export)
