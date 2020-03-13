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

class MetricConvert:
    '''
    This converter is designed to hopefully be useful for
    reproducing subclasses that are useful for a wide array of
    metric units. Temperature is the white elephant that most
    people are familiar with, celsius and fahrenheit do not share
    the same 0. They scale evenly, but have an awkward offset of
    32 degrees that should be addressable with the 'intr' variable (short for 'intercept'). Any other unit
    conversion with an aligned 0 point, such as length or weight,
    should set 'intr' equal to 0.
    '''
    def __init__(
                self, val_to_conv=None, intr=-32,
                old_unit="fahrenheit", coeff=(5/9),
                si_unit="celsius"
                ):
        self.val_to_conv = val_to_conv
        self.int = intr
        self.old_unit = old_unit
        self.coeff = coeff
        self.si_unit = si_unit
    
    def old_to_si(self, val_to_conv):
        '''
        convert the old clunky unit to S.I. (standard
        international, or metric)
        '''
        c = (self.intr + val_to_conv) * self.coeff
        return c
                # print(
                #     '{} {} equals {} {}'.format(
                #         c, self.si_unit,
                #         val_to_conv, self.old_unit
                #         )
                #     )

    def si_to_old(self, val_to_conv):
        '''
        convert the S.I. unit to the old clunky unit
        '''
        f = (val_to_conv / self.coeff) - self.intr
        return f
                # print(
                #     '{} {} equals {} {}'.format(
                #         f, self.old_unit,
                #         val_to_conv, self.si_unit
                #         )
                #     )