def top_n(items, n):
    """Returns the top n items from the array

    Args:
        items (array): list or array-like objects
        n (int): num of items to return

    Return:
        array: top n items, in desc order

    Egs:
        >>> top_n([6,7,8,2,4,1], 3) == [8,7,6]
    """
    for i in range(n):
        for j in range(len(items)-1-i):

            if items[j] > item[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
   
    #get last two items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]