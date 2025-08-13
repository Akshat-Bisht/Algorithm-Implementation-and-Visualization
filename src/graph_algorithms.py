import networkx as nx

def build_graph_from_df(df):
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['Source'], row['Target'], weight=row.get('Distance', 1))
    return G

def shortest_path(G, source, target):
    return nx.dijkstra_path(G, source=source, target=target)