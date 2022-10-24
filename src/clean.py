# LIBRARIES

import requests
from bs4 import BeautifulSoup


# ------------------------------ IMPORTING AND CLEANING NBA Stats 2021/2022 CSV ------------------------------

# Creating a new subset and renaming columns

def new_subset(df):
    df_2 = df[['FULL NAME','TEAM','POS','AGE','TS%True Shooting PercentageTrue shooting percentage is a measure of shooting efficiency that takes into account field goals, 3-point field goals, and free throws.',
        'PPGPointsPoints per game.', 'RPGReboundsRebounds per game.','APGAssistsAssists per game.','SPGStealsSteals per game.', 'BPGBlocksBlocks per game.',
        'TOPGTurnoversTurnovers per game.']]
    df_2.rename(columns={'TS%True Shooting PercentageTrue shooting percentage is a measure of shooting efficiency that takes into account field goals, 3-point field goals, and free throws.': 'TS%',
                            'PPGPointsPoints per game.': 'PPG',
                            'RPGReboundsRebounds per game.': 'RPG',
                            'APGAssistsAssists per game.': 'APG',
                            'SPGStealsSteals per game.': 'SPG',
                            'BPGBlocksBlocks per game.': 'BPG',
                            'TOPGTurnoversTurnovers per game.': 'TOPG'},
            inplace=True)
    return df_2

#Converting numeric columns to floats

def floats(df_2):
    list_columns = ['AGE', 'TS%', 'PPG', 'RPG', 'APG', 'SPG', 'BPG', 'TOPG']
    for i in list_columns:
        df_2[i] = df_2[i].str.replace(',','.').astype(float)
    return df_2

# Calculating player efficiency

def player_eff(df_2):
    df_2['MPPG'] = (df_2['PPG'] * (1- df_2['TS%']))
    df_2['EFF'] = df_2['PPG'] + df_2['RPG'] + df_2['APG'] + df_2['SPG'] + df_2['BPG'] - df_2['TOPG'] - df_2['MPPG']
    return df_2

# Dropping unnecessary columns for analysis and cleaning the remaining columns

def drop_clean(df_2):
    df_2.drop(columns=['TS%','PPG','RPG','APG','SPG','BPG','TOPG','MPPG'], inplace=True)
    df_2['TEAM'] = df_2['TEAM'].replace('Tor','Toronto Raptors').replace('Mem','Memphis Grizzlies').replace('Mia','Miami Heat').replace('Bro','Brooklyn Nets').replace('Nor','New Orleans Pelicans').replace('Uta','Utah Jazz').replace('Mil','Milwaukee Bucks').replace('Cle','Cleveland Cavaliers').replace('Ind','Indiana Pacers').replace('Lal','Los Angeles Lakers').replace('Orl','Orlando Magic').replace('Nyk','New York Knicks').replace('Nor','New Orleans Pelicans').replace('Hou','Houston Rockets').replace('Was','Washington Wizards').replace('Pho','Phoenix Suns').replace('Sac','Sacramento Kings').replace('Det','Detroit Pistons').replace('Cha','Charlotte Hornets').replace('Chi','Chicago Bulls').replace('Atl','Atlanta Hawks').replace('Den','Denver Nuggets').replace('Phi','Philadelphia 76ers').replace('San','San Antonio Spurs').replace('Lac','Los Angeles Clippers').replace('Okc','Oklahoma City Thunder').replace('Min','Minnesota Timberwolves').replace('Dal','Dallas Mavericks').replace('Gol','Golden State Warriors').replace('Por','Portland Trail Blazers').replace('Bos','Boston Celtics')
    df_2['POS'] = df_2['POS'].replace('G','Point Guard (1)').replace('F','Small Forward (3)').replace('C','Center (5)').replace('C-F','Power Forward (4)').replace('F-C','Power Forward (4)').replace('F-G','Shooting Guard (2)').replace('G-F','Shooting Guard (2)')
    df_2['AGE'] = df_2['AGE'].astype(int)
    df_2.rename(columns={'POS': 'POSITION', 'EFF': 'EFFICIENCY'}, inplace=True)
    return df_2


# ------------------------------------------- WEB SCRAPING SALARIES ------------------------------------------

# Web scraping names

def names(soup):
    players = soup.find_all("td", attrs={"class": "name"})
    names_list = [i.getText().strip() for i in players]
    names_list.pop(0) # Deleting the first item of the list ('Player')
    return names_list

# Web scraping salaries

def salaries(soup):
    salary = soup.find_all("td", attrs={"style": "color:black"})
    salaries = [i.getText().strip().replace('$','').replace(',','') for i in salary]

    salaries_list = [] # Taking only the salaries adjusted with inflation
    count = 0
    for i in salaries:
        count += 1 
        if count % 2 == 0:
            salaries_list.append(int(i))

    return salaries_list


# ------------------------------------------ WEB SCRAPING FOLLOWERS ------------------------------------------

def followers(soup):
    players_f = soup.find_all("tr")
    players_f.pop(0) # Deleting headers

    name_fol = [i.getText().strip().replace(',','').split('\n') for i in players_f]

    full_name_list = [i[1] for i in name_fol]
    followers_list = [int(i[2]) for i in name_fol]

    return full_name_list, followers_list


# ----------------------------------------- CLEANING FINAL DATAFRAME -----------------------------------------

def clean_final(final_df):
    final_df.drop(columns=['full_name_1','full_name_2'], inplace=True)
    
    final_df.dropna(axis = 0, how = 'any', inplace=True)
    final_df.reset_index(drop=True, inplace=True)
    
    final_df['SALARY'] = final_df['SALARY'].astype(int)
    final_df['FOLLOWERS'] = final_df['FOLLOWERS'].astype(int)
    final_df['EFFICIENCY'] = final_df['EFFICIENCY'].round(0).astype(int)

    return final_df