# -*- coding: utf-8 -*-
from api import db


class Iris(db.Model):
    """
    Iris plants model
    """
    __tablename__ = 'iris'

    id = db.Column(db.Integer, primary_key=True)
    sepal_length = db.Column(db.Float)
    sepal_width = db.Column(db.Float)
    petal_length = db.Column(db.Float)
    petal_width = db.Column(db.Float)
    class_plant = db.Column(db.String)

    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, class_plant):
        """
        Parameters
        ----------
        sepal_length : float 
            Define the sepal length of the iris plant
        sepal_width : float
            Define the sepal width of the iris plant
        petal_length : float
            Define the petal length of the iris plant
        petal_width : float
            Define the petal width of the iris plant
        class_plant : string
            Define the class of the iris plant

        Atributes
        ---------
        sepal_length : float 
            Sepal length of the current iris plant
        sepal_width : float
            Sepal width of the current iris plant
        petal_length : float
            Petal length of the current iris plant
        petal_width : float
            Petal width of the current iris plant
        class_plant : string
            Class of the current iris plant
        """
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.class_plant = class_plant

    def __repr__(self):
        """
        Get the iris sepal/petal/class information

        Returns
        -------
        _ : string
            Current iris plant basic information
        """
        iris_info = 'septal-length: %.1f, septal-width: %.1f, petal-width: %.1f'\
                    'petal-length: %.1f, class: %s'
        return iris_info % (self.sepal_length, sepal_width,
                            self.petal_length, self.petal_width,
                            self.class_plant)
