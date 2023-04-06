import pandas as pd
from transformers import pipeline
from tqdm import tqdm
import concurrent.futures
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from utils import loadData, storeData, dropColumns,languages

def joinReviewText(df):
    df["review_text"] = df["review_title"].astype(str) + " : " + df["review_body"].astype(str)
    df = df.drop(columns=["review_title","review_body"])
    return df


def getPartofDataset(df, perStarNr):
    df1 = df[df["stars"] == 1].sample(n=perStarNr, random_state=1)
    df2 = df[df["stars"] == 2].sample(n=perStarNr, random_state=1)
    df3 = df[df["stars"] == 3].sample(n=perStarNr, random_state=1)
    df4 = df[df["stars"] == 4].sample(n=perStarNr, random_state=1)
    df5 = df[df["stars"] == 5].sample(n=perStarNr, random_state=1)
    df = pd.concat([df1, df2, df3, df4, df5])
    return df




def translateData(df, translator):
    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        df.at[index, "review_text"] = translator(row["review_text"])[0]["translation_text"]
    return df


def processLanguage(language):
    df  = loadData(f"data/amazon_reviews_multi_{language.upper()}.csv")
    df = dropColumns(df,["product_id","reviewer_id","language"])
    df = joinReviewText(df)
    if language != "en":
        df = getPartofDataset(df, 20)
        tokenizer = AutoTokenizer.from_pretrained(f"Helsinki-NLP/opus-mt-{language}-en")
        model = AutoModelForSeq2SeqLM.from_pretrained(f"Helsinki-NLP/opus-mt-{language}-en")
        translator = pipeline("translation", model=model, tokenizer=tokenizer)
        translateData(df, translator)
    storeData(f"processedData/processed_amazon_reviews_multi_{language.upper()}.csv",df)


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        # Submit a new thread for each language
        futures = []
        for language in languages:
            futures.append(executor.submit(processLanguage, language))

        # Wait for all threads to complete
        for future in concurrent.futures.as_completed(futures):
            try:
                # Retrieve the result of the thread
                result = future.result()
            except Exception as exc:
                print(f'Language processing failed: {exc}')
            else:
                print(f'Language processing completed.')


if __name__ == "__main__":
    main()
