# NCAA March Madness 2020 Model

## Data Used
In past years I have tried using stats from each game to predict the winner of each game in the tournament. One downside of this approach is the large amount of data preprocessing needed to build an accurate model. A few things to consider include:

* Comparing the strength of conferences, (e.g. a team with a 21-10 record in the ACC is likely to be better than a team with a 21-10 record in the AAC)
* Adjusting for current roster strength, (e.g. a team with a star player who is injured is not as good as their records/stats show)
* Adjusting for team tendencies, (e.g. a fast-paced team will score more on average, but will be slowed down when facing a good defensive team)

Instead of doing this preprocessing, I decided to follow the approach of 538 and use polling data as my input data for the model. Pollsters account for all of these differences when selecting the top 25 each week. In addition, pollsters provide an excellent source of domain knowledge that I personally do not have. One downside of using polling data is that individual polls may be biased towards teams that were ranked highly at the beginning of the season. To account for this, I used 8 different polls.

One key data challenge is that polls are ordinal data. In most machine learning models, this implies that the difference between 1 and 2 in the polls is exactly the same as the difference between 24 and 25 in the polls. To help the model overcome this data challenge, I included the seed of the team as an input feature as well. Seeding data is also ordinal, however it provides another benchmark to differentiate teams. As an example:

* The number 1 team in the poll will have a poll ranking of 1 and a seed of 1.
* The number 2 team in the poll will have a poll ranking of 2 and a seed of 1.
* The number 5 team in the poll will have a poll ranking of 5 and a seed of 2.

Because there are now two levels of differentiation, the model can learn an interaction effect between these two ordinal levels. This allows for greater flexibility in the model to understand the difference between teams in terms of ranking, seeding, and the combination of the two.

## Machine Learning Model Used

I predicted the winner of each game of the NCAA March Madness 2020 tournament using a voting ensemble of the following models:

* Logistic Regression
* Support Vector Classification
* Gradient Boosting
* Random Forest

I found a significant increase in the cross-validation accuracy of my test set when using the voting ensemble compared to any one method. This finding is in line with 538's NCAA March Madness model.

## Results

Unfortunately, the tournament was cancelled due to Covid-19 so I wasn't able to compete with the model on Kaggle.
