# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:10:42 2022

@author: caberg
"""
# read ins
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
inodir = 'C:/Users/caberg/OneDrive - MetLife/Desktop/innovation challenge'
survey = pd.read_excel(inodir + '/MEET-MET Personality Matching Quiz(1-1).xlsx')


survey.columns[15]
survey['When you go somewhere for the day, would you rather'].unique()
survey['1'] = np.where(survey['When you go somewhere for the day, would you rather'].str.contains('Plan what you will do and when'), 1, 0)

survey['If you were a teacher, would you rather teach'].unique()
survey['2'] = np.where(survey['If you were a teacher, would you rather teach'].str.contains('Courses involving opinion or theory'), 1, 0)

survey['Are you usually'].unique()
survey['3'] = np.where(survey['Are you usually'].str.contains('Rather quiet and reserved'), 1, 0)

survey['Do you more often let'].unique()
survey['4'] = np.where(survey['Do you more often let'].str.contains('Your heart rule your head'), 1, 0)

survey['In doing something that many other people do, would you rather'].unique()
survey['5'] = np.where(survey['In doing something that many other people do, would you rather'].str.contains('Invent a way of your own'), 1, 0)

survey['Among your friends are you'].unique()
survey['6'] = np.where(survey['Among your friends are you'].str.contains('The last to hear what is going on'), 1, 0)

survey['Does the idea of making a list of what you should get done'].unique()
survey['7'] = np.where(survey['Does the idea of making a list of what you should get done'].str.contains('Help you'), 1, 0)

survey.columns[26]
survey['When you have a special job to do, do you like to\xa0'].unique()
survey['8'] = np.where(survey['When you have a special job to do, do you like to\xa0'].str.contains('Find out what is necessary as you go along'), 1, 0)

survey['Do you prefer to\xa0'].unique()
survey['9'] = np.where(survey['Do you prefer to\xa0'].str.contains('Be free to do whatever looks like fun'), 1, 0)

survey['Do you usually get along better with'].unique()
survey['10'] = np.where(survey['Do you usually get along better with'].str.contains('Imaginative people'), 1, 0)

survey['When you are with a group of people, would you rather'].unique()
survey['11'] = np.where(survey['When you are with a group of people, would you rather'].str.contains('Sit back and listen'), 1, 0)

survey['Is it a higher compliment to be called'].unique()
survey['12'] = np.where(survey['Is it a higher compliment to be called'].str.contains('A person of real feeling'), 1, 0)

survey['Do you'].unique()
survey['13'] = np.where(survey['Do you'].str.contains('Have a lot to say to only certain people'), 1, 0)

survey['Does following a schedule'].unique()
survey['14'] = np.where(survey['Does following a schedule'].str.contains('Structure you'), 1, 0)

survey['Are you more successful at'].unique()
survey['15'] = np.where(survey['Are you more successful at'].str.contains('Dealing with the unexpected'), 1, 0)

survey['Would you rather be considered\xa0'].unique()
survey['16'] = np.where(survey['Would you rather be considered\xa0'].str.contains('An out-of-the-box thinker'), 1, 0)

survey['In a large group, do you more often'].unique()
survey['17'] = np.where(survey['In a large group, do you more often'].str.contains('Get introduced'), 1, 0)

survey['Do you usually'].unique()
survey['18'] = np.where(survey['Do you usually'].str.contains('Value emotion more than logic'), 1, 0)




pca = PCA(n_components = 2, random_state=1)
principalComponents = pca.fit_transform(x)






