import numpy as np
import pandas as pd
import psutil
from datetime import datetime



def get_evolution_coefficient(df, feature):
    """
    This function takes a dataframe and a feature and returns the evolution coefficient of the feature.
    :param df: dataframe
    :param feature: feature
    :return: evolution coefficient
    """

    if feature == 'mood':
        return ''
    X = np.arange(len(df))
    Y = df[feature].values
    p = np.polyfit(X, Y, 1)
    return p[0]

def detect_mood(avg_speed, avg_pressure, ratio_backspace):#, time_between_words, mouse_spammed, keyb_kick):
    """
    This function takes the features extracted from the user's typing and mouse movements and returns a mood prediction.
    :param avg_speed: average speed of the user's typing
    :param avg_pressure: average pressure of the user's typing
    :param time_between_words: average time between words
    :param ratio_backspace: ratio of backspace key pressed
    :param mouse_spammed: nb of times the mouse was spammed
    :param keyb_kick: nb of times 
    :return: mood prediction
    """

    # Get the system's uptime in seconds
    uptime_seconds = psutil.boot_time()

    # Convert uptime to a human-readable format
    boot_time = datetime.fromtimestamp(uptime_seconds)
    current_time = datetime.now()
    uptime = current_time - boot_time

    # We construct a new row with the features extracted from the user's typing and mouse movements
    new_row = pd.Series({'avg_speed': avg_speed, 'avg_pressure': avg_pressure,'ratio_backspace': ratio_backspace})#, 'time_between_words': time_between_words,'ratio_backspace': ratio_backspace, 'mood': ''}
    
    # We load the previous points of the user
    df = pd.read_csv('data/mood_user.csv')
    mood = df['mood'].iloc[-1]
    df = pd.concat([df,new_row], ignore_index=True)

    # We get the mood set 10 points before
    previous_mood = df['mood'].iloc[-10]
    

    # We compute the evolution coefficient of each feature
    evolution = {}
    for feature in df.columns:
        evolution[feature] = get_evolution_coefficient(df.iloc[:-10], feature)

    # Turn into a dictionary with the feature as key and the evolution coefficient as value
    evolution = dict(zip(df.columns, evolution.values()))

    # We now analyze these coefficients to predict the mood
    # If the user is typing slower and slower, he is probably tired
    if evolution['avg_speed'] < -1 and evolution['ratio_backspace'] < -1 and uptime.seconds > 14400:
        mood = 'tired'
    
    if evolution['avg_speed'] < -0.5 and evolution['ratio_backspace'] < -0.5 and evolution['avg_pressure'] < -0.5:
        if previous_mood == 'tired':
            mood = 'angry'
        if previous_mood == 'neutral':
            mood = 'tired'
        if previous_mood == 'happy':
            mood = 'neutral'

    '''if keyb_kick == 1:
        mood = 'angry'''

    
    # We now check if he is happier
    if evolution['avg_speed'] > 0.5 and evolution['ratio_backspace'] > 0.5 and evolution['avg_pressure'] > 0.5:
        if previous_mood == 'angry':
            mood = 'neutral'
        else:
            mood = 'happy'
    
    # We set the final mood
    df['mood'].iloc[-1] = mood
    df.to_csv('data/mood_user.csv')
    return mood
