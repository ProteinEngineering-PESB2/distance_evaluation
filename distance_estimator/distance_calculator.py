from utils.utils_function import utils_functions
from joblib import Parallel, delayed

class distance_estimator(object):

    def __init__(self,
                 dataset,
                 type_distance,
                 constant_instance):

        self.dataset = dataset
        self.type_distance = type_distance
        self.constant_instance = constant_instance

    def __get_row(self, index_data):
        row = [self.dataset[column][index_data] for column in self.dataset.columns if column not in ['seq', 'id']]
        return row

    def __distance_sequence_to_all(self, index_data):

        row_target = self.__get_row(index_data)
        distance_values = []

        for i in range(len(self.dataset)):
            if i != index_data:
                row_evaluate = self.__get_row(i)
                distance_value = utils_functions().get_distance_vectors(row_target, row_evaluate, self.type_distance)
                row_value = [self.dataset['id1'][index_data], self.dataset['id2'][i], distance_value]
                distance_values.append(row_value)
        return distance_values

    def generate_matrix_distance(self):

        print("Start distance calculator")
        response_distance = Parallel(n_jobs=self.constant_instance.n_cores, require='sharedmem')(delayed(self.__distance_sequence_to_all)(i) for i in range(len(self.dataset)))
        print(response_distance)

        return 0
