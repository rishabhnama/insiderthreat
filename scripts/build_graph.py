# Script to build user-file graph

import pandas as pd
import networkx as nx
import os

def build_user_file_graph(file_path):
    df = pd.read_csv(file_path)
    G = nx.Graph()

    for _, row in df.iterrows():
        user = row['user']
        file = row['file']
        G.add_node(user, type='user')
        G.add_node(file, type='file')
        G.add_edge(user, file, activity=row['activity'], date=row['date'])

    return G

if __name__ == "__main__":
    G = build_user_file_graph("../data/file.csv")
    print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
