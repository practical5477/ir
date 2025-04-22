import numpy as np

def pagerank(graph, damping_factor=0.85, max_iterations=100, epsilon=1e-8):
    num_pages = len(graph)
    initial_page_rank = np.ones(num_pages) / num_pages
    teleportation_prob = (1 - damping_factor) / num_pages

    page_rank = initial_page_rank.copy()

    for _ in range(max_iterations):
        prev_page_rank = page_rank.copy()

        for i in range(num_pages):
            incoming_links = np.where(graph[:, i] == 1)[0]
            sum_page_rank = np.sum(prev_page_rank[incoming_links] / len(incoming_links)) if incoming_links.size > 0 else 0
            page_rank[i] = teleportation_prob + damping_factor * sum_page_rank

        # Check for convergence
        if np.linalg.norm(page_rank - prev_page_rank, 1) < epsilon:
            break

    return page_rank

if __name__ == "__main__":
    # Example web graph (adjacency matrix)
    web_graph = np.array([
        [0, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ])

    # Calculate PageRank
    page_rank_scores = pagerank(web_graph)

    # Display results
    for i, score in enumerate(page_rank_scores):
        print(f"Page {i + 1}: PageRank Score = {score:.4f}")
