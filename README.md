Titanic: How many survived?
-----------------------------

The sinking of the Titanic is one of the most infamous shipwrecks in history. On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew. While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others. 

Our goal is to predict if a passenger survived the sinking of the Titanic or not. So, we will perform data analysis on this dataset. The Titanic dataset has the following features:

VARIABLE DESCRIPTIONS:

survival        Survival

                (0 = No; 1 = Yes)
                
pclass          Passenger Class

                (1 = 1st; 2 = 2nd; 3 = 3rd)
                
name            Name

sex             Sex

age             Age

sibsp           Number of Siblings/Spouses Aboard

parch           Number of Parents/Children Aboard

ticket          Ticket Number

fare            Passenger Fare

cabin           Cabin

embarked        Port of Embarkation

                (C = Cherbourg; Q = Queenstown; S = Southampton)


Data Exploration & Cleaning
-----------------------------

The first part of any data analysis or predictive modeling task is an initial exploration of the data. Even if you collected the data yourself and you already have a list of questions in mind that you want to answer, it is important to explore the data before doing any serious analysis, since oddities in the data can cause bugs and muddle your results. Before exploring deeper questions, you have to answer many simpler ones about the form and quality of data. That said, it is important to go into your initial data exploration with a big picture question in mind since the goal of your analysis should inform how you prepare the data.

Friendly guidance: https://www.youtube.com/watch?v=IxxGqoOksJ4. The final dataset is formatted like this: ![dataset_final](https://user-images.githubusercontent.com/37047286/232353434-039cc9cb-b2a8-4422-8fec-2527ca41935c.PNG)



Results
-----------------------------

Random Forest Classifier model was used to predict the Titanic survivors. In training achieved accuracy score 98.8%, f1 score 98.37%, precision score 99.59% and recall score 97.19%. In testing achieved accuracy score 79.37%, f1 score 73.56%, precision score 77.11% and recall score 70.33%.
