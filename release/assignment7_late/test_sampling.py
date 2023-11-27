import pandas as pd
# Import the function here

def test_sd_rows():
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
    
    # Tests that the expected number of rows and columns are correct
    assert sample_dataframe(helper_data, 'neighbourhood', 1).shape == (4, 5)
    return

def test_sd_groups():
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
    
    # Tests that the expected number of groups is 4
    assert sample_dataframe(helper_data, 'neighbourhood', 1).groupby('neighbourhood').ngroups == 4
    return


def test_sd_shape():
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
    
    sampler = sample_dataframe(helper_data, 'type', 3)
    
    # Tests the shape of the dataframe. There are only 6 rows, 3 for each tree type (Oak and Cherry) 
    assert sampler.shape == (6, 5), "The dataframe is not of the expected dimensions"
    return


def test_sd_2groups():
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
    
    sampler = sample_dataframe(helper_data, 'type', 3)
    
    # Tests that there are only 2 groups in the outputted dataframe
    assert sampler.groupby('type').ngroups == 2, "The dataframe should have 2 groups"
    return

def test_sd_oak():
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
    
    sampler = sample_dataframe(helper_data, 'type', 3)
    
    # Tests that there are only 3 rows that are of type "Oak"
    assert sampler[sampler['type'] == 'Oak'].shape[0] == 3, "The dataframe should only have 3 rows of type 'oak'"
    
    return

def test_sd_cherry():
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
    
    sampler = sample_dataframe(helper_data, 'type', 1)
    
    # Tests that there are only 1 row of type "Cherry"
    assert sampler[sampler['type'] == 'Cherry'].shape[0] == 3, "The dataframe should only have 1 row of type 'cherry'"
    
    return
