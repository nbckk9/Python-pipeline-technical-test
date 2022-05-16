from src.utils import add_journal, add_pubmed, add_trials
import re
import pandas as pd


def graph_init(drugs_list):
    """Initialize the graph with the drugs as keys.

    Parameters:
    drugs_list (list): List of drugs extracted from data source

    Returns:
    output_graph (dict): Graph with drugs as keys.

    """
    output_graph = {}
    for drug in drugs_list:
        output_graph[drug] = {"pubmed": [], "trials": [], "journal": []}
    return output_graph


def graph_creation(drugs_df, trials_df, pubmed_df):
    """Processing of the data and creation of the graph.

    Parameters:
    drugs_df (pandas.DataFrame): Dataframe with drugs list
    trials_df (pandas.DataFrame): Dataframe with data extracted from the clinical_trials.csv file
    pubmed_df (pandas.DataFrame): Dataframe with data extracted from the pubmed.csv and pubmed.json file

    Returns:
    output_graph (dict): Graph with links between drugs and their respective mentions in clinical trials, medical publications and journals.
    """

    drugs_list = drugs_df["drug"].values.tolist()
    output_graph = graph_init(drugs_list)

    trials_titles = trials_df["scientific_title"].values
    trials_dates = pd.to_datetime(trials_df["date"].values)
    trials_journals = trials_df["journal"].values

    for i in range(len(trials_df)):
        for words in re.sub("[^\w]", " ", trials_titles[i]).lower().split():
            if words in drugs_list:
                add_trials(
                    output_graph,
                    words,
                    trials_titles[i],
                    trials_dates[i].strftime("%d/%m/%Y"),
                )
                add_journal(
                    output_graph,
                    words,
                    trials_journals[i],
                    trials_dates[i].strftime("%d/%m/%Y"),
                )

    pubmed_titles = pubmed_df["title"].values
    pubmed_dates = pd.to_datetime(pubmed_df["date"].values)
    pubmed_journals = pubmed_df["journal"].values

    for i in range(len(pubmed_df)):
        for words in re.sub("[^\w]", " ", pubmed_titles[i]).lower().split():
            if words in drugs_list:
                add_pubmed(
                    output_graph,
                    words,
                    pubmed_titles[i],
                    pubmed_dates[i].strftime("%d/%m/%Y"),
                )
                add_journal(
                    output_graph,
                    words,
                    pubmed_journals[i],
                    pubmed_dates[i].strftime("%d/%m/%Y"),
                )

    return output_graph
