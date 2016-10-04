# -*- coding: utf-8 -*-
from flask import jsonify, request, abort
from flask_restful import Resource

from api import api
from api.backend import randomiris
from api.constants import SUCCESS_REQUEST


class RandomIrisAPI(Resource):

    def __init__(self):
        """
        Endpoint for the random selection of iris plants based on class

        Attributes
        ----------
        class_iris : list
            Valid of Iris class
        """
        self.class_iris_list = ['Iris-setosa',
                                'Iris-versicolor',
                                'Iris-virginica']

    def get(self):
        """
        Get randomly 5 iris plants with same class

        Returns
        -------
        _ : JSON
            Request answer
        """
        # Get the dataframe with the sample
        results = randomiris.RandomIris().get_rnd()

        response = {'results': results,
                    'status': SUCCESS_REQUEST,
                    'method': 'GET',
                    'uri': '/api/v1/iris'}

        return jsonify(response)


api.add_resource(RandomIrisAPI, '/api/v1/iris', endpoint='iris')
