#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 22:09:19 2020

@author: Elijah Willie

"""

def custom_agg(data, grouping_col,action_col, action = 'count'):
    import pandas as pd
    """
    Given a dataframe, a column and an action, return a dataframe that has been
    grouped by the column and a aggregate function applied.
    
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to sample from
    grouping_col : str
        The column to group the data on
    action_col : str
        After grouping, the column to applying th action to
    action : str, optional
        The action to apply to the specified action_col. The default is the 
        count action.      
        
    Returns
    -------
    pandas.core.frame.DataFrame 
        A dataframe with the group by column and the result of the action applied.
        
    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    AssertError
        If the input argument grouping_col is not in the data columns
    AssertError
        If the input argument action_col is not in the data columns
    
    Examples
    --------
    >>> custom_agg(helper_data, 'type')
	type	count
	Cherry	 4
    Oak	     6

    """
    
    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(data, pd.DataFrame): 
        raise TypeError("The data argument is not of type DataFrame")
    
    # Tests that the the grouping column is in the dataframe
    assert grouping_col in data.columns, "The grouping column does not exist in the dataframe"
    
    # Tests that the the action column is in the dataframe
    assert action_col in data.columns, "The action column does not exist in the dataframe"
    
    
    # compute the groupby object
    res = data.groupby(grouping_col)[action_col].agg([action])
    
    # convert to a dataframe
    res = pd.DataFrame(res)
    
    # reset the index
    res = res.reset_index()
    
    # return the result
    return(res)
    
    