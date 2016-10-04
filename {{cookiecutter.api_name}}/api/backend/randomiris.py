# -*- coding: utf-8 -*-
import pandas as pd
import random
from api.models import Iris


class RandomIris(object):
    """
    Object that handles the random selection of 5 iris plants from the same class
    """

    def __init__(self):
        """
        Attributes
        ----------
        iris : pd.DataFrame
            Iris dataset
        """
        import os
        basedir = os.path.abspath(os.path.dirname(__file__))
        data_dir = '/'.join(basedir.split('/')[:-1] + ['data/iris.csv'])

        self.iris = pd.read_csv(open(data_dir, 'rb'), header=0)

    def get_rnd(self):
        """
        Selects randomly 5 iris from same class

        Returns
        -------
        result : pd.DataFrame
        """
        indexes = random.sample(range(0, 149), 5)
        sample_iris = self.iris.ix[indexes, :]

        result = []
        for row in sample_iris.iterrows():
            row_values = row[1].values
            result.append({'sepal_length': row_values[0],
                           'sepal_width': row_values[1],
                           'petal_length': row_values[2],
                           'petal_width': row_values[3],
                           'class': row_values[4]})

        return result
