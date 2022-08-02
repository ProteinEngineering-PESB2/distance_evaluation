from scipy.fft import fft
import pandas as pd
import numpy as np

class physicochemical_encoder(object):

    def __init__(self, dataset, encoder, n_cores, dict_encoder):
        self.dataset = dataset
        self.encoder = encoder
        self.n_cores = n_cores
        self.dict_encoder = dict_encoder

    def __encoding_one_sequence(self, sequence):

        array_response = []
        sequence = sequence.upper()
        for residue in sequence:
            try:
                value_encode = self.encoder[self.dict_encoder[residue]]
                array_response.append(value_encode)
            except:
                pass
        return array_response

    def __apply_fft_data(self, row, number_sample):
        T = 1.0 / float(number_sample)
        x = np.linspace(0.0, number_sample * T, number_sample)
        yf = fft(row)
        xf = np.linspace(0.0, 1.0 / (2.0 * T), number_sample // 2)
        yf = np.abs(yf[0:number_sample // 2])
        return xf, yf

    def encoding_process(self):

        matrix_encoder = []
        length_values = []
        response_data = []
        for i in range(len(self.dataset)):
            # name columns define in dataset
            sequence = self.dataset['seq'][i]
            response = self.dataset['response'][i]
            vector_encoder = self.__encoding_one_sequence(sequence)
            matrix_encoder.append(vector_encoder)
            length_values.append(len(vector_encoder))
            response_data.append(response)

        # apply zero-padding
        max_lenght = max(length_values)
        for i in range(len(matrix_encoder)):
            length_data = matrix_encoder[i]
            for j in range(len(length_data), max_lenght):
                matrix_encoder[i].append(0)

        header = ["p_{}".format(i) for i in range(0, max_lenght)]
        df_data = pd.DataFrame(matrix_encoder, columns=header)
        df_data['response'] = response_data
        return df_data

