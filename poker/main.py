"""
Poker game implementation
"""
# ToDo : royal flush


def card_ranks(hand):
    """
    :return: a list of sorted (from max) card weights
    """
    ranks = ["--23456789TJQKA".index(value) for value, suit in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks


def straight(ranks):
    """
    Checks if the hand is a straight

    :return: True or False
    """
    return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5


def flush(hand):
    """
    Checks if the hand is a flush

    :return: True or False
    """
    return len(set([suit for value, suit in hand])) == 1


def kind(n_times, ranks):
    """
    :return: weight of the n-times duplicated card in the hand or None
    """
    for rank in ranks:
        if ranks.count(rank) == n_times:
            return rank
    return None


def two_pairs(ranks):
    """
    :return: (max pair rank, min pair rank)
    """
    high_pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if high_pair and low_pair != high_pair:
        return [high_pair, low_pair]
    else:
        return None


def hand_rank(hand):
    """
    Compute hand rank
    """
    ranks = card_ranks(hand)

    if straight(ranks) and flush(hand):
        result = 8, max(ranks)
    elif kind(4, ranks):
        result = 7, kind(4, ranks), kind(1, ranks)
    elif kind(3, ranks) and kind(2, ranks):
        result = 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):
        result = 5, ranks
    elif straight(ranks):
        result = 4, max(ranks)
    elif kind(3, ranks):
        result = 3, kind(3, ranks), ranks
    elif two_pairs(ranks):
        result = 2, two_pairs(ranks), ranks
    elif kind(2, ranks):
        result = 1, kind(2, ranks), ranks
    else:
        result = 0, ranks
    return result


def all_max(iterable, key=None):
    """
    :param iterable: to find max
    :param key: of how to choose max
    :return: a list of all items equal to the max element of the iterable
    """
    result, max_val = [], None

    # Use provided key function or map x to x
    key = key or (lambda x: x)

    for item in iterable:
        item_val = key(item)
        if not result or item_val > max_val:
            result, max_val = [item], item_val
        elif item_val == max_val:
            result.append(item)
    return result


def poker(hands):
    """
    Return the best hands: poker([hand, ...]) => [hand, ...]
    """
    return all_max(hands, key=hand_rank)
