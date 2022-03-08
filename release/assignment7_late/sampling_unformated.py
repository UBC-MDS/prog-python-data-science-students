import pandas as pd


# +
def sample_dataframe(data, grouping_col, N = 1):
    """
    Given a dataframe, return a smaller sample of the dataframe
    sampling N rows from each specified group
    
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to sample from
    grouping_col : str
        The column to filter our condition on
    N : int, optional
        The number of rows to sample from each group (The default value is 1
        which implies a single observation)
        
    Returns
    -------
    pandas.core.frame.DataFrame
        The new sampled dataframe
        
    Examples
    --------
    >>> sample_dataframe(pokemon, 'legendary'])
        name     deck_no  attack  defense  type    gen  legendary
    411 Burmy     412     29        45      bug     4      0
    640 Tornadus  641     100       80      flying  5      1
    """
    
    df_grouped = data.groupby(grouping_col)
    
    sampled_df = None
    
    for group, rows in df_grouped: 
        group_sampling =  df_grouped.get_group(group).sample(N)
        sampled_df = pd.concat([sampled_df, group_sampling])
    
    return sampled_df


