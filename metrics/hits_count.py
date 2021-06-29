def hits_count(dup_ranks, k):
    """Precision@K
    
    Args:
        dup_ranks (list): list of guplicates
        k (int): Only consider the highest k scores in the ranking
    Return:
        Presicion at rank k
    """
    return np.mean(np.array(dup_ranks) <= k) 
