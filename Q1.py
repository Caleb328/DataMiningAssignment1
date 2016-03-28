import networkx as nx

# Draw the graph
G = nx.DiGraph()
G.add_nodes_from([1,2,3,4])
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 1)])

#Calcualte the page ranks
pr_scores = nx.pagerank_scipy(G, alpha=0.8, max_iter=10000)

ranked_nodes = sorted(pr_scores, key=pr_scores.get, reverse=True)
for node in ranked_nodes:
    print "%s, %.8f" % (node, pr_scores[node])