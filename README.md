# lambdata_ddodds42
Unit 3, Sprint 1

'''
install from https://test.pypi.org/project/ddodds/0.1.1/
pip install -i https://test.pypi.org/simple/ ddodds==0.1.1
'''

'''
Created MetricConvert, a class to modify functions that convert between SI (standard international, or metric) and non-SI units. (dd_mod.py)

In dd_mod.py, the function km_to_mile converts km values into miles.

The function t_val_t splits a dataframe into 4 parts; explore, train, test, and val. Explore and test are split from the original dataframe, train
and val are split from explore, in case cross validation is not
employed. In the use of CV, the explore and test set are the only
two needed.

Requires sklearn and pandas.
'''