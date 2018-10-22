import pandas as pd
import pickle
import os
import unicodedata
import Levenshtein

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

class GenderClassifier:

    def __init__(self):

        if not os.path.isfile('summary.p'):
            names_df = pd.read_csv('nomes.csv', delimiter=',')
            summary_df = names_df[['first_name', 'frequency_male', 'frequency_female', 'frequency_total', 'classification']]

            del names_df

            with open('summary.p', 'wb') as output:
                pickle.dump(summary_df, output)

            self.summary_df = summary_df
        else:
            with open('summary.p', 'rb') as input:
                self.summary_df = pickle.load(input)

    def _find_closest_name(self, name):
        max = len(name) * 2
        name_aux = ''
        for n in self.summary_df['first_name'].values.tolist():
            l = Levenshtein.distance(name, n)
            if l < max:
                max = l
                name_aux = n

        return name_aux
    def _sanitize(self, name):

        if ' ' in name:
            name = name.split(' ')[0]

        name = strip_accents(name).upper()

        if name not in self.summary_df['first_name'].values.tolist():
            name = self._find_closest_name()

        return name

    def get_gender(self, name):
        name = self._sanitize(name)
        gender = self.summary_df[self.summary_df['first_name'] == name]['classification'].values.tolist()[0]
        return gender

    def is_male(self, name):
        return self.get_gender(name) == 'M'

    def is_female(self, name):
        return self.get_gender(name) == 'F'

# classifier = GenderClassifier()
# print(classifier.get_gender('Gabriela'))
# print(classifier.is_female('Gabriela'))
# print(classifier.get_gender('Heriveltonn'))