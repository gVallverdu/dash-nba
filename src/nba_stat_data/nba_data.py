# coding: utf-8

from pathlib import Path
import pandas as pd
import plotly.express as px

__all__ = ["df_nba", "nba_scatter", "nba_pivot_table"]


def read_data_nba(filename):
    """ Read NBA data from the given filename 

    Args:
        filename (str): path to the data file

    Returns
        A data Frame
    """
    df = pd.read_csv(
        filename,
        index_col=0,
        dtype={"Year": "int"}
    )

    # manage data
    df = df.assign(bmi=df.weight / ((df.height / 100) ** 2))
    df = df[["Year", "height", "weight",
             "bmi", "PER", "PTS", "pos_simple"]].copy()

    return df


# read data file
data_file = Path(__file__).parent / "nba_physiques.csv"
df_nba = read_data_nba(data_file)


def nba_scatter(df, xvalue, yvalue):
    """ Make a scatter plot using the NBA data 

    Args:
        df (pandas.DataFrame): the NBA data frame
        xvalue (str): column name for x
        yvalue (str): column name for y

    Returns
        A figure object
    """
    figure = px.scatter(
        df,
        x=xvalue, y=yvalue,
        color='pos_simple',
        category_orders=dict(pos_simple=['PG', 'SG', 'SF', 'PF', 'C']),
        marginal_x="histogram",
        marginal_y="histogram",
        template="plotly_white",
    )

    return figure


def nba_pivot_table(df, value):
    """ Make a pivot table from NBA data.

    Args:
        df (pandas.DataFrame): the NBA data frame
        value (str): column name for averaging in the pivot table

    Returns
        data to fill in a dash_table
    """

    # create bins from height columns
    df = df.assign(height_bins=pd.qcut(df.height, q=4))

    pivot_df = pd.pivot_table(
        data=df, values=value, columns="pos_simple", index="height_bins"
    )
    pivot_df = pivot_df.reset_index()
    pivot_df = pivot_df.astype({"height_bins": "str"})

    return pivot_df
