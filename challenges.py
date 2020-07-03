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
    # Base Case: If items = [], or capacity = 0, return 0.
    if len(items) == 0 or capacity <= 0:
        return 0
    # unpack the next item
    item, weight, value = items[0]
    # Define value_without := knapsack(items[1:], capacity)
    value_without = knapsack(items[1:], capacity)
    # if the weight exceeds cap, then default to value_without
    if weight > capacity:
        return value_without
    # Define value_with 
    value_with = value + knapsack(items[1:], capacity - weight)
    # Return max of the two
    return max(value_with, value_without)

   
def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows, cols = len(items) + 1, capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]
    # Fill in the table using a nested for loop.
    for item_index in range(1, len(dp_table)):
        row = dp_table[item_index]
        name, weight, item_value = items[item_index - 1]
        # iterate over a single row (all cols)
        for cap_index, cap_value in enumerate(row):
            # define knapsack with value, and without it
            value_without = dp_table[item_index - 1][cap_index]
            value_with = dp_table[item_index - 1][cap_index - weight] + item_value
            # choose the max
            dp_table[item_index][cap_index] = max(value_without, value_with)
    # return max value in table
    return dp_table[len(items) - 1][capacity]
    
def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    # Base Case: either str is empty
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    # Recursive Case 1: last letters match
    letter1, letter2 = str1[-1], str2[-1]
    if letter1 == letter2:
        # edit dist same as without those letters
        return edit_distance(str1[:-1], str2[:-1])
    # Recursive Case 2: last letters don't match
    elif letter1 != letter2:
        # determine next subproblem to solve
        next_subprob = min(
            edit_distance(str1[:-1], str2[:-1]),
            edit_distance(str1, str2[:-1]),
            edit_distance(str1[:-1], str2)
        )
        return next_subprob + 1
    

def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str2) + 1
    cols = len(str1) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]
    # fill in known subproblem #1 = first row
    dp_table[0] = list(range(cols))
    # fill in known subproblem #2 = first col
    str2_index = 0
    while str2_index < rows:
        dp_table[str2_index][0] = str2_index
        str2_index += 1
    # Fill in rest of table using nested for loop
    for str2_index in range(1, len(dp_table)):
        row = dp_table[str2_index]
        letter2 = str2[str2_index - 1]
        for col_index in range(1, cols):
            # initialize letters to compare
            letter1 = str1[col_index - 1]
            # compare letters and solve subproblem
            is_matching = (letter1 == letter2)
            subprob_without_these_letters = (
                dp_table[str2_index - 1][col_index - 1]
            )
            # if match found, do nothing
            if is_matching is True:
                operation_value = subprob_without_these_letters
            # otherwise add the least operation as an edit
            else:
                operation_value = (
                    min(subprob_without_these_letters,
                        dp_table[str2_index][col_index - 1],
                        dp_table[str2_index - 1][col_index]
                    ) + 1
                )
            # insert value into table
            dp_table[str2_index][col_index] = operation_value
    # return solution for whole problem
    return dp_table[rows-1][cols-1]


if __name__ == "__main__":
    cap = 50
    items1 = [
        # name, weight, value
        ('boots', 10, 60),   
        ('tent', 20, 100),
        ('water', 30, 120),
        ('first aid', 15, 70)
    ]
    assert knapsack(items1, cap) == 230
    print(knapsack(items1, cap))
