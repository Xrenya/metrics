def dcg_score(dup_ranks, k):
    """Discounted cumulative gain (DCG) is a measure of ranking quality.
    
    Using a graded relevance scale of documents in a search-engine result set,
    DCG measures the usefulness, or gain, of a document based on its position
    in the result list. The gain is accumulated from the top of the result list
    to the bottom, with the gain of each result discounted at lower ranks.
    
    Args:
        dup_ranks (list): list of guplicates
        k (int): Only consider the highest k scores in the ranking
    Return:
        Discounted Cumulative Gain (DCG) at rank k
    """
    ranks = np.array(dup_ranks)
    return np.mean(1 / np.log2(1 + ranks) * (ranks <= k))
  
