from src.utils import read_csv, read_json, harmonize_dates
import pandas as pd


def preprocess_pubmed(csv_file_path, json_file_path):
    """Preprocessing of the pubmed files

    Parameters:
    csv_file_path (str): The path to the csv file to be preprocessed
    json_file_path (str): The path to the json file to be preprocessed


    Returns:
    df (pandas.DataFrame): The preprocessed dataframe with the concatenated pubmed data
    """

    pubmed_csv_df = read_csv(csv_file_path)
    pubmed_csv_df["date"] = pubmed_csv_df["date"].apply(harmonize_dates)

    pubmed_json_df = read_json(json_file_path)
    pubmed_json_df["date"] = pubmed_json_df["date"].apply(harmonize_dates)

    # We concatenate the two dataframes
    pubmed_df = pd.concat([pubmed_csv_df, pubmed_json_df])

    return pubmed_df
