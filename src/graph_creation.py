from src.utils import add_journal, add_pubmed, add_trials
import re


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
    drugs_list = drugs_df["drug"].tolist()
    output_graph = graph_init(drugs_list)

    for index, row in trials_df.iterrows():
        # We compare the drug name with the words in each title
        for words in re.sub("[^\w]", " ", row["scientific_title"]).lower().split():
            if words in drugs_list:
                add_trials(
                    output_graph,
                    words,
                    row["scientific_title"],
                    row["date"].strftime("%d/%m/%Y"),
                )
                add_journal(
                    output_graph,
                    words,
                    row["journal"],
                    row["date"].strftime("%d/%m/%Y"),
                )

    for index, row in pubmed_df.iterrows():
        for words in re.sub("[^\w]", " ", row["title"]).lower().split():
            if words in drugs_list:
                add_pubmed(
                    output_graph,
                    words,
                    row["title"],
                    row["date"].strftime("%d/%m/%Y"),
                )
                add_journal(
                    output_graph,
                    words,
                    row["journal"],
                    row["date"].strftime("%d/%m/%Y"),
                )

    return output_graph
