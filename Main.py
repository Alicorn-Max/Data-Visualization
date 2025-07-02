import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
pd.set_option('display.max_columns', None)
mtcars = pd.read_csv(r"C:\Users\tsara\Downloads\mtcars.csv")
from sklearn import datasets
#barplot
#res = sns.barplot(x="am", y="mpg", data=mtcars, palette="Set2")

#countplot
#sns.countplot(x='gear', hue='cyl', data=mtcars, palette="Set2")

#displot
#sns.displot(mtcars.mpg, bins =10, color ='r')

#heatmap
#numeric_cols = mtcars.select_dtypes(include=[np.number])
#sns.heatmap(numeric_cols.corr().corr(), cbar=True, linewidths=.5)


iris = sns.load_dataset("iris")

#scatterplot
#sns.scatterplot(x='sepal_length', y='petal_length', data=iris, hue='species', size='species')

#pairplot
#sns.pairplot(iris, hue="species", palette="viridis")

#Lmplot
#sns.lmplot(x="petal_length", y="petal_width", hue="species", data=iris, markers=['o','*', '^'], palette="Set2")

#boxplot
#sns.boxplot(x='species', y='sepal_width', data=iris)
sns.set_style("darkgrid")
palette = sns.cubehelix_palette(rot=.2,gamma=.5, dark=.25,light=1.5, reverse=True)
ax=sns.jointplot(x="petal_length", y="petal_width", data=iris, hue="species", palette=palette, height=20, marker=(4,1,0), s=500)
ax.set_axis_labels(xlabel='Petal Length', ylabel='Petal Width', fontsize=20)


st.header("Here is the visualization of the Iris dataset!")
st.pyplot(plt.gcf())
