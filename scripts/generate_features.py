# Script to generate node features
import torch
import pandas as pd
from collections import defaultdict

def generate_node_features(df_file, G, all_nodes):
    user_feature_dict = defaultdict(lambda: [0, 0])

    for user in df_file['user'].unique():
        files = df_file[df_file['user'] == user]['file']
        user_feature_dict[user] = [len(files), len(set(files))]

    features = []
    for node in all_nodes:
        if G.nodes[node]['type'] == 'user':
            feat = user_feature_dict.get(node, [0, 0])
        else:
            feat = [0, 0]
        features.append(feat)

    return torch.tensor(features, dtype=torch.float)
