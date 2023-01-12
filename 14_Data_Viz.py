import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks",color_codes=True )
big_ship=sns.load_dataset("titanic")
# print(big_ship) shows available  dataset for titatnic


# PLOT BASIC GRAPH with 1 Var
p=sns.countplot(x="sex", data=big_ship)
plt.show()

# PLOT Graph with 02 Var (here comes the hue option)
p=sns.countplot(x="sex", data=big_ship, hue="class")
plt.show()

# PLOT Graph with 02 Var (here comes the hue option) with TITLE of the Graph
p=sns.countplot(x="sex", data=big_ship, hue="class")
p.set_title("TITANIC PLOT FOR COUNTING")
plt.show()