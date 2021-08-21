from hashlib import sha1
import pandas as pd
import pytest
import sys
from decimal import Decimal


def test_1a(answer):
    case1 = (sha1(str(answer[0].lower() + "x").encode("utf8")).hexdigest() == "2a2e1206b4222b0d7cc8c8a1d8b302ee70cfe817")
    case2 = (sha1(str(answer[1].lower() + "p").encode("utf8")).hexdigest() == "0691a664b24b6f15b20cd5aee64b72271db08be1")
    total_sum = sum([case1, case2])
    assert total_sum == 2, "You have {0} correct answer(s) and {1} incorrect answer(s).".format(total_sum, 2-total_sum)
    return("Success")

def test_1b(answer):
    assert len(answer) == 1, "There is only one correct answer for this question"
    assert sha1(str(answer).encode("utf8")).hexdigest() == "f1e31df9806ce94c5bdbbfff9608324930f4d3f1", "Your answer is incorrect"
    return("Success")


def test_1d(answer):
    assert answer.shape[0] == 4 and answer.shape[1] == 3, "Your dataframe dimensions are incorrect. Are you tidying properly?"
    assert answer[answer.columns[-1]].sum() == 57, "Some values in your dataframe are incorrect. Are you tidying properly?"
    return("Success")

def test_1e(answer):
    assert sha1(str(answer.lower() + "c").encode("utf8")).hexdigest() == "13211ef68928d927b98c56e3497bfbc0a93a377a", "Your answer is incorrect"
    return("Success")

def test_2a(answer):
    assert answer.shape[0] == 21 and answer.shape[1] == 3, "Your dataframe dimensions are incorrect. Are you using the read_csv function?"
    msg = "Your dataframe contains the incorrect columns. Are you using the correct index column? \
    \nExpected ['School', 'Women', 'Men'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['School', 'Women', 'Men']), msg
    assert "MIT" in list(
        answer.School
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert sum(
        list(answer.Women)
    ) == 1703, "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return("Success")

def test_2b(answer):
    assert sha1(str(answer.lower() + "e").encode("utf8")).hexdigest() == "986b1bc1eb8de89643c50722910f99001c232865", "Your answer is incorrect"
    return("Success")

def test_2c(answer):
    assert answer.shape[0] == 42 and answer.shape[1] == 3, "Your dataframe dimensions are incorrect. using the .melt function with School as id_vars?"
    msg = "Your dataframe contains the incorrect columns. Are you using the correct index column? \
    \nExpected ['School', 'Gender', 'Wage'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['School', 'Gender', 'Wage']), msg
    assert list(answer.School)[0:4] == ['Berkeley', 'Berkeley', 'Brown', 'Brown'], "Order of School column incorrect. Are you sorting by School?"
    assert list(answer.Gender)[0:4] == ['Men', 'Women', 'Men', 'Women'], "Order of School column incorrect. Are you sorting by Gender?"
    return("Success")

def test_2e(answer):
    assert sha1(str(answer.lower() + "w").encode("utf8")).hexdigest() == "e2c44c572970480e0089da2b6ef90adce84d30fd", "Your answer is incorrect"
    return("Success")


def test_2f(answer):
    assert answer.shape[0] == 21 and answer.shape[1] == 3, "Your dataframe dimensions are incorrect. Are you using the pivot function"
    msg = "Your dataframe contains the incorrect columns. Are you pivoting properly? \
    \nExpected ['School', 'Women', 'Men'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['School', 'Women', 'Men']), msg
    assert "Harvard" in list(
        answer.School
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    assert list(answer.index)[0:4] == [0, 1, 2, 3], "The index columns are incorrect. Did you reset the columns when pivoting?"
    return("Success")

def test_2g(answer):
    assert answer.shape[1] == 4, "The number of columns is incorrect. Are you adding the Wage_Gap column?"
    msg = "Your dataframe contains the incorrect columns. Are you adding the Wage_Gap column? \
    \nExpected ['School', 'Women', 'Men', 'Wage_Gap'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['School', 'Women', 'Men', 'Wage_Gap']), msg
    assert answer.Wage_Gap.sum() == 681, "Wage_Gap values are incorrect. Are you computing the wage gap properly?"
    assert list(answer.Wage_Gap)[0:4] == [58, 55, 53, 49], "Order of Wage_Gap column is incorrect. Are you sorting by Wage_Gap in decending order?"
    return("Success")

# =============================================================================   
# def test_2i(answer):
#     msg = "Incorrect columns present in the dataframe. Are you keeping the Wage_Gap column \
#     \nExpected ['School', 'Wage_Gap', 'Gender', 'Wage'], but got {0}".format(
#         list(answer.columns))
#     assert sorted(list(answer.columns)) == sorted(
#         ['School', 'Wage_Gap', 'Gender', 'Wage']), msg
#     return("Success")
#
# def test_2j(answer):
#     assert answer.get_xlabel(
#     ), "No x-axis label present, Please provide labels"
#     assert list(answer.get_ylim()) == [
#         0.0, 173.25
#     ], "The y-axis limits are incorrect. Are you plotting the correct column?"
#     assert str(
#         list(answer.get_xticklabels())[0]
#     ) == "Text(0, 0, 'Berkeley')", "The x-axis contains incorrect values. Are you plotting the correct values?"
#     return ("success")
#
# def test_2k(answer):
#     assert answer.shape[1] == 4, "The number of columns is incorrect. Are you transforming the Men and Women columns?"
#     msg = "Your dataframe contains the incorrect columns. Are you adding the Men and Women columns \
#     \nExpected ['School', 'Wage_Gap', 'Men', 'Women'], but got {0}".format(
#         list(answer.columns))
#     assert sorted(list(answer.columns)) == sorted(
#         ['School', 'Wage_Gap', 'Men', 'Women']), msg
#     return("Success")
#     
# =============================================================================

def test_2h(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert (answer.mark == 'bar' or answer.mark.type == 'bar'), "Make sure you are using the 'mark_bar()' function"
    assert str(answer.encoding.x.shorthand) == 'School' or str(answer.encoding.x.field) == 'School', "Make sure you are plotting the \
                                                                                                    `School` variable on the x-axis."
    assert str(answer.encoding.y.shorthand) == 'Wage_Gap' or str(answer.encoding.y.field) == 'Wage_Gap', "Make sure you are plotting the \
                                                                                                    `Wage_Gap` variable on the y-axis."
    assert not answer.title == 'Undefined', "Make sure you are providing a title for the plot."
    return ("success")

def test_3a(answer):
    assert answer.shape[0] == 5 and answer.shape[1] == 8, "Your dataframe dimensions are incorrect. Are you concatinating and merging?"
    msg = "Your dataframe contains the incorrect columns. Are you merging by title? \
    \nExpected ['title','type','director','country','date_added','release_year','rating','duration'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['title','type','director','country','date_added','release_year','rating','duration']), msg
    assert set(answer.type) == {'Movie', 'TV Show'}, "The type column contains incorrect values. Are you merging by title?"
    return("Success")

def test_3c(answer1, answer2, answer3, answer4):
    case1 = (sha1(str(answer1.lower() + "t").encode("utf8")).hexdigest() == "8898418c76244dcb558dbdc6d32107882050de0a")
    case2 = (sha1(str(answer2.lower() + "u").encode("utf8")).hexdigest() == "670dab28256d98e66ce82019b35f628e292f4f05")
    case3 = (sha1(str(answer3.lower() + "v").encode("utf8")).hexdigest() == "8ea4a46aacad00a1a028b61ebc4c3252271bb134")
    case4 = (sha1(str(answer4.lower() + "w").encode("utf8")).hexdigest() == "649b391d73110dd0cb56ba752ff2706b830248fa")
    total_correct = sum([case1, case2, case3, case4])
    assert  total_correct == 4, "You have {0} correct answers and {1} incorrect answers".format(total_correct, 4 - total_correct)
    return("Success")

def test_4a(answer):
    assert answer.shape[0] == 195 and answer.shape[1] == 5, "Your dataframe dimensions are incorrect. Are you reading in the specified columns?"
    msg = "Your dataframe contains the incorrect columns. Are you specifying the correct columns? \
    \nExpected ['Country', '2008', '2009', '2010', '2011'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Country', '2008', '2009', '2010', '2011']), msg
    assert "Venezuela" in list(
        answer.Country
    ), "Some values in your dataframe are incorrect. Do you have the correct dataframe?"
    return("Success")

def test_4b(answer):
    assert answer.shape[0] == 780 and answer.shape[1] == 3, "Your dataframe dimensions are incorrect. Are you using the melt function with Country as id_var?"
    msg = "Your dataframe contains the incorrect columns. Are you setting the var_name and value_name? \
    \nExpected ['Country', 'Year', 'Population'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Country', 'Year', 'Population']), msg
    assert answer.Population.sum() == 27501912178, "Some values in the Population colum are wrong. Are you melting with id_vars as Country?"
    return("Success")

def test_4c(answer):
    assert answer.shape[0] == 828 and answer.shape[1] == 6, "Your dataframe dimensions are incorrect. Are you merging by Country and Year?"
    msg = "Your dataframe contains the incorrect columns. Are you merging by Country and Year? \
    \nExpected ['Country', 'Year', 'Population', 'Continent', 'Emission', '_merge'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Country', 'Year', 'Population', 'Continent', 'Emission', '_merge']), msg
    assert round(answer.Emission.sum()) == 3868.0, "The Emission column contains incorrect values. Are you merging by Country and Year?"
    assert round(answer.Population.sum()) == 27501912178.0, "The Population column contains incorrect values. Are you merging by Country and Year?"
    return("Success")

def test_4d(answer):
    assert answer.shape[0] == 207 and answer.shape[1] == 5, "Your dataframe dimensions are incorrect. Are you filtering by year = 2010 and dropping the year column?"
    msg = "Your dataframe contains the incorrect columns. Are you filtering by year = 2010 and dropping the year column? \
    \nExpected ['Country', 'Continent', 'Emission', 'Population', '_merge'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Country', 'Continent', 'Emission', 'Population', '_merge']), msg
    assert round(answer.Emission.sum()) == 973.0, "The Emission column contains incorrect values. Are you selecting only 2010 and dropping Year?"
    assert round(answer.Population.sum()) == 6915441183.0, "The Population column contains incorrect values. Are you selecting only 2010 and dropping Year?"
    return("Success")

def test_4e(answer1, answer2, answer3):
    case1 = (sha1(str(answer1 + 11).encode("utf8")).hexdigest() == "472b07b9fcf2c2451e8781e944bf5f77cd8457c8")
    case2 = (sha1(str(answer2 + 15).encode("utf8")).hexdigest() == "bc33ea4e26e5e1af1408321416956113a4658763")
    case3 = (sha1(str(answer1 + 15).encode("utf8")).hexdigest() == "bc33ea4e26e5e1af1408321416956113a4658763")
    case4 = (sha1(str(answer2 + 11).encode("utf8")).hexdigest() == "472b07b9fcf2c2451e8781e944bf5f77cd8457c8")
    
    total_sum = sum([case1, case2, case3, case4])
    assert total_sum == 2, "You have {0} correct answers and {1} incorrect answer for missing_left and missing_right.".format(total_sum, 2-total_sum)
    assert answer3.shape[0] == 185 and answer3.shape[1] == 5, "Your dataframe dimensions are incorrect. Are you selecting rows that present in both dataframes?"
    assert round(answer3.Emission.sum()) == 870.0, "The Emission column contains incorrect values. Are you selecting rows that present in both dataframes?"
    assert round(answer3.Population.sum()) == 6895304100.0, "The Population column contains incorrect values. Are you selecting rows that present in both dataframes?"
    return("Success")

def test_4g(answer):
    assert answer.shape[0] == 6 and answer.shape[1] == 2, "Your dataframe dimensions are incorrect. Are you grouping by Continent and aggregating Population and Quantity?"
    msg = "Your dataframe contains the incorrect rows. Are you grouping by Continent? \
    \nExpected ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America'], but got {0}".format(
        list(answer.index))
    assert sorted(list(answer.index)) == sorted(
        ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']), msg
    return("Success")

def test_4h(answer):
    assert answer.shape[0] == 6 and answer.shape[1] == 3, "Your dataframe dimensions are incorrect. Are you adding the Emission_pp column?"
    msg = "Your dataframe contains the incorrect columns. Are you adding the Emission_pp column? \
    \nExpected ['Population', 'Quantity', 'Emission_pp'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Population', 'Quantity', 'Emission_pp']), msg
    assert round(answer.Emission_pp.sum()) == 39.0, "The Emission_pp column contains incorrect values. Are you dividing Quantity by Population?"
    return("Success")

def test_4i(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert (answer.mark == 'bar' or answer.mark.type == 'bar'), "Make sure you are using the 'mark_bar()' function"
    assert str(answer.encoding.x.shorthand) == 'Continent' or str(answer.encoding.x.field) == 'Continent', "Make sure you are plotting the \
                                                                                                    `Continent` variable on the x-axis."
    assert str(answer.encoding.y.shorthand) == 'Emission_pp' or str(answer.encoding.y.field) == 'Emission_pp', "Make sure you are plotting the \
                                                                                                    `Emission_pp` variable on the y-axis."
    assert not answer.title == 'Undefined', "Make sure you are providing a title for the plot."
    return("Success")
