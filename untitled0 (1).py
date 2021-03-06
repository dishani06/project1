# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UKcQxWPEkhxzeXDFOoWvGIEBGhD3HSec
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

df.info

"""Q1. Fill all the null values in the Age columns (Median)"""

df.isnull().sum()

"""Q2. Remove/delete the two null values from the Embarked column.

"""

df.dropna(thresh=2)

"""Q3. Tell the name of the Passanger, who is a female and she has survived, her age was b/w 20 - 30 and they belongs to the 1st class"""

name_of_the_femalePassenger = df[((df["Pclass"]==1) & (df["Survived"]==1) & (df["Sex"]=='female')  & (df["Age"]>=20)) & (df["Age"]<=30)]



name_of_the_femalePassenger  #list of female and age between 20- 30 who have survived in Pclass 1



name_of_the_femalePassenger.Name

name_of_the_femalePassenger.Name.iloc[0]

"""4.Visualise the Pclass who has Survived and Not Survived w.r.t the gender"""

sns.factorplot(x='Pclass',hue='Sex',col='Survived', kind='count', data=df)
plt.grid()