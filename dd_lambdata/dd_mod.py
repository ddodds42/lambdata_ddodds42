'''
Shortcut functions: work smart, not hard!
'''

def km_to_mile(km):
    '''
    converts kilometer values to mile equivalence
    '''
    mi = km / 1.60934
    return mi

def t_val_t(df):
    '''
    Splits a dataframe into train, vaidate, explore, and test sets
    '''
    from sklearn.model_selection import train_test_split
    explore, train = train_test_split(df)
    test, val = train_test_split(explore)
    return explore, test, val, train