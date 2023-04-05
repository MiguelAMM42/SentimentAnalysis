from datasets import load_dataset, concatenate_datasets


languages = ["de", "en", "es", "fr", "ja", "zh"]


def getData():
    datasets = {}
    for language in languages:
        dataset = load_dataset("amazon_reviews_multi", language)
        datasets[language] = dataset
    return datasets

def storeCSVs(datasets):
    for dataset in datasets.keys():
        print("Saving dataset: ", dataset)
        train = datasets[dataset]["train"]
        test = datasets[dataset]["test"]
        validation = datasets[dataset]["validation"]
        total = concatenate_datasets([train,test,validation])
        total.to_csv(f"data/amazon_reviews_multi_{dataset.upper()}.csv")

def main():
    datasets = getData()
    storeCSVs(datasets)


if __name__ == "__main__":
    main()