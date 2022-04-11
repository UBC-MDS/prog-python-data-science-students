from hashlib import sha1
import pandas as pd
import pytest
import sys
from decimal import Decimal
import inspect

def test_1a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "ac5b9a895584d5b47a3072d11c4116a9a1fe97ee", "The value for clothing is incorrect. Are you setting up the conditionals properly?"
    return("Success")

def test_1b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "b2b49807429fe76fc54b0f3ab85f97eb9f2b496b", "The value for size is incorrect. Are you setting up the conditionals properly?"
    return("Success")

def test_1c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "35a14b140d57ee762921022522818ee219473828", "Your answer is incorrect. Please try again."
    return("Success")

def test_1d(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "50c9e8d5fc98727b4bbc93cf5d64a68db647f04f", "Your answer is incorrect. Please try again."
    return("Success")

def test_1f(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer + "k").encode('utf8')).hexdigest() == "a7d0008d025f37434b7cd8c853384cd610f6d92c", "Your answer is incorrect. Please try again."
    return("Success")

def test_1g(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "1d9b230e46d9e6f99820e00c8cea3a333c839671", "The value for dinner is incorrect. Are you setting up the conditionals properly?"
    return("Success")

def test_2a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(
        answer
    ) == 13, "The length of your answer is incorrect. Are you appending all the words to a list?"
    msg = "Your list contains the incorrect words. Are you appending the words to a list? \
    \nExpected ['For', 'every', 'word', 'in', 'this', 'sentence,', 'print', 'the', 'word','on', 'its', 'own', 'line'], but got {0}".format(
        list(answer))
    assert sorted(list(answer)) == sorted([
        'For', 'every', 'word', 'in', 'this', 'sentence,', 'print', 'the',
        'word', 'on', 'its', 'own', 'line'
    ]), msg
    return ("Success")

def test_2b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer) == 18, "The length of your answer is incorrect. Are you iterating over all the items?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "19c6241a5373a6bfaf08f42557a9f1efe640bbae", "The values in ingredient_stock are incorrect. Are you setting up the forloop properly?"
    return("Success")

def test_2d(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(round(answer)).encode('utf8')).hexdigest() == "77de68daecd823babbb58edb1c8e14d7106e83bb", "Your answer is incorrect. Are you dividing by the length?"
    return("Success")

def test_2e(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(round(answer)).encode('utf8')).hexdigest() == "da4b9237bacccdf19c0760cab7aec4a8359010b0", "Your answer is incorrect. Are you setting up your loop properly?"
    return("Success")

def test_2f(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer) == 5, "The length of your dictionary is incorrect. Are you setting up your loop and conditionals properly?"
    keys_sorted = sorted(list(answer.keys()))
    assert sha1(str(keys_sorted).encode('utf8')).hexdigest() == "7db2e0930ed769a0e13892fb3a618c42f2db8462", "The keys in your dictionary are incorrect. Are you setting up your loop and conditionals properly?"
    assert sha1(str(answer[keys_sorted[0]]+16).encode("utf8")).hexdigest() == "9e6a55b6b4563e652a23be9d623ca5055c356940", "The number of items on the shopping list for one of the ingredients is incorrect."
    assert sha1(str(answer[keys_sorted[1]]+8).encode("utf8")).hexdigest() == "17ba0791499db908433b80f37c5fbc89b870084b", "The number of items on the shopping list for one of the ingredients is incorrect."
    assert sha1(str(answer[keys_sorted[2]]+7).encode("utf8")).hexdigest() == "fe5dbbcea5ce7e2988b8c69bcfdfde8904aabc1f", "The number of items on the shopping list for one of the ingredients is incorrect."
    assert sha1(str(answer[keys_sorted[3]]+2).encode("utf8")).hexdigest() == "1b6453892473a467d07372d45eb05abc2031647a", "The number of items on the shopping list for one of the ingredients is incorrect."
    assert sha1(str(answer[keys_sorted[4]]+10).encode("utf8")).hexdigest() == "17ba0791499db908433b80f37c5fbc89b870084b", "The number of items on the shopping list for one of the ingredients is incorrect."
    return("Success")

def test_3a(answer):
    answer = sorted(answer)
    case1 = (sha1(str(answer[0].lower()).encode("utf8")).hexdigest() == "357fe2e7c6e4365947196f3193885d1203174a12")
    case2 = (sha1(str(answer[1].lower()).encode("utf8")).hexdigest() == "b19406c18e1d40d8b138119ae7e99a4edbf8481d")
    case3 = (sha1(str(answer[2].lower()).encode("utf8")).hexdigest() == "b19406c18e1d40d8b138119ae7e99a4edbf8481d")
    case4 = (sha1(str(answer[3].lower()).encode("utf8")).hexdigest() == "6ec2d47f3bbcd9acdc286b8c83f81c49184bb4be")
    total_correct = sum([case1, case2, case3, case4])
    assert  total_correct == 4, "You have {0} correct answers and {1} incorrect answers".format(total_correct, 4 - total_correct)
    return("Success")

def test_3b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    answer = sorted(answer)
    case1 = (sha1(str(answer[0].lower()).encode("utf8")).hexdigest() == "357fe2e7c6e4365947196f3193885d1203174a12")
    case2 = (sha1(str(answer[1].lower()).encode("utf8")).hexdigest() == "b19406c18e1d40d8b138119ae7e99a4edbf8481d")
    case3 = (sha1(str(answer[2].lower()).encode("utf8")).hexdigest() == "b19406c18e1d40d8b138119ae7e99a4edbf8481d")
    case4 = (sha1(str(answer[3].lower()).encode("utf8")).hexdigest() == "6ec2d47f3bbcd9acdc286b8c83f81c49184bb4be")
    total_correct = sum([case1, case2, case3, case4])
    assert  total_correct == 4, "You have {0} correct answers and {1} incorrect answers".format(total_correct, 4 - total_correct)
    return("Success")


def test_4a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "9e6a55b6b4563e652a23be9d623ca5055c356940", "Your answer is incorrect. Are you reading the nested loop properly?"
    return("Success")

def test_4b(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer) == 3, "The length of your dictionary is incorrect. Are you setting up your loop and conditionals properly?"
    assert sha1(str(list(answer.keys())).encode('utf8')).hexdigest() == "cc7372cfe80a04d3104bec411c58bc43f5d47271", "The keys in your dictionary are incorrect. Are you setting up your loop and conditionals properly?"
    assert sha1(str(list(answer.values())).encode('utf8')).hexdigest() == "a6c9d40507e08e8f60572583f929c17619e0203d", "The values in your dictionary are incorrect. Are you setting up your loop and conditionals properly?"
    
    return("Success")

def test_5a(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(answer).encode('utf8')).hexdigest() == "d2ba7416e4995e025e3a6fcb781d9728cbd00e5f", "Your answer is incorrect. Are you setting your function and conditionals properly?"
    return("Success")

def test_5c(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer) == 9, "The length of your dictionary is incorrect. Are you setting up your loop and conditionals properly?"
    assert sha1(str(list(answer.keys())).encode('utf8')).hexdigest() == "2df66bbcc227015e2e5f941df65f73b1ad3ae05d", "The keys in your dictionary are incorrect. Are you setting up your loop and conditionals properly?"
    assert sha1(str(list(answer.values())).encode('utf8')).hexdigest() == "77cc5b00ed6bbd0400b97de495ceaf1b46649c98", "The values in your dictionary are incorrect. Are you setting up your loop and conditionals properly?"
    return("Success")

def test_5d(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    dict1 = {'bread': 5, 'peanut butter': 3,
          'flour': 7}
    dict2 = {'eggs': 2, 'vanilla': 2, 'sugar': 3,
                'flour': 2, 'eggs': 2}
    res = answer(dict1, dict2)
    assert sha1(str(res).encode('utf8')).hexdigest() == "e3a6de1097ddaae1ab41be3d1e25dfa3f50f479c", "Your function output is incorrect. Please examine your function and try again."
    return("Success")

def test_5e(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer) == 6, "The length of your dictionary is incorrect. Are you setting up your function properly?"
    assert sha1(str(list(answer.keys())).encode('utf8')).hexdigest() == "4fe94dae421429155f4a9eae286f79ac623b1eb7", "The keys in your function's output are incorrect. Are you setting up your loop and conditionals in your function properly?"
    assert sha1(str(list(answer.values())).encode('utf8')).hexdigest() == "ae769f11adc0df819ce4cc71f64a46943030b15a", "The values in your function's output are incorrect. Are you setting up your loop and conditionals in your function properly?"
    return("Success")
