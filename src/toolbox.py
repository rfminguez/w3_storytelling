def unique_sorted_values_plus_ALL(array):
    '''
    receives: a list of elements.
    returns: a list of unique elements plus the value "ALL"

    code from:
    https://towardsdatascience.com/bring-your-jupyter-notebook-to-life-with-interactive-widgets-bc12e03f0916
    '''
    ALL = 'ALL'
    unique = array.unique().tolist()
    unique.sort()
    unique.insert(0, ALL)
    return unique

