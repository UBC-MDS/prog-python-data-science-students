from hashlib import sha1
import pandas as pd
import pytest
import sys
from decimal import Decimal


def test_3b(answer1,answer2):
    assert not answer1 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not answer2 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer1, int),  str(answer1) + \
        " should be expressed as an integer"
    assert isinstance(answer2, int),  str(answer2) + \
        " should be expressed as an integer"
    assert sha1(str(answer1 + 9).encode('utf8')).hexdigest(
    ) == 'a72b20062ec2c47ab2ceb97ac1bee818f8b6c6cb', "Your answer is incorrect. seconds_in_a_minute should exist and have the value of how many seconds are in a minute.'" # we hid the answer to the test here so you can't see it, but we can still run the test
    assert sha1(str(answer2 + 7).encode('utf8')).hexdigest(
    ) == '85ecc3db0f2f59a5c1108559f249a92aa5c2007b', "Your answer is incorrect. seconds_in_a_hour should exist and have the value of how many seconds are in a hour." # we hid the answer to the test here so you can't see it, but we can still run the test
    return "Success"


def test_4a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, str), str(answer) + \
        " should be expressed as a string"
    assert sha1(str(answer).encode('utf8')).hexdigest(
    ) == '02b7558df1cdf9e9ee01b0cf4e37ac518a80eec1', "Your answer is incorrect." # we hid the answer to the test here so you can't see it, but we can still run the test
    return "Success"


def test_4b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, int), str(answer) + \
        " should be expressed as a integer"
    assert sha1(str(answer +12).encode('utf8')).hexdigest(
    ) == 'fa35e192121eabf3dabf9f5ea6abdbcbc107ac3b', "Your answer is incorrect." # we hid the answer to the test here so you can't see it, but we can still run the test
    return "Success"

def test_5a(answer):
    assert 'pandas' in sys.modules, "Solution is incorrect, the pandas package needs to be imported. Try doing this with the import function."
    assert "pd" in answer, "Don't forget to use the pd alias when importing the pandas package!"
    assert "pd" in globals() , "Don't forget to use the pd alias when importing the pandas package!"
    return "Success"

def test_6b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    answer = answer.upper()
    assert sha1(str(answer).encode('utf8')).hexdigest(
    ) == '32096c2e0eff33d844ee6d675407ace18289357d', "Your answer is incorrect." # we hid the answer to the test here so you can't see it, but we can still run the test
    return "Success"


def test_7a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, type(pd.DataFrame())), str(answer) + \
        " should be a pandas dataframe"
    assert len(answer) == 1833, "the number of rows in the dataframe should be 1833"
    assert len(answer.columns) == 6, "the number of columns in the dataframe should be 6. \n Did you load it properly?"
    assert sorted(list(answer.columns.values)) == ['age',
                                                   'bmi',
                                                   'km10_time_minutes',
                                                   'km10_time_seconds',
                                                   'km5_time_seconds',
                                                   'sex'], "At least one column name is not matching the original dataframe"
    assert round(answer['bmi'].sum(), 2) == 43594.45,  "Your dataframe has the wrong summed values for the bmi column."
    assert sha1(str(round(answer['age'].sum(), 1)).encode('utf8')).hexdigest() == '1abebafd12eaadc0c94d49614e8051372963fb2d', "Your dataframe has the wrong summed values for the age column."
    return("Success")

def test_7b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, type(pd.DataFrame())), str(answer) + \
        " should be a pandas dataframe"
    assert len(answer) == 1141, "the number of rows in the dataframe should be 1141"
    assert len(answer.columns) == 6, "the number of columns in the dataframe should be 6. \n Did you load it properly?"
    assert sorted(list(answer.columns.values)) == ['age',
                                                   'bmi',
                                                   'km10_time_minutes',
                                                   'km10_time_seconds',
                                                   'km5_time_seconds',
                                                   'sex'], "At least one column name is not matching the original dataframe"
    assert round(answer['bmi'].sum(), 2) == 27488.71,  "Your dataframe has the wrong summed values for the bmi column."
    assert sha1(str(round(answer['age'].sum(), 1)).encode('utf8')).hexdigest() == '9cd3f6a7f84c7f0b6d89323f8d0dc521b5898fe4', "Your dataframe has the wrong summed values for the age column."
    return "Success"

def test_7d(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer) == 8, "the number of rows in the dataframe should be 8"
    assert sorted(list(answer.index)) == ['25%', '50%', '75%', 'count', 'max', 'mean', 'min', 'std'], "At least one index label is not matching the describe indices"
    assert sha1(str(round(answer['bmi']['mean'], 1)).encode('utf8')).hexdigest() == '9ab751fe3fe3a85f1ff10576a722069be9958997', "Your describe method was not conducted properly. The mean of `key` feature is not correct."
    assert answer.loc['max'].sum() == 9106.75645447, "This dataframe may not have been made will all the rows of the male runners"
    assert sha1(str(round(answer['age']['min'], 1)).encode('utf8')).hexdigest() == 'a99f1dbbfe0c91ea18cfffda9d7c8a31427e101b', "Your describe method was not conducted properly. The min value of `loudness` feature is not correct."
    assert sha1(str((round(answer['km10_time_seconds']['max'], 1))).encode('utf8')).hexdigest() == 'b2811a96a671a1f24dd204f2e0bab2e0eaca6320', "Your describe method was not conducted properly. The max value of `tempo` feature is not correct."
    return "Success"


def test_7e_i(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, float), str(answer) + \
        "Are you putting quotes around a number "
    assert sha1(str(round(answer + 12, 2)).encode('utf8')).hexdigest(
    ) == '8e4c10625cab06ee6b1b3592c401e3b3a6cf11ff', "Your answer is incorrect. You should indicate the index corresponding to the wrongly labled sample"
    return "Success"

def test_7e_iii(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, float), str(answer) + \
        " Are you putting quotes around a number? Are you not expressing your answer as a whole number?"
    assert sha1(str(answer).encode('utf8')).hexdigest(
    ) == '9621d5227eedf02a0ae0762647b6693054a8b9ab', "Your answer is incorrect. You should indicate the index corresponding to the wrongly labled sample"
    return "Success"

def test_7e_iv(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, float), str(answer) + \
        " Are you putting quotes around a number?"
    assert sha1(str(round(answer + 3, 2)).encode('utf8')).hexdigest(
    ) == '379ce184d6c8976597799239018a7a63b8875e81', "Your answer is incorrect. You should indicate the index corresponding to the wrongly labled sample"
    return "Success"

def test_7f(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer) == 56, "the number of rows in the object should be 56"
    assert round(answer.sum(), 2) == 1141,  "Your dataframe has the wrong summed values for the freq column." 
    return "Success"

def test_7g(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == "bar", "Your plot is not a histogram. Make sure you are using the 'mark_bar()' function"
    assert answer.mark.color == "lightsteelblue", "Make sure you are using the 'color' argument in the 'mark_bar' function to set the color to 'lightsteelblue'."
    assert answer.encoding.x.bin.maxbins == 25, "Make sure you are setting the 'maxbins = 25'"
    assert str(answer.encoding.x.shorthand) == 'bmi' or str(answer.encoding.x.field) == 'bmi', "Make sure you are plotting the `bmi` variable."
    assert answer.title == 'Distribution of Male Runners BMI', "Make sure you are providing the correct title for the plot."
    return "Success"

def test_7h(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.mark.type == "circle", "Your plot is not a histogram. Make sure you are using the 'mark_circle' function"
    assert answer.mark.color == "slateblue", "Make sure you are using the 'color' argument in the 'mark_circle' function to set the color to 'slateblue'."
    assert answer.mark.opacity == 0.3, "Make sure you are using the 'opacity' argument in the 'mark_circle' function to set the opacity to 0.3."
    assert answer.mark.size == 12, "Make sure you are using the 'size' argument in the 'mark_circle' function to set the size to 12."
    assert str(answer.encoding.x.shorthand) == 'bmi' or str(answer.encoding.x.field) == 'bmi', "Make sure you are plotting the `bmi` variable on the x-axis."
    assert str(answer.encoding.y.shorthand) == 'km10_time_minutes' or str(answer.encoding.y.field) == 'km10_time_minutes', "Make sure you are plotting the `km10_time_minutes` variable. on the y-axix"
    assert answer.title == 'Relationship between BMI and 10k running time (mins)', "Make sure you are providing the correct title for the plot."
    return "Success"


def test_7i(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert isinstance(answer, str), "Are you putting your answer in quotations?"
    assert answer.isupper() == True, "Are you expressing you solution in uppercase?"
    assert sha1(str(answer + "X").encode('utf8')).hexdigest(
    ) == 'fe09563e3a1b9f78674fe92fcb5b526a1b9353d8', "Your answer is incorrect. You should indicate the index corresponding to the wrongly labled sample"
    return "Success"
