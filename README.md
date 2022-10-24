# NBA PROJECT 🏀

## OBJECTIVE

The main goal of this project is to analyze a database with data about the 2021-22 NBA season. The initial questions are the following:

- Who are the most popular players?
- Which teams have the highest salaries?
- What are the differences in player's efficiency, salary and followers according to the player's position?
- What is the average age of the players?
- Is there any relationship between player efficiency, salary and followers?

## ACQUISITION

To perform the analysis, a CSV was obtained from [NBA stuffer](https://www.nbastuffer.com/2021-2022-nba-player-stats/) and python beautifulsoup module was used to web scraping the salaries from [HoopsHype](https://hoopshype.com/salaries/players/2021-2022/) and the Instagram followers from [Popular Basketballers](https://www.popularbasketballers.com/).

## WRANGLING

In order to clean the three dataframes and put them together, various functions have been used, saved in the [clean.py](src/clean.py) document.

The rest of the code can be found in the [main.ipynb](src/main.ipynb) document.

## ANALYSIS

**1. Who are the most popular players?**

In the following graph we can see that LeBron James clearly stands out, with more than 130 million followers, followed by Stephen Curry with more than 45 million. This big difference with the rest of the players may cause the data related to the followers not to be clearly visualized in the following analyses.

<img src="/images/graph_1.png">

**2. Which teams have the highest salaries?**

The graph below shows that the team with the highest average salary is the Golden State Warriors (current NBA champion), but the Boston Celtics, a team that reached the final, is in 15th place.

<img src="/images/graph_2.png">

**3. What are the differences in player's efficiency, salary and followers according to the player's position?**

The first graph shows the average efficiency of the players according to their position. Power forwards have the best average, followed by point guards and centers.

<img src="/images/graph_3.1.png">

If we focus on the salary, we can see that although the power forwards are the best paid, the centers (who have a high-efficiency average) are ones of the worst paid, together with the shooting guards.

<img src="/images/graph_3.2.png">

In the case of Instagram followers, we can see that small forwards clearly stand out (position where plays LeBron James), followed by point guards (position where plays Stephen Curry).

<img src="/images/graph_3.3.png">

**4. What is the average age of the players?**

In the following box plot we can see some data such as:

- The youngest player is 19 years (Joshua Primo)
- The oldest player is 41 (Udonis Haslem)
- The average age is 26 years
- 50% of the players are between 22 and 29

<img src="/images/graph_4.png"> 

**5 Is there any relationship between player efficiency, salary and followers?**

In the following plot, it can be seen that the efficiency of the players is positively related to the salary.

<img src="/images/graph_5.1.png"> 

In the case of followers, it could not be said that there is any kind of relationship with the salary.

<img src="/images/graph_5.2.png">

By putting the 3 variables together, it can be seen that salaries are much more related to player efficiency than to Instagram followers.

<img src="/images/graph_5.3.png">

## CONCLUSIONS

- The most popular player by far is LeBron James. It should be noted that apart from being a great basketball player, he is also known to be involved in social struggles or acting.
- The team with the highest average salary is Golden State Warriors. Current NBA champion and where Stephen Curry plays, the player with the highest NBA salary.
- Power forward is the position with the most efficient players and the highest salaries.
- Most NBA players are between 22 and 29 years old.
- There is no clear relationship between salaries and followers, but there is a clear relationship between salaries and player efficiency.