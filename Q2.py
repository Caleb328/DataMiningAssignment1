import networkx as nx

G = nx.read_adjlist('cit-Patents.small.txt')
pr_scores = nx.pagerank_scipy(G)

ranked_nodes = sorted(pr_scores, key=pr_scores.get, reverse=True)
for node in ranked_nodes[:10]:
    print "%s: %.8f" % (node, pr_scores[node])