import xgb
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

import language_tool_python
import nltk

tool = language_tool_python.LanguageTool('en-US')
is_bad_rule = lambda rule: rule.message == 'Possible spelling mistake found.' and len(rule.replacements) and rule.replacements[0][0].isupper()



def load_data_training():
    df_free = pd.read_csv('data/free_text_typing_dataset.csv', sep=';')
    df_freq = pd.read_csv('data/frequency_dataset.csv', sep=';')
    df_user = pd.read_csv('data/participants_information.csv', sep=';')

    df_free = df_free.rename(columns={'userid':'userId'})
    df_freq = df_freq.rename(columns={'User ID':'userId'})

    return df_free, df_freq, df_user

# functions to extract features from the df_free table
def extract_editDistance_free(sentence):
    matches = tool.check(sentence)
    matches = [rule for rule in matches if not is_bad_rule(rule)]
    correct = language_tool_python.utils.correct(sentence, matches)
    return nltk.edit_distance(sentence, correct)

def extract_nbKeystroke(val, start, end):
    return val[end] - val[start] + 1

def extract_mean(val, start, end):
    return np.mean(val[start:end+1])

def extract_std(val, start, end):
    return np.std(val[start:end+1])

def preprocess_loading(df_free, df_freq, df_user, is_train):

    text_free = pd.DataFrame(columns=['sentence', 'idx_start', 'idx_end'])

    df_free.keyCode = df_free.keyCode.astype(str)

    
    df_free = df_free.drop(['D1U3','D1D3','answer'], axis=1)
    df_free.head()

    df_free[['D1U1','D1U2','D1D2','U1D2','U1U2']]  = df_free[['D1U1','D1U2','D1D2','U1D2','U1U2']].map(lambda x: float(str(x).replace(',', '')) if isinstance(x, str) else x)

    key_features = ['D1U1','D1U2','D1D2','U1D2','U1U2']

    text_free['userId'] = df_free.userId[text_free.idx_start].values
    text_free['emotionIndex'] = df_free.emotionIndex[text_free.idx_start].values
    text_free = text_free.reindex(columns=['emotionIndex'])

    text_free['editDistance'] = text_free.apply(lambda x: extract_editDistance_free(x['sentence']), axis=1)
    text_free['nbKeystroke'] = text_free.apply(lambda x: extract_nbKeystroke(df_free.index, x['idx_start'], x['idx_end']), axis=1)

    for feat in key_features:
        df_free[feat] = df_free[feat].apply(lambda x: np.nan if np.abs(x) > 1570000000000 else x)
        text_free[feat+'_mean'] = text_free.apply(lambda x: extract_mean(df_free[feat], x['idx_start'], x['idx_end']), axis=1)
        text_free[feat+'_std'] = text_free.apply(lambda x: extract_std(df_free[feat], x['idx_start'], x['idx_end']), axis=1)

    # filter free-text experiments in df_freq
    df_freq_free = df_freq[df_freq.textIndex == 'FR'].reset_index(drop=True)

    # correction of expections to align df_freq_free and text_free tables
    text_free.loc[43,'userId'] = 94
    tmp = text_free.loc[29]
    text_free.loc[29] = text_free.loc[30]
    text_free.loc[30] = tmp

    # alignment of df_freq_free and text_free tables
    text_free['text_index'] = -1
    df_freq_free['text_index'] = -1
    index = 0

    i = 0
    j = 0
    while i<len(df_freq_free) and j<len(text_free):
        if (is_train and (df_freq_free.userId[i] == text_free.userId[j] and df_freq_free.emotionIndex[i] == text_free.emotionIndex[j])) \
        or (not is_train and df_freq_free.userId[i] == text_free.userId[j]):
            df_freq_free.loc[i,'text_index'] = index
            text_free.loc[j,'text_index'] = index
            index += 1
            i += 1
            j += 1
        elif (is_train and (j != len(text_free)-1 and df_freq_free.userId[i] == text_free.userId[j+1] and df_freq_free.emotionIndex[i] == text_free.emotionIndex[j+1]))\
        or (not is_train and (j != len(text_free)-1 and df_freq_free.userId[i] == text_free.userId[j+1])):
            df_freq_free.loc[i,'text_index'] = index
            text_free.loc[j+1,'text_index'] = index
            index += 1
            i += 1
            j += 2
        elif (is_train and (i != len(df_freq_free)-1 and df_freq_free.userId[i+1] == text_free.userId[j] and df_freq_free.emotionIndex[i+1] == text_free.emotionIndex[j])) \
        or (not is_train and (i != len(df_freq_free)-1 and df_freq_free.userId[i+1] == text_free.userId[j])):
            df_freq_free.loc[i+1,'text_index'] = index
            text_free.loc[j,'text_index'] = index
            index += 1
            i += 2
            j += 1
        else:
            i += 1
            j += 1

    # correction of expections to align df_freq_free and df_user tables
    tmp = df_user.loc[10]
    df_user.loc[10] = df_user.loc[11]
    df_user.loc[11] = tmp
    tmp = df_user.loc[70]
    df_user.loc[70] = df_user.loc[71]
    df_user.loc[71] = tmp
    tmp = df_user.loc[91]
    df_user.loc[91] = df_user.loc[92]
    df_user.loc[92] = tmp

    # alignment of df_freq_free and df_user tables
    df_freq_free['user_index'] = -1
    index = 0

    j = 0
    for i in range(len(df_freq_free)):
        if i in [20,38,58,68,129,139,150,154,173,225,227]: 
            j += 1
        if j < len(df_user) and df_freq_free.userId[i] == df_user.userId[j]:
            df_freq_free.loc[i,'user_index'] = j
            i += 1
        else:
            if j < len(df_user)-1 and df_freq_free.userId[i] == df_user.userId[j+1]:
                df_freq_free.loc[i,'user_index'] = j+1
                i += 1
                j += 1
            else:
                for k in range(1,7):
                    if df_freq_free.userId[i] == df_freq_free.userId[i-k]:
                        df_freq_free.loc[i,'user_index'] = df_freq_free.loc[i-k,'user_index']
                        break

    # merge all tables
    df_free_all = df_freq_free.join(text_free, on='text_index', how='left', rsuffix='_right')
    if (is_train):
        df_free_all = df_free_all.drop(['emotionIndex_right'], axis=1)

    df_free_all = df_free_all.drop(['userId_right', 'text_index_right', 'answer'], axis=1)
    df_free_all = df_free_all.join(df_user.reset_index().rename(columns={'index':'user_index'}), on='user_index', how='left', rsuffix='_right')
    df_free_all = df_free_all.drop(['user_index_right','userId_right'], axis=1)

    return df_free_all

def preprocess_model(df_free_all, is_train):
    if (is_train):
        data_free = df_free_all.loc[:,df_free_all.columns.difference(['emotionIndex'])]
        label_free = df_free_all.emotionIndex.map({'N':0,'H':1,'C':2,'S':3,'A':4})

    data_free = df_free_all.loc[:,df_free_all.columns.difference(['user_index','userId','textIndex','TotTime','text_index','idx_start','idx_end','sentence'])]
            
    # convert categorical features into numerical features
    data_free.gender = (data_free.gender == 'Male')
    data_free.ageRange = data_free.ageRange.map({'16-19':1,'20-29':2,'30-39':3,'>=50':4})
    data_free.degree = data_free.degree.map({'High School':1, 'College/University':2})
    data_free.pcTimeAverage = data_free.pcTimeAverage.map({'less than an hour per day':1, 'between 1 hour and 3 hours per day':2, 'More than 3 hours per day':3})
    data_free.status = data_free.status.map({'Student':1, 'Professional':2})
    data_free.typeWith = data_free.typeWith.map({'1 hand':1, '2 hands':2})
    data_free = pd.get_dummies(data_free, columns=['country','typistType'])
    data_free = data_free.fillna(-1)

    if (is_train):
        return data_free, label_free
    else:
        return data_free, -1

def scaler(X, y):
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X, y)
    return X, scaler

def preprocess_train():
    df_free, df_freq, df_user = load_data_training()
    df_free_all = preprocess_loading(df_free, df_freq, df_user)
    data_free, label_free = preprocess_model(df_free_all)
    data_free, scaler_free = scaler(data_free, label_free)
    return data_free, label_free, scaler_free


def train():
    X_train, Y_train, scaler_free = preprocess_train()
    model = xgb.XGBClassifier(objective='multi:softmax', eval_metric='mlogloss',use_label_encoder=False)
    model.fit(X_train, Y_train)
    return model, scaler_free

def preprocess_test(df_free, df_freq, df_user, scaler_free):
    df_free_all = preprocess_loading(df_free, df_freq, df_user)
    data_free, _ = preprocess_model(df_free_all)
    data_free = scaler_free.transform(data_free)
    return data_free

def load_data_test():
    df_free = pd.read_csv('data/free_text_typing_test.csv', sep=';')
    df_freq = pd.read_csv('data/frequency_test.csv', sep=';')
    df_user = pd.read_csv('data/participants_information.csv', sep=';')

    df_free = df_free.rename(columns={'userid':'userId'})
    df_freq = df_freq.rename(columns={'User ID':'userId'})

    return df_free, df_freq, df_user

def test():
    df_free, df_freq, df_user = load_data_training()
    model, scaler_free = train()
    X_test = preprocess_test(df_free, df_freq, df_user, scaler_free)
    Y_pred = model.predict(X_test)
    print(Y_pred)