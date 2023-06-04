from get_counts_dict import get_counts_dict


def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_counts = get_counts_dict(s)
    t_counts = get_counts_dict(t)

    s_unique_letters = s_counts.keys()
    t_unique_letters = t_counts.keys()

    if len(s_unique_letters) != len(t_unique_letters):
        return False

    for c in s_counts:
        if c not in t_counts:
            return False
        if s_counts[c] != t_counts[c]:
            return False

    return True
