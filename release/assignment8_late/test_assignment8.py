from hashlib import sha1
import pandas as pd
import pytest
import sys
from decimal import Decimal
import numpy as np
import inspect


def test_1a(answer):
    assert not answer is None, "Your object does not exist. Have you passed in the correct object?"
    assert answer.size == 3, "Your array has the incorrect size. Are you slicing properly?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "3e1a4e12e3ba7129bcd27422d6a77dbb57ec68de", "Your array values are incorrect. Are you slicing properly?"
    return("Success")

def test_1b(answer):
    assert not answer is None, "Your object does not exist. Have you passed in the correct object?"
    assert 'numpy.ndarray' in str(type(answer)), "Your object is not of type 'numpy.ndarray'. Are you using the 'np.full()' function?"
    assert answer.shape == (2,2), "Your array dimensions are incorrect. Make sure you are creating a '2x2' array"
    assert str(answer.dtype) == 'float64', "Make sure your array is filled with floating point values."
    assert np.count_nonzero(answer == 3.4) == 4, "Your array values are incorrect. Make sure you are filling it with 3.4"
    return("Success")

def test_1c(answer):
    assert not answer is None, "Your object does not exist. Have you passed in the correct object?"
    assert 'numpy.ndarray' in str(type(answer)), "Your object is not of type 'numpy.arrary'. Are you using the 'np.full()' function?"
    assert answer.shape == (2, 3, 4), "Your array dimensions are incorrect. Make sure you are creating a '2x3X4' array"
    assert str(answer.dtype) == 'float64', "Make sure your array is filled with floating point values."
    assert np.count_nonzero(answer == 1) == 24.0, "Your array values are incorrect. Make sure you are using the 'np.ones()' function"
    return("Success")

def test_2a(answer):
    assert not answer is None, "Your object does not exist. Have you passed in the correct object?"
    assert answer.shape == (569, 20), "Your dataframe dimensions are incorrect. Are you reading in the correct dataframe?"
    assert str(answer['air_date'].dtype) == 'datetime64[ns]', "The 'air_date' column is of the incorrect type. Are you parsing it as dates?"
    return("Success")

def test_2c(answer):
    assert not answer is None, "Your object does not exist. Have you passed in the correct object?"
    assert answer.shape == (568,), "Your object dimensions are incorrect. The number of intervals should be 568. You may need to omit that NaT value we discussed."
    assert str(answer.dtype) == 'timedelta64[ns]', "Your object is of the incorrect data type. Are you parsing it as dates?"
    assert str(sum(answer.values)) == '364089600000000000 nanoseconds', "Some values in your object are incorrect."
    return("Success")

def test_2d(answer):
    assert not answer is None, "Your object does not exist. Have you passed in the correct object?"
    assert sha1(str(round(answer,2)).encode('utf8')).hexdigest() == "bc0d5950400d4df7183f1f23d44ed27def3095df", "Your answer is incorrect. Please try again. You may want to use a 'for' loop for this."
    return("Success")

def test_2e(answer):
    assert not answer is None, "Your object does not exist. Have you named your dataframe correctly?"
    assert str(answer['weekday_aired'].dtype) == 'object', "The 'weekday_aired' colum is of the incorrect data type. Are you using the 'dt.day_name()' function?"
    assert set(answer['weekday_aired']) == {'Monday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday'}, "The 'weekday_aired' colum has incorrect values. Are you using the 'dt.day_name()' function?"
    return("Success")

def test_2f(answer):
    assert not answer is None, "Your object does not exist. Have you passed in the correct object?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "215bb47da8fac3342b858ac3db09b033c6c46e0b", "Your answer is incorrect.\
    Are you summing up all rows with a 'weekday_aired ' column value of Tuesday?"
    return("Success")

def test_2g(answer):
    assert not answer is None, "Your object does not exist. Have you passed in the correct object?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "77de68daecd823babbb58edb1c8e14d7106e83bb", "Your answer is incorrect. Are you grouping by a column? Are you using a 'for' loop?\
    The '.min() and .max() functions may be useful here."
    return("Success")

def test_3(answer,dirty,clean):
    assert not answer is None, "Your function does not exist. Have you passed in the correct function?"
    str_fun = inspect.getsource(answer)
    assert "fillna" in str_fun, "Make sure you are replacing the missing values."
    assert "str.strip()" in str_fun, "Make sure you are removing unwanted whitespaces."
    assert "assign" in str_fun, "Make sure that when fixing columns, you are assigning it a column name."
    assert "Ivoire" in str_fun, "Make sure you are fixing the names of countries."
    assert "China" in str_fun, "Make sure you are fixing the names of countries."
    res = answer(dirty)
    assert res.equals(clean), "Your function output is incorrect. Make sure you are cleaning the dataframe."
    return("Success")


def test_2g(answer):
    assert not answer is None, "Your object does not exist. Have you passed in the correct object?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "77de68daecd823babbb58edb1c8e14d7106e83bb", "Your answer is incorrect. Please try again"
    return("Success")
