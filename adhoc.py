import json


def drug_mentions_journal(json_file):
    data = json.load(open(json_file))

    journal_mentions = []
    for drug, values in data.items():
        unique_mentions = []
        for journal in values["journal"]:
            if journal["title"] not in unique_mentions:
                unique_mentions.append(journal["title"])

        journal_mentions = journal_mentions + unique_mentions
        unique_mentions = []

    # It only return the first journal with the maximum mentions of different drugs, but it could be improved by returning all journals with the maximum mentions of different drugs
    return max(journal_mentions, key=journal_mentions.count)


def main():
    print(drug_mentions_journal("Data/graph.json"))


if __name__ == "__main__":
    main()
