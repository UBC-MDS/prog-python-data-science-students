from hashlib import sha1
import pandas as pd
import pytest
import altair
import sys
import numpy as np

def test_1_1(answer1,answer2,answer3,answer4):
    assert not answer1 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not answer2 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not answer3 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not answer3 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert str(type(answer1)) == "<class 'pandas.core.series.Series'>", "Make sure your passing in a pandas series object."
    assert str(type(answer2)) == "<class 'pandas.core.series.Series'>", "Make sure your passing in a pandas series object."
    assert str(type(answer3)) == "<class 'pandas.core.series.Series'>", "Make sure your passing in a pandas series object."
    assert str(type(answer4)) == "<class 'pandas.core.series.Series'>", "Make sure your passing in a pandas series object."
    assert answer1.shape == (10000,), "The dimensions of the training set is incorrect. Are you splitting correctly?"
    assert answer2.shape == (10000,), "The dimensions of the test set is incorrect. Are you splitting correctly"
    assert answer3.shape == (10000,), "The dimensions of the training set is incorrect. Are you splitting correctly? Are you using single brackets?"
    return("Success")

def test_1_2(answer):
    answer = list(answer)
    assert sha1(str(answer[0]).encode('utf8')).hexdigest() == 'f8237d8959e03355010bb85cc3dc46a46fb31110', "The number of positive cases is incorrect. The count function might be useful."
    assert sha1(str(answer[1] + 7).encode('utf8')).hexdigest() == 'e30861784ef1cabed9fa83f93382d9c96013ace7', "The number of negative cases is incorrect. The count function might be useful."
    return("Success")

def test_1_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer + 'm').encode('utf8')).hexdigest() == "4cd7920fdd3598ce4b7635b6879d03af8ca0fdb1", "Your answer is incorrect. Are you checking using .info()?"
    return("Success")

def test_1_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert 'review_wordcount' in answer.columns, "Make sure you are adding the review_wordcount to the dataframe."
    assert len(answer['review_wordcount']) == 10000, "Make sure you are adding the review_wordcount column to the dataframe."
    assert min(answer['review_wordcount']) == 10, "The minimum word count is incorrect. Are you counting properly?"
    assert max(answer['review_wordcount']) == 1723, "The maximum word count is incorrect. Are you counting properly?"
    return("Success")

def test_1_5_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(int(answer)).encode('utf8')).hexdigest() == "5b7d26c4d99b922929b7c30ce06be0fd58a71500","The average positive word count is incorrect. Are you using the mean function?"
    return("Success")

def test_1_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    try:
        answer.mark.type == "bar", "Your plot is not a bar plot. Make sure you are using the 'mark_bar()' function"
    except AttributeError as error:
        assert answer.mark == "bar", "Your plot is not a bar plot. Make sure you are using the 'mark_bar()' function"
    assert 'label' in str(answer.encoding.x.shorthand) or 'label' in str(answer.encoding.x.field), "Make sure you are plotting the `label` variable on the x-axis."
    assert 'review_wordcount' in str(answer.encoding.y.shorthand) or 'review_wordcount' in str(answer.encoding.y.field), "Make sure you are plotting the `review_wordcount` variable. on the y-axix"
    assert not answer.title == 'Undefined', "Make sure you are providing a title for the plot."
    return("Success")

def test_1_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (5, 4), "The dimensions of you solution is incorrect. Are you setting up the model correctly?"
    assert sorted(list(answer.columns)) == ['fit_time', 'score_time', 'test_score', 'train_score'], "Your dataframe contains the incorrect columns. Are you setting up the model correctly?"
    assert min(answer['test_score']) == 0.5 and max(answer['test_score']) == 0.5, "The range of your test scores is incorrect. Are you specifying the dummy classifier?"
    assert min(answer['train_score']) == 0.5 and max(answer['train_score']), "The range of your training scores is incorrect. Are you specifying the dummy classifier?"
    return("Success")

def test_1_8():
    assert 'sklearn' in sys.modules, "Make sure you are importing 'plot_confusion_matrix' and 'classification_report' from the sklearn module."
    return("Success")

def test_1_9(answer1, answer2):
    assert not answer1 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not answer2 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert 'CountVectorizer(max_features=100)' in str(answer1.get_params()['steps']), "Make sure you are including count vectorizer with 100 features as part of your pipeline"
    assert 'LogisticRegression(max_iter=2000)' in str(answer1.get_params()['steps']), "Make sure you are including LogisticRegression with 2000 iterations as part of your pipeline"
    assert sorted(list(answer2.columns)) == ['fit_time', 'score_time', 'test_score', 'train_score'], "Your dataframe contains the incorrect columns. Are you setting up the model correctly?"
    return("Success")

def test_1_10(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert round(answer,2)['test_score'] == 0.73, "The average test score is incorrect. Are you taking the mean?"
    assert round(answer,2)['train_score'] == 0.74, "The average train score is incorrect. Are you taking the mean?"
    return("Success")

def test_1_11(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + 'w').encode('utf8')).hexdigest() == "8a85c06c4eba8aba733a4be991bd4b4c6b4e4581", "Your answre is incorrect. Are you analysing the models correctly?"
    return("Success")

def test_1_12_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == 'afe08934db435cd1eab0c1fc63c2e21d1101c16d', "Your answer is incorrect. Are you reviewing these models?"
    return("Success")

def test_1_12_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(answer.lower().encode('utf8')).hexdigest() == '67bed8a8994bdcc6f3026e959ce5f5c3cf09efba', "Your answer is incorrect. Are you reviewing these models?"
    return("Success")

def test_1_13(answer):
    case_1 = sha1(answer.lower().encode('utf8')).hexdigest() == "c807a3ee37a900a97e217e3734285cc85e24c56d"
    case_2 = sha1(answer.lower().encode('utf8')).hexdigest() == "42efe213754e10a4f1332ca356d3f2832e0145b5"
    assert (case_1 or case_2),  "Your answer is incorrect. What is the effect of C on the model?"
    return("Success")

def test_1_14(answer1,answer2):
    assert not answer1 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert not answer2 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert 'CountVectorizer()' in str(answer1.get_params()['steps']), "Make sure you are including count vectorizer as part of your pipeline"
    assert 'LogisticRegression' in str(answer1.get_params()['steps']), "Make sure you are including LogisticRegression as part of your pipeline"
    assert answer2.get_params()['n_iter'] == 10, "Make sure you are specifying the correct number of iterations."
    assert answer2.get_params()['return_train_score'] == True, "Make sure you are returing the training scores."
    assert answer2.get_params()['random_state'] == 888, "Make sure you are using the correct random state."
    return("Success")

def test_1_15_2(answer1, answer2):
    assert not answer2 is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert round(answer1.best_score_,4) == round(answer2, 4), "Your value for the optimal score is incorrect. Are you using the .best_score_ function?"
    return("Success")

def test_1_16(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + 'e').encode('utf8')).hexdigest() == "1eabdaf488b3a3682bbca94c5f468f065cdfaf13", "Your answre is incorrect. Are you analysing the results correctly?"
    return("Success")

def test_2_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert 'max_features=874' in str(list(answer)), "Your best model is incorrect. Are you using the best_estimator_ function?"
    assert 'C=0.0340' in str(list(answer)), "Your best model is incorrect. Are you using the best_estimator_ function?"
    return("Success")

def test_2_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer[0]) == 874, "The number of coefficient is incorrect. Are you using the coef_ function?"
    assert round(min(answer[0]),2) == -1.07, "Some coefficient values are incorrect. Are you using the coef_ function?"
    assert round(max(answer[0]),2) == 0.68, "Some coefficient values are incorrect. Are you using the coef_ function?"
    return("Success")

def test_2_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert len(answer) == 874, "The number of features are incorrect. Are you using the get_feature_names function?"
    assert sha1(str(sorted(answer)).encode('utf8')).hexdigest() =='ca83ca2c0d1bf91315117d2bbaa9c63def3c31bc', "The features are incorrect. Are you using the get_feature_names function."
    return("Success")

def test_2_4(answer):
    assert answer.shape == (10, 2), "The dimensions of your dataframe is incorrect. Are you selecting the top 10 positive words?"
    assert list(answer.loc[760])[0] == 'today', "Your dataframe contains incorrect values. Are you sorting in the correct order?"
    assert list(answer.loc[231])[0] == 'excellent', "Your dataframe contains incorrect values.  Are you sorting in the correct order?"
    assert list(answer.loc[439])[0] == 'loved', "Your dataframe contains incorrect values.  Are you sorting in the correct order?"
    return("Success")

def test_2_5(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (10, 2), "The dimensions of your dataframe is incorrect. Are you selecting the top 10 negative words?"
    assert list(answer.loc[854])[0] == 'worst', "Your dataframe contains incorrect values. Are you selecting the top 10 negative words?"
    assert list(answer.loc[89])[0] == 'boring', "Your dataframe contains incorrect values. Are you selecting the top 10 negative words?"
    assert list(answer.loc[351])[0] == 'horrible', "Your dataframe contains incorrect values. Are you selecting the top 10 negative words?"
    return("Success")

def test_2_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(len(answer)).encode('utf8')).hexdigest() == "77de68daecd823babbb58edb1c8e14d7106e83bb", "The number of correct answers is incorrect. Please try again."
    answer = [x.lower() for x in answer]
    assert sha1(str(sorted(answer)).encode('utf8')).hexdigest() == "e52bfee75467f61d74e9663e71da1c898699d2ed", "Your answer is incorrect. Are you analyzing the answers carefully? Is there more than one correct answer?"
    return("Success")

def test_3_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(round(answer,2)).encode('utf8')).hexdigest() == "431c7e0f059354f8237990cf99466704cc85f23a", "Your training score is incorrect. Are you scoring using the best model?"
    return("Success")

def test_3_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1((answer.lower() + 'i').encode('utf8')).hexdigest() == "5a4fe08359c7f97380e408c717ef42c86939cd86", "Your answer is incorrect. Are comparing the models correctly?"
    return("Success")

def test_3_4(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert str(type(answer)) == "<class 'sklearn.metrics._plot.confusion_matrix.ConfusionMatrixDisplay'>", "Make sure you are generating a confusion matrix plot"
    return("Success")

def test_3_5_1(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(round(answer, 2)).encode('utf8')).hexdigest() == "15e4f66808acb4ab8ac72b8c56eba22310069e7f", "Your value for recall is incorrect. Are you examining the classification report?"
    return("Success")

def test_3_5_2(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(round(answer, 2)).encode('utf8')).hexdigest() == "1284d7d1d642ef8e51475cce5c1972ca6b8bd2b6", "Your value for the weighted precision average is incorrect. Are you examining the classification report?"
    return("Success")

def test_3_5_3(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sha1(str(round(answer, 2)).encode('utf8')).hexdigest() == "1284d7d1d642ef8e51475cce5c1972ca6b8bd2b6", "Your value for the f1 score is incorrect. Are you examining the classification report?"
    return("Success")

def test_3_6(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (10000, 5), "The dimensions of your dataframe is incorrect."
    assert sorted(list(answer.columns)) == ['neg_label_prob', 'pos_label_prob', 'predicted_y', 'review', 'true_label'], "ncorrect column names. Make sure you are specifying the required columns."
    assert list(answer['predicted_y']).count('neg') == 4863 or list(answer['predicted_y']).count('neg') == 4862, "The predicted number of negative reviews is incorrect. Are you predicting correctly?"
    assert list(answer['predicted_y']).count('pos') == 5137 or list(answer['predicted_y']).count('pos') == 5138, "The predicted number of positive reviews is incorrect. Are you predicting correctly?"
    return("Success")

def test_3_7(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (5, 5), "The dimensions of your dataframe is incorrect."
    assert sorted(list(answer.columns)) == ['neg_label_prob', 'pos_label_prob', 'predicted_y', 'review', 'true_label'], "Your dataframe contains incorrect columns. Make sure you are specifying the required columns."
    assert list(answer['predicted_y']).count('neg') == 0, "The predicted number of negative reviews is incorrect. Are you taking the top positive reviews"
    assert list(answer['predicted_y']).count('pos') == 5, "The predicted number of positive reviews is incorrect. Are you taking the top positive reviews?"
    assert min(list(answer['pos_label_prob'])) > 0.99 and max(list(answer['pos_label_prob'])) > 0.99, "The range of the probability values are incorrect. Make sure you are selecting the top positive reviews."
    return("Success")

def test_3_8(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.shape == (5, 5), "The dimensions of your dataframe is incorrect."
    assert sorted(list(answer.columns)) == ['neg_label_prob', 'pos_label_prob', 'predicted_y', 'review', 'true_label'], "Your dataframe contains incorrect columns. Make sure you are specifying the required columns."
    assert list(answer['predicted_y']).count('neg') == 5, "The predicted number of negative reviews is incorrect. Are you taking the top negative reviews"
    assert list(answer['predicted_y']).count('pos') == 0, "The predicted number of positive reviews is incorrect. Are you taking the top negative reviews?"
    assert min(list(answer['neg_label_prob'])) > 0.99 and max(list(answer['neg_label_prob'])) > 0.99, "The range of the probability values are incorrect. Make sure you are selecting the top negative reviews."
    return("Success")

def test_3_9(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert sorted(list(answer.columns)) == ['neg_label_prob','pos_label_prob','predicted_y','prob_diff','review','true_label'], "Your dataframe contains incorrect column names."
    assert list(answer['predicted_y']).count('neg') + list(answer['predicted_y']).count('pos') == 5, "The number of predicted negative and positive reviews is incorrect"
    return("Success")

def test_3_10(answer):
    assert not answer is None, "Your answer does not exist. Have you passed in the correct variable?"
    assert answer.iloc[0,1] != answer.iloc[0,2], "Your answer is incorrect. Please try again."
    return("Success")
