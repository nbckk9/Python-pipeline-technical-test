import pandas as pd
import dateutil.parser


def read_csv(csv_path):
    df = pd.read_csv(csv_path)
    return df


def harmonize_dates(x):
    return dateutil.parser.parse(x, dayfirst=True)


def read_json(json_path):
    df = pd.read_json(json_path, convert_dates=False)
    return df


def add_journal(graph, drug, title, date):
    journal_dict = {"title": title, "date": date}
    if journal_dict not in graph[drug]["journal"]:
        graph[drug]["journal"].append(journal_dict)
    return graph


def add_pubmed(graph, drug, title, date):
    pubmed_dict = {"title": title, "date": date}
    if pubmed_dict not in graph[drug]["pubmed"]:
        graph[drug]["pubmed"].append(pubmed_dict)
    return graph


def add_trials(graph, drug, title, date):
    trials_dict = {"title": title, "date": date}
    if trials_dict not in graph[drug]["trials"]:
        graph[drug]["trials"].append(trials_dict)
    return graph
