from hashlib import sha1
import pandas as pd
import altair as alt
import pytest
import sys
from decimal import Decimal


def test_1a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 5 and answer.shape[1] == 6, "Your dataframe dimensions are incorrect. Are you using the read_csv function?"
    msg = "Your dataframe contains the incorrect columns. Are you using the correct index column? \
    \nExpected ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour','Aroma'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour', 'Aroma']), msg
    assert "Chardonnay" in list(
        answer.Grape
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.Alcohol)
    ) == 69.33, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return ("success")

def test_1b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 5 and answer.shape[1] == 6, "Your dataframe dimensions are incorrect. Are you using the read_csv or read_excel function to load the data?"
    msg = "Your dataframe contains the incorrect columns. Are you using the correct header argument? \
    \nExpected ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour','Aroma'], but got {0}".format(
        list(answer.columns))
    assert list(answer.columns) == [
        'Grape', 'Origin', 'Alcohol', 'pH', 'Colour', 'Aroma'
    ], msg
    assert "Chardonnay" in list(
        answer.Grape
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.Alcohol)
    ) == 69.33, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return ("success")


def test_1c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[
        0] == 5, "The number of rows are incorrect. Are you specifying the number of rows?"
    msg = "Your dataframe contains the incorrect columns. Are you specifying the correct index_col? \
    \nExpected ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour','Aroma'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour', 'Aroma']), msg
    assert "Malbec" in list(
        answer.Grape
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert "Red" in list(
        answer.Colour
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return ("success")


def test_1d(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 5 and answer.shape[1] == 6, "Your dataframe dimensions are incorrect. Are you specifying the correct delimeter?"
    msg = "Your dataframe contains the incorrect columns. Are you specifying the correct index_col? \
    \nExpected ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour','Aroma'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour', 'Aroma']), msg
    assert "Chardonnay" in list(
        answer.Grape
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.Alcohol)
    ) == 69.33, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return ("success")


def test_1f(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[
        0] == 5, "The number of rows are incorrect. Are you specifying the correct number of rows and correct delimeter?"
    assert answer.shape[
        1] == 6, "The number of columns are incorrect. Are you specifying the correct columns and header?"
    msg = "Your dataframe contains the incorrect columns. Are you specifying the correct index? \
    \nExpected ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour','Aroma'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour', 'Aroma']), msg
    assert "Chardonnay" in list(
        answer.Grape
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.Alcohol)
    ) == 69.33, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return ("success")


def test_1g(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 5 and answer.shape[1] == 6, "Your dataframe dimensions are incorrect. Are you specifying the correct function to read the data?"
    msg = "Your dataframe contains the incorrect columns. Are you specifying the correct index? \
    \nExpected ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour','Aroma'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour', 'Aroma']), msg
    assert "Chardonnay" in list(
        answer.Grape
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.Alcohol)
    ) == 69.33, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return ("success")


def test_1h(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 5 and answer.shape[1] == 6, "Your dataframe dimensions are incorrect. Are you specifying the correct sheet?"
    msg = "Your dataframe contains the incorrect columns. Are you specifying the correct index? \
    \nExpected ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour','Aroma'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Grape', 'Origin', 'Alcohol', 'pH', 'Colour', 'Aroma']), msg
    assert "Chardonnay" in list(
        answer.Grape
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.Alcohol)
    ) == 69.33, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return ("success")


def test_1i(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 653 and answer.shape[1] == 3, "Your dataframe dimensions are incorrect. Are you specifying the correct URL"
    msg = "Your dataframe contains the incorrect columns. Do you have the correct dataframe? \
    \nExpected ['Date', 'From US', 'From Britain'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Date', 'From US', 'From Britain']), msg
    assert "25/06/2016" in list(
        answer.Date
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return ("success")


def test_2a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 146461 and answer.shape[1] == 19, "Your dataframe dimensions are incorrect. Are you using the correct function to load the data?"
    msg = "Your dataframe contains the incorrect columns. Are you specifying the correct delimiter? \
    \nExpected ['CIVIC_NUMBER', 'COMMON_NAME', 'CULTIVAR_NAME','CURB'],, but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns))[1:5] == sorted(
        ['CIVIC_NUMBER', 'COMMON_NAME', 'CULTIVAR_NAME', 'CURB']), msg
    assert "PRUNUS" in list(
        answer.GENUS_NAME
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return ("success")


def test_2b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(
        answer.columns
    ) == 20, "The number of columns is incorrect. Have you added DIAMETER_CM?"
    assert "DIAMETER_CM" in list(
        answer.columns), "You are missing the DIAMETER_CM columns"
    assert round(
        sum(answer["DIAMETER_CM"])
    ) == 4277067, "DIAMETER_CM values are incorrect. Are you converting properly?"
    return ("success")


def test_2c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 13353 and answer.shape[1] == 20, "Your dataframe dimensions are incorrect. Are you subsetting correctly?"
    assert list(set(answer.SPECIES_NAME)) == [
        'SERRULATA'
    ], "You have more than one species present. Are you subsetting correctly?"
    return ("success")


def test_2d(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(
        answer
    ) == 16, "The number of groups is incorrect. Are you using the group_by function?"
    assert sorted(list(answer.groups.keys())[0:2]) == sorted([
        'ACCOLADE CHERRY', 'AMANOGAWA JAPANESE CHERRY'
    ]), "The groups are incorrect, Are you grouping by COMMON_NAME?"
    return ("success")


def test_2e(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sorted(list(round(answer.loc['ACCOLADE CHERRY']))) == sorted(
        [53.0, 60.0]
    ), "Some of your values are incorrect. Are you grouping on COMMON_NAME first and then aggregating by mean and count?"
    assert sorted(list(round(answer.loc['SEIBOLDI CHERRY']))) == sorted(
        [43.0, 170.0]
    ), "Some of your values are incorrect. Are you grouping on COMMON_NAME first and then aggregating by mean and count?"
    assert round(
        max(answer['mean'])
    ) == 72, "The range of averages is incorrect. Are you taking the mean?"
    assert max(
        answer['count']
    ) == 10540, "The range of counts is incorrect. Are you counting correctly?"
    return ("success")


def test_2f(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert (answer.mark == 'bar' or answer.mark.type == 'bar'), "Make sure you are using the 'mark_bar()' function"
    assert str(answer.encoding.x.shorthand) == 'COMMON_NAME' or str(answer.encoding.x.field) == 'COMMON_NAME', "Make sure you are plotting the \
                                                                                                    `COMMON_NAME` variable on the x-axis."
    if str(answer.encoding.y.shorthand) == 'Undefined':
        assert answer.encoding.y.field == 'mean', "Make sure you are plotting the mean on the y-axis"
    else:
        assert 'mean' in str(answer.encoding.y.shorthand), "Make sure you are plotting the mean on the y-axis"
    assert not answer.title == 'Undefined', "Make sure you are providing a title for the plot."
    return ("success")


def test_3a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 1309 and answer.shape[1] == 14, "Your dataframe dimensions are incorrect. Are you reading in the correct dataframe?"
    assert sorted(list(answer.columns))[1:5] == [
        'boat', 'body', 'cabin', 'embarked'
    ], "Some of your columns are incorrect. Do you have the correct dataframe?"
    assert "C22 C26" in list(
        answer.cabin
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return ("success")


def test_3b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(
        {'sibsp', 'parch'}.intersection(set(answer.columns))
    ) == 0, "sibsp and parch still exists. Have you changed their names?"
    assert len({'siblings_spouses', 'parents_children'}.intersection(
        set(answer.columns)
    )) == 2, "The new column names do not exists. Have you changed the names?"
    return ("success")


def test_3c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 1309 and answer.shape[1] == 12, "Your dataframe dimensions are incorrect. Did you drop any columns?"
    assert len({'body', 'cabin'}.intersection(set(answer.columns))
               ) == 0, "Body and cabin still exists. Have you dropped them?"
    return ("success")


def test_3e(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer + 10).encode('utf8')).hexdigest(
    ) == '2d3fbcffe8a44d7f02a2b8c374085b84f0284201', "The number of survivors is incorrect. Are you selecting only survivors?"
    return ("success")


def test_3f(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 8 and answer.shape[1] == 14, "Your dataframe dimensions are incorrect. Are you subsetting correctly?"
    assert round(
        sum(answer.fare)
    ) == 1233, "The sum of the fares is incorrect. Are you selecting only ages less than 16 in first class?"
    assert round(
        answer.age.mean()
    ) == 8.0, "The average age is incorrect. Are you selecting only ages less than 16 in first class?"
    assert set(answer.pclass) == {
        1
    }, "Your dataframe contains more than first class individuals. Are you selecting only first class?"
    return ("success")


def test_3g(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(list(answer)[0] + 10).encode('utf8')).hexdigest(
    ) == "ebb4fe9f608ae0e66e714b2299a672ef7cc1e0f3", "The average age is incorrect. Are you computing it correctly?"
    assert sha1(str(list(answer)[1] + 10).encode('utf8')).hexdigest(
    ) == "81087e980caa119b87c091c0f1048c577e277c15", "The average fare is incorrect. Are you computing it correctly?"
    return ("success")


def test_3h(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert list(answer.index) == [
        'female', 'male'
    ], "The groups are incorrect. Are you grouping by sex?"
    assert sha1(
        str(list(round(answer.loc['female']))[0]).encode('utf8')
    ).hexdigest(
    ) == "70142f66475ae2fb33722d8d4750f386ecfefe7b", "Some vaThe groups are incorrect, Are you grouping by COMMON_NAME?lues are incorrect. Are you using the mean function?"
    assert sha1(
        str(list(round(answer.loc['female']))[1]).encode('utf8')
    ).hexdigest(
    ) == "e8dc057d3346e56aed7cf252185dbe1fa6454411", "Some values are incorrect. Are you using the mean function?"
    assert sha1(
        str(list(round(answer.loc['male']))[2]).encode('utf8')
    ).hexdigest(
    ) == "af7ac69416fe2aa0fe4e14e167044ae9813d1318", "Some values are incorrect. Are you using the mean function?"
    assert sha1(
        str(list(round(answer.loc['male']))[3]).encode('utf8')
    ).hexdigest(
    ) == "38f6d7875e3195bdaee448d2cb6917f3ae4994af", "Some values are incorrect. Are you using the mean function?"
    return ("success")


def test_3i(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + "T").encode('utf8')).hexdigest(
    ) == "9eb1eeb4de77eb9c787fa2d19bbceb532d690116", "Answer is incorrect"
    return ("success")


def test_3j(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert list(answer.index) == [
        'female', 'male'
    ], "The group names are incorrect. Are you grouping by sex?"
    assert sha1(
        str(list(round(answer.loc['female']))[0]).encode('utf8')
    ).hexdigest(
    ) == "5e9cdb5ce344cda5613041b69b4e7d5ad7f26be3", "Max value is incorrect. Are you using the correct function?"
    assert sha1(
        str(list(round(answer.loc['female']))[1]).encode('utf8')
    ).hexdigest(
    ) == "5e56ceb6a3ee0eeaba07ec39a491a470a34c31f7", "Min value is incorrect. Are you using the correct function?"
    assert sha1(
        str(list(round(answer.loc['male']))[0] + 9).encode('utf8')
    ).hexdigest(
    ) == "f619bd0573a24a36b86ea0620e9e84f3c74e7fa6", "Some values are incorrect. Are you using the correct function?"
    assert sha1(
        str(list(round(answer.loc['male']))[1] + 10).encode('utf8')
    ).hexdigest(
    ) == "c23f7da7070511444ebc75875fd9d202b5dd13cf", "Some values are incorrect. Are you using the correct function?"
    return ("success")


def test_3k(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.encode("utf8")).hexdigest(
    ) == "e47b8984ceba51bd6004ac6575ca688ba8a05991", "Answer is incorrect. Are you chaining the correct commands?"
    return ("success")


def test_4a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert (answer.mark == 'bar' or answer.mark.type == 'bar'), "Make sure you are using the 'mark_bar()' function"
    assert answer.encoding.x.shorthand == 'pclass' or answer.encoding.x.field == 'pclass', "Make sure you are plotting the 'pclass' variable on the x-axis."
    if str(answer.encoding.y.shorthand) == 'Undefined':
        assert answer.encoding.y.field == 'survived', "Make sure you are plotting the 'survived' variable on the y-axis."
    else:
        assert 'survived' in str(answer.encoding.y.shorthand), "Make sure you are plotting the 'survived' variable on the y-axis."
    assert not answer.title == 'Undefined', "Make sure you are providing a title for the plot."
    return ("success")


def test_4b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + "Y").encode('utf8')).hexdigest(
    ) == "a892d11bb4ca68a3866b7feaa3c9ae302516a478", "Answer is incorrect"
    return ("success")


def test_4c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert (answer.mark == 'bar' or answer.mark.type == 'bar'), "Make sure you are using the 'mark_bar()' function"
    assert answer.encoding.x.shorthand == 'sex' or answer.encoding.x.field == 'sex', "Make sure you are plotting the 'sex' variable on the x-axis."
    if str(answer.encoding.y.shorthand) == 'Undefined':
        assert answer.encoding.y.field == 'survived', "Make sure you are plotting the 'survived' variable on the y-axis."
    else:
        assert 'survived' in str(answer.encoding.y.shorthand), "Make sure you are plotting the 'survived' variable on the y-axis."
    assert not answer.title == 'Undefined', "Make sure you are providing a title for the plot."
    return ("success")


def test_4d(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + "Y").encode('utf8')).hexdigest(
    ) == "3723abda8a02e1484745a568b80f8fbec8abad50", "Answer is incorrect"
    return ("success")


def test_4e(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert (answer.mark == 'bar' or answer.mark.type == 'bar'), "Make sure you are using the 'mark_bar()' function"
    assert answer.encoding.x.shorthand == 'age_group' or answer.encoding.x.field == 'age_group', "Make sure you are plotting the 'age_group' variable on the x-axis."
    if str(answer.encoding.y.shorthand) == 'Undefined':
        assert answer.encoding.y.field == 'survived', "Make sure you are plotting the 'survived' variable on the y-axis."
    else:
        assert 'survived' in str(answer.encoding.y.shorthand), "Make sure you are plotting the 'survived' variable on the y-axis."
    assert not answer.title == 'Undefined', "Make sure you are providing a title for the plot."
    return ("success")

def test_4g(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert list(answer.index[0]) == [1, 'female'
    ], "Incorrect values. Are you grouping and sorting correctly?"
    assert list(answer.index[2]) == [3, 'female'
    ], "Incorrect values. Are you grouping and sorting correctly?"
    assert list(answer.index[3]) == [1, 'male'
    ], "Incorrect values. Are you grouping and sorting correctly?"
    assert list(answer.index[5]) == [2, 'male'
    ], "Incorrect values. Are you grouping and sorting correctly?"
    return ("success")


def test_4h(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer + 7).encode('utf8')).hexdigest(
    ) == "632667547e7cd3e0466547863e1207a8c0c0c549", "Answer is incorrect"
    return ("success")

def test_4i(answer):
    assert list(answer.index[0]) == [3, 'female', 'senior'], "Incorrect values. Are you grouping and sorting correctly?"
    assert list(answer.index[23]) == [3, 'male', 'senior'], "Incorrect values. Are you grouping and sorting correctly?"
    assert list(answer.index[12]) == [1, 'male', 'adult'], "Incorrect values. Are you grouping and sorting correctly?"
    return("success")


def test_4j(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer).encode('utf8')).hexdigest(
    ) == "98ae019454f12e734c6fefc48b193b4e5c47604f", "Answer is incorrect"
    return("success")
