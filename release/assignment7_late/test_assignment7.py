from hashlib import sha1
import pytest
import sys
from decimal import Decimal
import inspect
import os


def test_1a(answer):
    assert 'pandas' in sys.modules, "Solution is incorrect, the pandas library needs to be imported. Try doing this with the import function."
    assert "pd" in answer, "Don't forget to use the pd alias when importing the pandas library!"
    return("Success")

def test_1b(answer):
    assert 'altair' in sys.modules, "Solution is incorrect, the altair library needs to be imported. Try doing this with the import function."
    return("Success")

def test_1c():
    assert 'numpy' in sys.modules, "Make sure you are importing the 'arrange()' function from the 'numpy' module."
    return("Success")

def test_2a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (569, 20), "The dimensions of your dataframe are incorrect. Are you reading in the correct dataframe?"
    assert sorted(list(answer.columns))[0:4] == ['air_date', 'appetizer', 'contestant1', 'contestant1_info'], "Your dataframe contains the incorrect columns. \
                                                                                                                Are you reading in the correct dataframe?"
    return("Success")

def test_2b(answer):
    assert 'sampling' in sys.modules, "Make sure you are importing the 'sampling' file."
    assert "sample_dataframe" in answer, "Are you importing the sample_dataframe function from 'sampling' library?"
    return("Success")

def test_2d(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + '5').encode('utf8')).hexdigest() == "7c0575c87e8cae6ca0bb863db72413e54e32308c","Your answer is incorrect. Please try again."
    return("Success")

def test_2e(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + '7').encode('utf8')).hexdigest() == "16f9985e19e4d784492f2cb20746436b0364cfbb", "Your answer is incorrect. Please try again."
    return("Success")

def test_2f(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (90, 20), "The dimensions of your dataframe are incorrect. Are sampling only two rows from the dataframe?"
    temp = list(answer.groupby('season')['season'].count())
    res = {i:temp.count(i) for i in temp}   
    assert 2 in res.keys(), "Make sure you are sampling only two rows from each season"
    assert 45 in res.values(), "Make sure you are sampling only two rows from each season"
    assert sorted(list(answer.columns))[0:4] == ['air_date', 'appetizer', 'contestant1', 'contestant1_info'], "Your dataframe contains the incorrect columns. \
                                                                                                                Are you shuffling the correct dataframe?"
    return("Success")

def test_3a():
    with open("test_sampling.py") as fp:
        for i, line in enumerate(fp):
            if i == 1:
                break
    assert "sampling" in str(line), "Make sure you are importing from the 'sampling.py' file on line 2"
    assert "sample_dataframe" in str(line), "Make sure you are importing the 'sample_dataframe' function from the 'sampling.py' file on line 2"
    assert "from" in str(line), "Make sure you are using the correct keywords for importing"
    return("Success")

def test_3bi(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "ac3478d69a3c81fa62e60f5c3696165a4e5e6ac4", "Your answer is incorrect. Are you counting properly."
    return("Success")

def test_3biii(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower()).encode('utf8')).hexdigest() == "8af91746b2bc0f564a8d9fe1fb3294be0dc7519e", "Your answer is incorrect. Are you sure you have the right test name? Are your spelling the test properly?"
    return("Success")

def test_4ai(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer + 15).encode('utf8')).hexdigest() == "bc33ea4e26e5e1af1408321416956113a4658763", "Your answer is incorrect. Check in the output flake8 again."
    return("Success")

def test_4aii(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer + 9).encode('utf8')).hexdigest() == "b1d5781111d84f7b3fe45a0852e59758cd7a87e5", "Your answer is incorrect. Please try again."
    return("Success")

def test_4aiii(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + '17').encode('utf8')).hexdigest() == "80db3577882af5eb37c0a9a61e8e027f61997b92", "Your answer is incorrect. Please try again."
    return("Success")

def test_4b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + 'k').encode('utf8')).hexdigest() == "b86f6db284d374188d561d46b45b188d5631609a", "Your answer is incorrect. Please try again."
    return("Success")

def test_5a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + '8').encode('utf8')).hexdigest() == "b6485633f4901443360d61967ca307d7257f7dd9", "This isn't the best fitting name, can you find a better one?"
    return("Success")

def test_5b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer.lower() + '0').encode('utf8')).hexdigest() == "98c4c237274ca567cccd6a842a950919ca9e6a63", "This isn't the best fitting name, can you find a better one?"
    return("Success")

def test_5d(answer):
    assert not answer is None, "Your function does not exist. Make sure you don't change the name of the function given."
    str_fun = inspect.getsource(answer)
    assert "histogram_plot_of_column_name" not in str_fun, "Are you sure that 'histogram_plot_of_column_name' is a proper variable name?"
    assert "cs" not in str_fun, "Are you sure that 'cs' is a proper variable name?"
    assert "it could be useful" not in str_fun, "Make sure you are keeping only informative comments"
    assert "This function now returns a histogram" not in str_fun, "Make sure you are keeping only informative comments"
    return("Success")

