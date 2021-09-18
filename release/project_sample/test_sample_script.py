#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:45:43 2020

@author: Elijah Willie

This function creates a helper data to test the sample script created for 
the sample solution to the Python Programmign for Data Science project.
"""

from sample_script import custom_agg
import pandas as pd

def test_custom_agg():

    # Create helper data and write tests for the function
    raw = {'id': [1873, 4913, 4801, 4540, 3581,
                   4534, 1934, 4944, 1983, 1266], 
           'name': ['English Oak', 'Higan Cherry', 'Willow Oak', 
                    'Yoshino Cherry', 'Red Oak', 'Kindred Spirit Oak',
                    'Garry Oak', 'Accolade Cherry', 'Snow Goose Cherry',
                    'Evergreen Oak'], 
            'neighbourhood': ['Sunset','West end','Kitsilano', 'Sunset', 
                              'Arbutus-ridge','Arbutus-ridge', 'Kitsilano', 
                              'West end','Kitsilano', 'Arbutus-ridge'],
            'type': ['Oak', 'Cherry', 'Oak', 'Cherry', 'Oak',
                     'Oak', 'Oak', 'Cherry', 'Cherry', 'Oak'],
            'diameter': [9.0, 27.0, 3.0, 22.0, 3.0,
                         6.5, 12.0, 18.0, 8.5, 23.0]}

    helper_data = pd.DataFrame.from_dict(raw)

    res = custom_agg(helper_data, 'type', 'name')

    assert res.shape == (2,2)
    assert list(res['count']) == [4, 6]
    assert list(res['type']) == ['Cherry', 'Oak']