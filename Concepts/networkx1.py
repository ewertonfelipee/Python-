import networkx as nx
import pandas as pd

df = pd.read_csv("bestsellerswithcategories.csv",
					header = None, names=['n1', 'n2', 'weight'])
					
G = nx.from_pandas_dataframe(df, 'n1', 'n2', edge_attr = 'weight')

print(list(G.edges(data = True)))
