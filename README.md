# UEFA Champions League Predictor
Based on last 5 years of UEFA Champions League group stage records, the machine learning model tried to predict the outcome of some teams participating in the League based on their performance in the Group Stage only.

The model predicted stage, which each team can reach in the season 2019-20. Simple **Random Forest Classification Model** is used in this project.

<br>

## Predictions for the season 2019-20

|Stage                |Stage          |
|---------------------|:-------------:|
|Real Madrid          |Round of 16    |
|Barcelona            |Quarter Finals |
|Bayern Munich        |Semi Finals    |
|Tottenham Hotspur    |Finals         |
|Manchester City      |Quarter Finals |
|Juventus             |Quarter Finals |
|Atlético Madrid          |Finals         |
|Liverpool            |Quarter Finals |
|Borussia Dortmund    |Round of 16    |
|Chelsea              |Quarter Finals |
|Paris Saint-Germain  |Finals         |


<br>

## About the data

All the datasets used in this project were made manually *(well, actually using web scraping)* and, can be found [here](/data).

Data consists of Group Stage information from the past 5 years in UEFA Champions League, of some selected high-rated teams only. Datasets are from the seasons **2014-15, 2015-16, 2016-17, 2017-18 and 2018-19**.

<br>

#### Following teams were selected for the project
- Real Madrid
- FC Barcelona
- Bayern Munich
- Tottenham Hotspur 
- Manchester City
- Juventus
- Atlético Madrid
- Liverpool
- Borussia Dortmund
- Chelsea
- Paris Saint-Germain

<br>

#### Standing of each of these teams in the past years were also collected and, converted into a number using the following table

|Stage            |Integer Representation   |
|-----------------|:-----------------------:|
|Group Stage      |1                        |
|Round of 16      |2                        |
|Quarter Finals   |3                        |
|Semi Finals      |4                        |
|Finals           |5                        |

<br>

## Steps to setup the project locally

- Clone the repository
- Create a python virtual environment, run `python3 -m virtualenv venv && source venv/bin/activate`
- Install all the required dependencies, run `pip install -r requirement.txt`
- Input the details of whatever team you want to predict future for in `src/prediction.py` and, simply run the python script `python3 src/prediction.py`.
- Make sure you print the predictions or else you won't see the result of the model.
