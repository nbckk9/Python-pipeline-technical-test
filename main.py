from src.clinical_trials_preprocessing import preprocess_trials
from src.drugs_preprocessing import preprocess_drugs
from src.pubmed_preprocessing import preprocess_pubmed
from src.graph_creation import graph_creation
import json


def main():
    # We preprocess the data
    trials_df = preprocess_trials("data/clinical_trials.csv")
    drugs_df = preprocess_drugs("data/drugs.csv")
    pubmed_df = preprocess_pubmed("Data/pubmed.csv", "Data/pubmed.json")
    # We create the graph
    output_graph = graph_creation(drugs_df, trials_df, pubmed_df)
    # We save the graph
    with open("Data/graph.json", "w") as outfile:
        json.dump(output_graph, outfile)


if __name__ == "__main__":
    main()
