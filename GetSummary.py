import os
import pandas as pd
import pickle

if not os.path.isfile('summary.p'):

    names_df = pd.read_csv('nomes.csv', delimiter=',')

    summary_df = names_df[
        ['first_name', 'frequency_male', 'frequency_female', 'frequency_total', 'classification']]

    summary_df.set_index('first_name', inplace=True)

    with open('summary.p', 'wb') as output:
        pickle.dump(summary_df, output)