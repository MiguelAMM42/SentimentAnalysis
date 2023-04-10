from src.scraperV1 import scraperV1
from src.scraperV2 import scraperV2
from src.sentimentAnalysis import processData
from src.utils import storeData


weeks = [
    {'byear': '2023', 'bmonth': '04', 'bday': '02', 'eyear': '2023', 'emonth': '04', 'eday': '09'},
    {'byear': '2023', 'bmonth': '03', 'bday': '26', 'eyear': '2023', 'emonth': '04', 'eday': '01'},
    {'byear': '2023', 'bmonth': '03', 'bday': '19', 'eyear': '2023', 'emonth': '03', 'eday': '25'},
    {'byear': '2023', 'bmonth': '03', 'bday': '12', 'eyear': '2023', 'emonth': '03', 'eday': '18'},
    {'byear': '2023', 'bmonth': '03', 'bday': '05', 'eyear': '2023', 'emonth': '03', 'eday': '11'},
    {'byear': '2023', 'bmonth': '02', 'bday': '26', 'eyear': '2023', 'emonth': '03', 'eday': '04'},
    {'byear': '2023', 'bmonth': '02', 'bday': '19', 'eyear': '2023', 'emonth': '02', 'eday': '25'},
    {'byear': '2023', 'bmonth': '02', 'bday': '12', 'eyear': '2023', 'emonth': '02', 'eday': '18'},
    {'byear': '2023', 'bmonth': '02', 'bday': '05', 'eyear': '2023', 'emonth': '02', 'eday': '11'},
    {'byear': '2023', 'bmonth': '01', 'bday': '29', 'eyear': '2023', 'emonth': '02', 'eday': '04'},
    {'byear': '2023', 'bmonth': '01', 'bday': '22', 'eyear': '2023', 'emonth': '01', 'eday': '28'},
    {'byear': '2023', 'bmonth': '01', 'bday': '15', 'eyear': '2023', 'emonth': '01', 'eday': '21'},
    {'byear': '2023', 'bmonth': '01', 'bday': '08', 'eyear': '2023', 'emonth': '01', 'eday': '14'},
    {'byear': '2023', 'bmonth': '01', 'bday': '01', 'eyear': '2023', 'emonth': '01', 'eday': '07'},
    {'byear': '2022', 'bmonth': '12', 'bday': '25', 'eyear': '2022', 'emonth': '12', 'eday': '31'},
    {'byear': '2022', 'bmonth': '12', 'bday': '18', 'eyear': '2022', 'emonth': '12', 'eday': '24'},
    {'byear': '2022', 'bmonth': '12', 'bday': '11', 'eyear': '2022', 'emonth': '12', 'eday': '17'},
    {'byear': '2022', 'bmonth': '12', 'bday': '04', 'eyear': '2022', 'emonth': '12', 'eday': '10'},
    {'byear': '2022', 'bmonth': '11', 'bday': '27', 'eyear': '2022', 'emonth': '12', 'eday': '03'},
    {'byear': '2022', 'bmonth': '11', 'bday': '20', 'eyear': '2022', 'emonth': '11', 'eday': '26'},
    {'byear': '2022', 'bmonth': '11', 'bday': '13', 'eyear': '2022', 'emonth': '11', 'eday': '19'},
    {'byear': '2022', 'bmonth': '11', 'bday': '06', 'eyear': '2022', 'emonth': '11', 'eday': '12'},
    {'byear': '2022', 'bmonth': '10', 'bday': '30', 'eyear': '2022', 'emonth': '11', 'eday': '05'},
    {'byear': '2022', 'bmonth': '10', 'bday': '23', 'eyear': '2022', 'emonth': '10', 'eday': '29'},
]


def main():
    #query = "#chatgpt OR #AI min_replies:10 min_faves:100 min_retweets:100"
    #df = scraperV1(query, 1000)
    query = "(#chatgpt OR #AI) lang:en min_replies:1 min_faves:10 min_retweets:5"
    df = scraperV2(query, 50, weeks) 
    storeData("data/chatGPT_AI/scrappedData.csv", df)
    sentiments = processData(df)
    storeData("data/chatGPT_AI/processedData.csv", sentiments)



if __name__ == "__main__":
    main()