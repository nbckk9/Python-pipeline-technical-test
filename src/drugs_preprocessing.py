from src.utils import read_csv


def preprocess_drugs(file_path):
    """Preprocessing of the drug file

    Parameters:
    file_path (str): The path to the file to be preprocessed

    Returns:
    df (pandas.DataFrame): The preprocessed dataframe with the drugs list
    """
    drugs_df = read_csv(file_path)
    # We lowercase the drugs to for further processing
    drugs_df["drug"] = drugs_df["drug"].str.lower()

    # We could also add some duplicates cleaning here
    return drugs_df
