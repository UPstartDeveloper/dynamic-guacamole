class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]: # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else: # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # Fill in the table using a nested for loop.
    for i, array_row in enumerate(dp_table):  # each row is an array
        for j, elem_col in enumerate(array_row):  # each col is an element in an array
            # fill the first row and column all thr way through with zeros
            if i == 0 or j == 0:
                dp_table[i][j] = 0
            # fill in each row, by comparing every letter of A, with each 
            # subsequent letter of B
            elif strA[i - 1] != strB[j - 1]:
                # if not matching, look up and to the left, take the bigger
                dp_table[i][j] = max(dp_table[i][j - 1], dp_table[i - 1][j])
            elif strA[i - 1] == strB[j - 1]:
                # if match, increment the value of the num in upper left
                dp_table[i][j] = 1 + dp_table[i - 1][j - 1]

    return dp_table[rows-1][cols-1]

def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    """
    base case: 
    - if no items or no cap, return 0
    - total weight in the knapsack is >= capacity:
        return the value so far, (without the overflow)

    recursive case: 
    weight of single item is > capacity:
        "skip" the item
    weight in the total knapsack is < capacity:
        so need to grab more items
            For each item - grab the best value of permutations involving that item
        pass over it
    """
    pass

def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    """
    cap: 50
    items1 = [
        # name, weight, value
        ('boots', 10, 60),   
        ('tent', 20, 100),
        ('water', 30, 120),
        ('first aid', 15, 70)
    ]
    Exp Out: 230
    
        0   1   2    3    4    5   6   7  8 ... 51
    0
    1
    2
    3
    4
    5
    """

    # TODO: Fill in the table using a nested for loop.

    return dp_table[rows-1][cols-1]
    
def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    pass

def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.

    return dp_table[rows-1][cols-1]
