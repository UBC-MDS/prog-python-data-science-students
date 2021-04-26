from hashlib import sha1
import pandas as pd
import pytest
import sys
from decimal import Decimal
import inspect
import altair as alt

def test_1a(answer):
    assert not answer is None, "Your function does not exist. Have you passed in the correct function?"
    str_fun = inspect.getsource(answer)
    assert "sample_dataframe" in str_fun, "Make sure you are naming your function 'sample_dataframe'."
    assert "data" in str_fun, "Make sure you are passing 'data' as an argument."
    assert "grouping_col" in str_fun, "Make sure you are passing 'grouping_col' as an argument."
    assert "N=1" in str_fun, "Make sure you making 'N=1' a default argument."
    return("Success")

def test_1b(answer, data):
    assert not answer is None, "Your function does not exist. Have you passed in the correct function?"
    str_fun = inspect.getsource(answer)
    assert "df_filterer" in str_fun, "Make sure you are naming your function 'df_filterer'."
    assert "data" in str_fun, "Make sure you are passing 'data' as an argument."
    assert "interest_column" in str_fun, "Make sure you are passing 'interest_column' as an argument."
    assert "value" in str_fun, "Make sure you are passing 'value' as an argument."
    assert "keep" in str_fun, "Make sure you are passing 'keep' as an argument."
    res = answer(data,'Alma Mater','University of Kansas', ['Name'])
    assert "Joe H. Engle" in list(res.Name), "Your function output is incorrect. Are you writing the function correctly?"
    return("Success")

def test_2a(answer):
    assert not answer is None, "Your function does not exist. Have you passed in the correct function?"
    str_fun = inspect.getsource(answer)
    assert "Parameters" in str_fun, "Make sure your docstring includes a 'Parameter' section"
    assert "data" in str_fun.lower(), "Make sure you are describing the 'data' argument in the docstring"
    assert "grouping_col" in str_fun.lower(), "Make sure you are describing the 'grouping_col' argument in the docstring"
    assert "N" in str_fun, "Make sure you are describing the 'N' argument in the docstring"
    assert "optional" in str_fun.lower(), "Make sure you are specifying that 'N' is optional"
    assert "Returns" in str_fun, "Make sure your docstring includes a 'Returns' section"
    assert "Examples" in str_fun, "Make sure your docstring includes an 'Examples' section"
    return("Success")


def test_3a(answer):
    assert not answer is None, "Your function does not exist. Have you passed in the correct function?"
    str_fun = inspect.getsource(answer)
    assert str_fun.count('raise') == 4, "Make sure your are raising exceptions for all four conditions"
    assert "TypeError" in str_fun, "Make sure you are raising a 'TypeError' for incorrect data types"
    assert "ValueError" in str_fun, "Make sure you are raising a 'ValueError' for incorrect values"
    assert "Exception" in str_fun, "Make sure you are raising an 'Excpetion' for non existent values"
    return("Success")

def test_3b(answer):
    assert not answer is None, "Your function does not exist. Have you passed in the correct function?"
    str_fun = inspect.getsource(answer)
    assert str_fun.count('raise') > 2, "Make sure you are adding at least three conditions"
    assert str_fun.count('if') > 2, "Make sure you are adding at least three conditions"
    return("Success")

def test_4a(answer):
    assert not answer is None, "Your dataframe does not exist. Have you passed in the correct dataframe?"
    assert answer.shape[0] < 20 and answer.shape[0] > 4, "Make sure the number of rows in your dataframe is between 5 and 20"
    assert answer.shape[1] < 10 and answer.shape[1] > 3, "Make sure the number of columns in your datafame is between 3 and 10"
    assert len(set(list(answer.dtypes))) > 1, "Make sure you are providing different data types to the columns in your dataframe"
    return("Success")

def test_5a(answer):
    assert sha1(str(answer + "5").encode('utf8')).hexdigest() == "d5183bf9332928633669d12c81fe3cda73996b19", "Your answer is incorrect. Please try again"
    return("Success")

def test_5c(answer):
    assert sha1(str(answer + "16").encode('utf8')).hexdigest() == "8dda9f6573d6e7b59c6ee869cd930d1e181b046d", "Your answer is incorrect. Please try again"
    return("Success")

def test_5d(answer):
    assert not answer is None, "Your function does not exist. Have you passed in the correct function?"
    str_fun = inspect.getsource(answer)
    assert "astronauts_stats" in str_fun, "Make sure you are naming your function 'astronauts_stats'"
    assert "parameters" in str_fun.lower(), "Make sure your docstring includes a 'Parameter' section"
    assert "returns" in str_fun.lower(), "Make sure your docstring includes a 'Returns' section"
    assert "examples" in str_fun.lower(), "Make sure your docstring includes an 'Examples' section"
    res = answer("Deceased")
    assert round(res) == 274, "Your function's output is incorrect. Are you writing the function properly?"
    return("Success")

def test_5e(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer + "26").encode('utf8')).hexdigest() == "9bd29e9018fb40e7e7beef564d296f5c26704785", "Your answer is incorrect. Please try again"
    return("Success")

def test_5f(answer1, answer2, data):
    assert not answer1 is None, "Your function does not exist. Have you passed in the correct function?"
    str_fun1 = inspect.getsource(answer1)
    str_fun2 = inspect.getsource(answer2)
    assert "filters_military_rank" in str_fun1, "Make sure you are naming your function 'filters_military_rank'"
    assert "parameters" in str_fun1.lower(), "Make sure your docstring for 'filters_military_rank' includes a 'Parameter' section"
    assert "returns" in str_fun1.lower(), "Make sure your docstring for 'filters_military_rank' includes a 'Returns' section"
    assert "examples" in str_fun1.lower(), "Make sure your docstring for 'filters_military_rank' includes an 'Examples' section"
    assert "filters_active_years" in str_fun2, "Make sure you are naming your function 'filters_active_years'"
    assert "parameters" in str_fun2.lower(), "Make sure your docstring for 'filters_active_years' includes a 'Parameter' section"
    assert "returns" in str_fun2.lower(), "Make sure your docstring for 'filters_active_years' includes a 'Returns' section"
    assert "examples" in str_fun2.lower(), "Make sure your docstring for 'filters_active_years' includes an 'Examples' section"
    arg1 = list(inspect.getargspec(answer1))[0]
    arg2 = list(inspect.getargspec(answer1))[0]
    assert len(arg1) > 0, "Make sure your 'filters_military_rank' is taking arguments"
    assert len(arg2) > 0, "Make sure your 'filters_active_years' is taking arguments"
    res1 = answer1(data, "Colonel")
    assert res1.shape == (93, 19), "The output for 'filters_military_rank' is incorrect. Are you filtering properly?"
    res2 = answer2(data, 1996, 2005)
    assert res2.shape == (88, 19), "The output for 'filters_active_years' is incorrrect. Are you setting up your conditionals properly?"
    return("Success")
