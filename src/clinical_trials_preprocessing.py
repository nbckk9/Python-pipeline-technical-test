from src.utils import read_csv, harmonize_dates


def preprocess_trials(file_path):
    """Preprocessing of the drug file

    Parameters:
    file_path (str): The path to the file to be preprocessed

    Returns:
    df (pandas.DataFrame): The preprocessed dataframe with cleaned clinical trials data
    """
    trials_df = read_csv(file_path)

    # We harmonize the dates to make sure that the dates are in the same format.
    trials_df["date"] = trials_df["date"].apply(harmonize_dates)

    # We remove the unicode characters
    # We could find a better way to do this rather than using a replace function to remove all eventual characters not those specified
    trials_df["scientific_title"] = trials_df["scientific_title"].apply(
        lambda x: x.replace("\\xc3", "").replace("\\xb1", "")
    )
    trials_df["journal"] = (
        trials_df["journal"]
        .astype(str)
        .apply(lambda x: x.replace("\\xc3", "").replace("\\x28", ""))
    )

    # Find a way to merge similar rows

    return trials_df
