from hashlib import sha1
import pandas as pd
import pytest
import sys
from decimal import Decimal
import operator


def test_1a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    answer = [x.lower() for x in answer]
    case1 = (sha1(str(answer[0] + "a").encode("utf8")).hexdigest() ==
             "c1943964a4b548e74ff06b3674506cf9de93b9a2")
    case2 = (sha1(str(answer[1] + "b").encode("utf8")).hexdigest() ==
             "87c8fbcf99ab95226f59406df61904a689e240a4")
    case3 = (sha1(str(answer[2] + "c").encode("utf8")).hexdigest() ==
             "52ca2ba99daee126e0067fee9377ff79f83a32e9")
    case4 = (sha1(str(answer[3] + "d").encode("utf8")).hexdigest() ==
             "fa6b5eaa1533458ee0170f3cdec816406ee9c190")
    case5 = (sha1(str(answer[4] + "e").encode("utf8")).hexdigest() ==
             "0292aa9c29e8e4b165701d18fab9761c999d92ff")
    case6 = (sha1(str(answer[5] + "f").encode("utf8")).hexdigest() ==
             "07a396e53e133f290939f8a3810723256895a49c")
    case7 = (sha1(str(answer[6] + "g").encode("utf8")).hexdigest() ==
             "e567235d2487893f97d6b1fb0602e632f6b6b47c")
    case8 = (sha1(str(answer[7] + "h").encode("utf8")).hexdigest() ==
             "b0fee6995bc1fcbe92a7785f7649f0b52dca2b26")
    case9 = (sha1(str(answer[8] + "i").encode("utf8")).hexdigest() ==
             "f244f7f1e104253bbdccfc2ab08cc2fb03ec5888")
    case10 = (sha1(str(answer[9] + "j").encode("utf8")).hexdigest() ==
              "79e7256b7a474c5e9ac1d0ffacb54477d93a8e47")
    case11 = (sha1(str(answer[10] + "k").encode("utf8")).hexdigest() ==
              "3c5c43ca3c88b3a57dd3f125f9ad040c3a915f18")
    total_sum = sum([
        case1, case2, case3, case4, case5, case6, case7, case8, case9, case10,
        case11
    ])
    assert total_sum == 11, "You have {0} correct answer(s) and {1} incorrect answer(s).".format(
        total_sum, 11 - total_sum)
    return ("Success")


def test_2a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    answer = [x.lower() for x in answer]
    case1 = (sha1(str(answer[0] + "a").encode("utf8")).hexdigest() ==
             "31aeea97a13f516d66a5c6a932cc482d4f2764ea")
    case2 = (sha1(str(answer[1] + "b").encode("utf8")).hexdigest() ==
             "7a5788e3a4f655f8487b31415fa525a6a27379bb")
    case3 = (sha1(str(answer[2] + "c").encode("utf8")).hexdigest() ==
             "7ef6d49f720ea5dc0da9e01bce36601ffe289237")
    case4 = (sha1(str(answer[3] + "d").encode("utf8")).hexdigest() ==
             "23de6f4c6dc18ce0f2f9a3f25ec3407483274484")
    case5 = (sha1(str(answer[4] + "e").encode("utf8")).hexdigest() ==
             "bbfe131fd1b5aaa5116a9172b7479cf9c929dd3b")
    case6 = (sha1(str(answer[5] + "f").encode("utf8")).hexdigest() ==
             "52b263907e59fceb54aea9ef9a08098a86be89a0")
    case7 = (sha1(str(answer[6] + "g").encode("utf8")).hexdigest() ==
             "1b40f4659d5e5e922ab46991ca5acc2e875c20c8")
    case8 = (sha1(str(answer[7] + "h").encode("utf8")).hexdigest() ==
             "2bb95934e0ccf331c15aad506c22741642965ec7")
    case9 = (sha1(str(answer[8] + "i").encode("utf8")).hexdigest() ==
             "5a52c3a88f12b8d9f1079c1404f9684aa3582d1f")
    case10 = (sha1(str(answer[9] + "j").encode("utf8")).hexdigest() ==
              "26a370cc84a6f4c7f474a834ee9bc1688a42b9a7")
    case11 = (sha1(str(answer[10] + "k").encode("utf8")).hexdigest() ==
              "0491301843bdb2e791d9509ded840db2e32acd8d")
    case12 = (sha1(str(answer[11] + "l").encode("utf8")).hexdigest() ==
              "7b1f0ffa6527a9c34b4f84868426925f8fc4af09")
    case13 = (sha1(str(answer[12] + "m").encode("utf8")).hexdigest() ==
              "e33c45ce6375ff982e8f732745749e7276c2218e")
    total_sum = sum([
        case1, case2, case3, case4, case5, case6, case7, case8, case9, case10,
        case11, case12, case13
    ])
    assert total_sum == 13, "You have {0} correct answer(s) and {1} incorrect answer(s).".format(
        total_sum, 13 - total_sum)
    return ("Success")


def test_2c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    answer = [x.lower() for x in answer]
    case1 = (sha1(str(answer[0] + "1").encode("utf8")).hexdigest() ==
             "d79ea06897f53e04431e5c2389e6aced44201e1e")
    case2 = (sha1(str(answer[1] + "2").encode("utf8")).hexdigest() ==
             "e84087cf04566d37d981b5bd3677697167149670")
    case3 = (sha1(str(answer[2] + "3").encode("utf8")).hexdigest() ==
             "4b1365b775c519fd6a316a7837f7695bff350ff0")
    case4 = (sha1(str(answer[3] + "4").encode("utf8")).hexdigest() ==
             "dca62daace659c836a6e82a878ec29eea409df45")
    case5 = (sha1(str(answer[4] + "5").encode("utf8")).hexdigest() ==
             "2020ff47c450baa0794838a958148ef508b6ab67")
    case6 = (sha1(str(answer[5] + "6").encode("utf8")).hexdigest() ==
             "64039a097dcdcc9b8aa6b245354541ae09ba1620")
    case7 = (sha1(str(answer[6] + "7").encode("utf8")).hexdigest() ==
             "a2125002d39eec28a22bd7a6fd1c5704f800f4f5")
    case8 = (sha1(str(answer[7] + "8").encode("utf8")).hexdigest() ==
             "b74777c55db0fb6707ffab4f3db006eb69c34c57")
    case9 = (sha1(str(answer[8] + "9").encode("utf8")).hexdigest() ==
             "7f62f8ab45559e197cf9e8f4a06b877f10a78580")
    case10 = (sha1(str(answer[9] + "10").encode("utf8")).hexdigest() ==
              "70090c5ae2f1d5b7064f87dccd76b2758eb930ec")
    case11 = (sha1(str(answer[10] + "11").encode("utf8")).hexdigest() ==
              "2dde20e6596d8f082be437fc1375512ef58a2d0f")
    case12 = (sha1(str(answer[11] + "12").encode("utf8")).hexdigest() ==
              "62855340a91b943c0a0be267c1c78b39e7c15287")
    total_sum = sum([
        case1, case2, case3, case4, case5, case6, case7, case8, case9, case10,
        case11, case12
    ])
    assert total_sum == 12, "You have {0} correct answer(s) and {1} incorrect answer(s).".format(
        total_sum, 12 - total_sum)
    return ("Success")


def test_3a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    answer = [str(x).lower() for x in answer]
    assert sha1(str(answer[0] + "A").encode("utf8")).hexdigest(
    ) == "3cae921935215da5c275391ab043af1333c0fdac", "The data type for 'Country' is incorrect. Are you using the 'dtypes' function?"
    assert sha1(str(answer[1] + "B").encode("utf8")).hexdigest(
    ) == "c52172635b199a6ab77e4b3456f9023cfb3502b8", "The data type for 'year_2012' is incorrect. Are you using the 'dtypes' function?"
    assert sha1(str(answer[2] + "C").encode("utf8")).hexdigest(
    ) == "6eede883da721977045060ab0be4a8f3c1bd32e5", "The data type for 'year_2013' is incorrect. Are you using the 'dtypes' function?"
    assert sha1(str(answer[3] + "D").encode("utf8")).hexdigest(
    ) == "b40cb7b89fd5245600697256fa2006995102e24e", "The data type for 'year_2014' is incorrect. Are you using the 'dtypes' function?"
    assert sha1(str(answer[4] + "E").encode("utf8")).hexdigest(
    ) == "a7e68017692ca22049a8af690500ac4aa261c122", "The data type for 'year_2015' is incorrect. Are you using the 'dtypes' function?"
    assert sha1(str(answer[5] + "F").encode("utf8")).hexdigest(
    ) == "9d188fa2e081e420c2f4ca22167b754a66fbfa4a", "The data type for 'year_2016' is incorrect. Are you using the 'dtypes' function?"
    return ("Success")


def test_3b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 585 and answer.shape[1] == 3, "Your dataframe dimensions are incorrect. using the .melt function with School as Country?"
    msg = "Your dataframe contains the incorrect columns. Are you using the correct index column? \
    \nExpected ['Country', 'Year', 'Population'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['Country', 'Year', 'Population']), msg
    return ("Success")


def test_3c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    answer = [str(x).lower() for x in answer]
    sha1(str(answer[0] + "K").encode("utf8")).hexdigest(
    ) == "7c5d1f6411d2c2ab9e8226fa86ec0a3e1cec49d3", "The data type for 'Year_type' is incorrect. Are you using the 'dtypes' function?"
    sha1(str(answer[1] + "w").encode("utf8")).hexdigest(
    ) == "b20aa03eae57d05b936df12094357be9d9fe539e", "The data type for 'Population_type' is incorrect. Are you using the 'dtypes' function?"
    return ("Success")


def test_3e(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert str(
        answer.Year.dtype
    ) == "int64", "Make sure you are using the 'astype()' function to change the 'Year' column data type."
    return ("Success")


def test_3f(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer + "z").encode("utf8")).hexdigest(
    ) == "3f59e5bf0b4aa9d8ccce288b1ccc1597b1d66da3", "Your answer is incorrect. Please try again."
    return ("Success")


def test_4a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    answer = [[j.lower() for j in i] for i in answer]
    case1 = (sha1(str(answer[0]).encode("utf8")).hexdigest() ==
             "420379f27d2303a20d696ec57f607d740bae7d9c")
    case2 = (sha1(str(answer[1]).encode("utf8")).hexdigest() ==
             "21744f7bedceb72efae76e558a43da7fe3321b62")
    case3 = (sha1(str(answer[2]).encode("utf8")).hexdigest() ==
             "80d54d00594661070488bd49133ee5ef2deeded8")
    case4 = (sha1(str(answer[3]).encode("utf8")).hexdigest() ==
             "96a38fd2712b4e0e73837aaeac2e8136e67b4a91")
    case5 = (sha1(str(answer[4]).encode("utf8")).hexdigest() ==
             "9d7ad2b72019f7ce8bbdaf85b99e2daceb2770f1")
    case6 = (sha1(str(answer[5]).encode("utf8")).hexdigest() ==
             "a0edf00e10c0275dda545819d5d19dcf3f9157ce")
    case7 = (sha1(str(answer[6]).encode("utf8")).hexdigest() ==
             "08390e1f452d666b31eb001d81a898796a1a164a")
    case8 = (sha1(str(answer[7]).encode("utf8")).hexdigest() ==
             "f2139d15705b2a1b00922e7fdf2abae4859b7ec9")
    case9 = (sha1(str(answer[8]).encode("utf8")).hexdigest() ==
             "21744f7bedceb72efae76e558a43da7fe3321b62")
    case10 = (sha1(str(answer[9]).encode("utf8")).hexdigest() ==
              "80d54d00594661070488bd49133ee5ef2deeded8")
    total_sum = sum([
        case1, case2, case3, case4, case5, case6, case7, case8, case9, case10
    ])
    assert total_sum == 10, "You have {0} correct answer(s) and {1} incorrect answer(s).".format(
        total_sum, 10 - total_sum)
    return ("Success")


def test_5a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer + "y").encode("utf8")).hexdigest(
    ) == "cdc1a9a393a3b2c70ba267b063e7f59bb04dd0b0", "Your answer is incorrect. Please try again."
    return ("Success")


def test_5b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert str(
        type(answer)
    ) == "<class 'pandas.core.frame.DataFrame'>", "Make sure you are using the correct verb to convert the json file to a dataframe"
    assert answer.shape[0] == 189 and answer.shape[1] == 7, "Your dataframe dimensions are incorrect. Are you using the correct verb?"
    msg = "Your dataframe contains the incorrect columns. Are you using the correct verb? \
    \nExpected ['Year','Classification','Union','Minimum hourly rate','Maximum hourly rate','Women','Men'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted([
        'Year', 'Classification', 'Union', 'Minimum hourly rate',
        'Maximum hourly rate', 'Women', 'Men'
    ]), msg
    return ("Success")


def test_5c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 189 and answer.shape[1] == 8, "Your dataframe dimensions are incorrect. Are you adding the 'Total' column?"
    msg = "Your dataframe contains the incorrect columns. Are you adding the 'Total' column? \
    \nExpected ['Year','Classification','Union','Minimum hourly rate','Maximum hourly rate','Women','Men', 'Total'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted([
        'Year', 'Classification', 'Union', 'Minimum hourly rate',
        'Maximum hourly rate', 'Women', 'Men', 'Total'
    ]), msg
    assert round(
        sum(answer.Total)
    ) == 8074, "The values in the 'Total' column are incorrect. Are you over both 'Men' and 'Women'?"
    return ("Success")


def test_5e(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(len(answer)).encode("utf8")).hexdigest(
    ) == "356a192b7913b04c54574d18c28d46e6395428ab", "The number of answers is incorrect. Please try again."
    assert sha1(str(answer[0]).encode("utf8")).hexdigest(
    ) == "94c2a3189e7f7885455350c4c7a8df2d0d6ad1d1", "Your answer is incorrect. Please try again."
    return ("Success")


def test_6a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 7 and answer.shape[1] == 8, "Your dataframe dimensions are incorrect. Are you using the 'pd.DataFrame()' function?"
    msg = "Your dataframe contains the incorrect columns. Are you specifying the 'columns' in the 'pd.DataFrame()' function?\
    \nExpected ['day','description','day_temperature','night_temperature','pop','wind','hrs_sun','rain'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted([
        'day', 'description', 'day_temperature', 'night_temperature', 'pop',
        'wind', 'hrs_sun', 'rain'
    ]), msg
    return ("Success")


def test_6c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(round(answer) + 11).encode("utf8")).hexdigest(
    ) == "64e095fe763fc62418378753f9402623bea9e227", "Your answer is incorrect. Make sure you are selecting \
    the correct column and converting to the proper datatype using 'astype'."

    return ("Success")


def test_6d(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 7 and answer.shape[1] == 9, "Your dataframe dimensions are incorrect. Are you adding the 'temp_avg' column?"
    assert 'temp_avg' in list(
        answer.columns
    ), "The 'temp_avg' column does not exist. Please add it to your dataframe."
    assert round(
        sum(answer.temp_avg)
    ) == 125, "The values in the 'temp_avg' column are incorrect. Are you converting 'night_temperature' to the correct format\
    before computing the average?"

    return ("Success")


def test_6e(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 7 and answer.shape[1] == 2, "Your dataframe dimensions are incorrect. Are you adding the wind_speed and wind_direction columns?"
    msg = "Your dataframe contains the incorrect columns. Are you adding the wind_speed and wind_direction columns?\
    \nExpected ['wind_speed', 'wind_direction'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted(
        ['wind_speed', 'wind_direction']), msg
    assert str(
        answer.wind_speed.dtype
    ) == "int64", "Make sure you are converting the 'wind_speed' column to type 'int64'"
    assert set(answer.wind_direction) == {
        'S', 'SE', 'SW', 'W'
    }, "The values in the 'wind_direction' columns are incorrect. Are you using the \
    '.str.split()' funciton with argument 'expand=True'?"

    assert round(
        sum(answer.wind_speed)
    ) == 79, "The values in the 'wind_speed' columns are incorrect. Are you using the \
    '.str.split()' funciton with argument 'expand=True'?"

    return ("Success")


def test_6f(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape[0] == 7 and answer.shape[1] == 11, "Your dataframe dimensions are incorrect. Are you using the 'merge' or 'concat' function?"
    msg = "Your dataframe contains the incorrect columns. Are you using the 'merge' or 'concat' function?\
    \nExpected ['day', 'description', 'day_temperature', 'night_temperature', 'pop','wind', 'hrs_sun', 'rain', 'temp_avg', 'wind_speed', 'wind_direction'], but got {0}".format(
        list(answer.columns))
    assert sorted(list(answer.columns)) == sorted([
        'day', 'description', 'day_temperature', 'night_temperature', 'pop',
        'wind', 'hrs_sun', 'rain', 'temp_avg', 'wind_speed', 'wind_direction'
    ]), msg
    assert set(answer.wind_direction) == {
        'S', 'SE', 'SW', 'W'
    }, "The values in the 'wind_direction' columns are incorrect. Are you the 'merge' or 'concat' function?"
    assert round(
        sum(answer.hrs_sun)
    ) == 59, "The values in the 'hrs_sun' columns are incorrect. Are you the 'merge' or 'concat' function?"
    return ("Success")
    return ("Success")


def test_6g(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert (answer.mark == 'line' or answer.mark.type == 'line'),"Make sure you are creating a line plot using the 'mark.line()' function."
    assert answer.encoding.x.shorthand == 'day' or answer.encoding.x.field == 'day', "Make sure you are plotting 'day' on the x-axis."
    assert answer.encoding.y.shorthand == 'wind_speed' or answer.encoding.y.field == 'wind_speed', "Make sure you are plotting 'wind_speed' on the y-axis."
    return ("Success")
