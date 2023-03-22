# Motivation and Purpose

Our role: A data scientist consultancy firm.

Target audience: People who are enthusiastic NBA fans and are interested
in comparing and learning skills of NBA players.

NBA or National Basketball Association is the most famous professional
Basketball league in the world. It consists of 30 professional
basketball teams with approximately 500 players playing per season.

The motivation behind this project is to help NBA fans better understand
their favorite players and visualize how the players have performed compared to other players.
Since the NBA has a long history, NBA fans can compared NBA players from previous decades with the current NBA players
and see how they perform in term of each offensive and defensive skills

On the other hand, we can also honor and learn those former NBA
superstars, such as Micheal Jordan and Kobe Bryant, by visualizing their
performances. For instance, Kobe Bryant, we can learn about the wonders
the legendary superstar created with the Lakers and the glory of the
purple and gold dynasty with scored 33,643 points, 7,047 rebounds, and
6,306 assists during the entire career. Salute to the eternal Lakers
#24.

# Description of the data

The NBA player stats data for the regular season will be retrieved from [The NBA Player Data in Kaggle](https://www.kaggle.com/datasets/drgilermo/nba-players-stats?select=Seasons_Stats.csv).
Also the glossary of each statistics is provided [here](https://www.basketball-reference.com/about/glossary.html).


The data contains of 15,116 statistics of 2,417 NBA players among 30 NBA teams during 1950-2017.

The data features will be used for this application are as followings:

1. The player name; `Name`

2. The year of that statistic; `Year`

3. Number of game played; `Game`

4. Offensive statistics
 - `Field Goal Percentage(FGp)`
 - `Free Throw Percentage(FTp)`
 - `3-Point Percentage(3Pp)`
 - `Offensive Rebound Percentage(ORBp)`
 - `Assist Percentage(ASTp)`.

5. Defensive statistics
 - `Block Percentage(BLKp)`
 - `Defensive Rebound Percentage(DRBp)`
 - `Steal Percentage(STLp)`.


# Primary research question and usage scenarios

The project aims to answer the following primary question:

`How compare the top NBA players such as Micheal Jordan and Kobe Bryant?`

`In what skills Micheal Jordan is better Kobe Bryant?`

`How did these players perform over times?`

Below is an example of a usage scenario from a member of our target
audience.

Florencia is an enthusiastic NBA fan who usually loves to learn, study, and compare NBA players.
There are some options available on the internet to obtain the player information,
such as searching particular players through Wikipedia pages, checking
historical data from NBA official website, sporting news websites, and
[The Basketball Reference website](https://www.basketball-reference.com/), etc. 

However, she found that it was time-consuming and less effective to find her interested player information in a
well-organized way from these websites. Either she had to read paragraphs 
or a massive table to extract interested data by herself, or there was less
control to customize the visualizations to make her own conclusions.

By using `NBA Player Comparison` visualization, 
now Florencia can effectively and efficiently search a pair of her interested NBA players and draw insights from the app. 
When she enters a pair of players to compare, such as `Micheal Jordan` and `Kobe Bryant`, 
she can immediately the last 5-year statistics of each player.
Then she have a control over offensive skill and defensive skill of the players to compare.
She can select an offensive skill such as `Field Goal Percentage(FGp)`, `Free Throw Percentage(FTp)`, `3-Point Percentage(3Pp)`, `Offensive Rebound Percentage(ORBp)`, and `Assist Percentage(ASTp)` to compare.
Also, she can select an defensive skill such as `Block Percentage(BLKp)`, `Defensive Rebound Percentage(DRBp)`, and `Steal Percentage(STLp)` to compare.
Therefore, she can compare and analyze skill of players in each different category and she can draw a conclusion efficiently and effectively.

