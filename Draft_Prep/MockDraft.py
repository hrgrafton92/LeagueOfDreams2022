import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import altair as alt
import matplotlib.patches as mpatches


#import projections
hitters = pd.read_csv("hitter_projections2.csv")
hitters = hitters[hitters["AB"]>99]
pitchers = pd.read_csv("pitcher_projections2.csv")
pitchers = pitchers[pitchers["IP"]>49.9]
all = pd.read_csv("all_projections2.csv")
all = all.drop(all[(all.AB < 100) & (all.AB > 0)].index)
all = all.drop(all[(all.IP < 50) & (all.IP > 0)].index)

#trim down to only 5x5 categories
all_trimmed = all.drop(['AB','OBP','SLG','OPS','K_%','B_%','IP','ER','H','BB','HR_all','HR_perc','BB_perc','K_perc'], axis=1)
#Hitter projections scatterplot. all projections

"""
# The Draft Is Upon Us

The lockout is over. Trades are happening. Spring training is on deck.

League Of Dreams 2022 is around the corner. While the final details of draft date & time, along with a few league format debates to iron out, we are set to begin a new season.
While we wait, here is a simple tool to help you all brainstorm some specific players you'd like to target.

Choose different pairings of stats to plot below for both hitters and pitchers. Find some outliers that catch your eye. These are *projections* not 2022, not their 2021 stats. (Anyone with fewer than 100 ABs or 50 IP was excluded.)
Then further below, map out which players in each round you would *ideally* draft if they are available in that spot. Be hopeful, but be realistic. And remember to plug your keepers into their proper round.
As you select players a running tally will be kept of all their projected 2022 stats. Compare this to a target goal of team stats for the season. The target stats were determined by guidance from various sources online (SI, fantrax, rotowire, fantasypros, etc) aiming for totals that would have finished in the 80th percentile of most leagues last year. I would have used our own league totals from last year to aim for but given the weekly lineup nature of our league, our own teams had their stat totals supressed.

Due to the inexact nature of the target stats, they shouldn't be viewed as a challenge to beat. But rather as a guardrail to keep your roster generally balanced. It'll show if you get too imbalanced while pursuing any given strategy.

Experiment with taking pocket aces early, punting on certain categories, or any other variation of draft strategy. Test the depth of different positions. Can you get away with waiting on 3rd base? Can you find good pitchers late if you load up on bats early?

Make sure to keep roster positional requirements in mind. Can't leave the draft with any vacant positions. 


"""

selected_x_var = st.selectbox('What category you want the x variable to be? (Cannot be Name)', hitters.columns)
selected_y_var = st.selectbox('What about the y? (Cannot be Name)', hitters.columns)

hitters_final = pd.DataFrame()
hitters_final = hitters[[selected_x_var,selected_y_var,"Name"]]


x_name = selected_x_var
y_name = selected_y_var
tooltip_name = 'Name'
xx = hitters_final[[x_name]]
yy = hitters_final[[y_name]]


hitters_fun = alt.Chart(hitters_final, title = x_name+" vs "+y_name).mark_circle().encode(
    x = x_name,
    y = y_name,
    tooltip = "Name")

st.altair_chart(hitters_fun,use_container_width=True)

#Pitcher projections scatterplot. all projections
selected_x_var_P = st.selectbox('What category you want the x variable to be? (Cannot be Name)', pitchers.columns,key=2)
selected_y_var_P = st.selectbox('What about the y? (Cannot be Name)', pitchers.columns,key=2)

pitchers_final = pd.DataFrame()
pitchers_final = pitchers[[selected_x_var_P,selected_y_var_P,"Name"]]


x_name_P = selected_x_var_P
y_name_P = selected_y_var_P
tooltip_name_P = 'Name'
xx_P = pitchers_final[[x_name_P]]
yy_P = pitchers_final[[y_name_P]]


fun_P = alt.Chart(pitchers_final, title = x_name_P+" vs "+y_name_P).mark_circle().encode(
    x = x_name_P,
    y = y_name_P,
    tooltip = "Name")

st.altair_chart(fun_P,use_container_width=True)

#Player selections for all 26 rounds of draft. Show all 5x5 categories
player_1 = st.selectbox('Select a player to draft in Round 1:', all_trimmed.Name)
round_1 = all_trimmed[all_trimmed['Name']==player_1]

player_2 = st.selectbox('Select a player to draft in Round 2:', all.Name)
round_2 = all_trimmed[all_trimmed['Name']==player_2]

player_3 = st.selectbox('Select a player to draft in Round 3:', all.Name)
round_3 = all_trimmed[all_trimmed['Name']==player_3]

player_4 = st.selectbox('Select a player to draft in Round 4:', all.Name)
round_4 = all_trimmed[all_trimmed['Name']==player_4]

player_5 = st.selectbox('Select a player to draft in Round 5:', all.Name)
round_5 = all_trimmed[all_trimmed['Name']==player_5]

player_6 = st.selectbox('Select a player to draft in Round 6:', all.Name)
round_6 = all_trimmed[all_trimmed['Name']==player_6]

player_7 = st.selectbox('Select a player to draft in Round 7:', all.Name)
round_7 = all_trimmed[all_trimmed['Name']==player_7]

player_8 = st.selectbox('Select a player to draft in Round 8:', all.Name)
round_8 = all_trimmed[all_trimmed['Name']==player_8]

player_9 = st.selectbox('Select a player to draft in Round 9:', all.Name)
round_9 = all_trimmed[all_trimmed['Name']==player_9]

player_10 = st.selectbox('Select a player to draft in Round 10:', all.Name)
round_10 = all_trimmed[all_trimmed['Name']==player_10]

player_11 = st.selectbox('Select a player to draft in Round 11:', all.Name)
round_11 = all_trimmed[all_trimmed['Name']==player_11]

player_12 = st.selectbox('Select a player to draft in Round 12:', all.Name)
round_12 = all_trimmed[all_trimmed['Name']==player_12]

player_13 = st.selectbox('Select a player to draft in Round 13:', all.Name)
round_13 = all_trimmed[all_trimmed['Name']==player_13]

player_14 = st.selectbox('Select a player to draft in Round 14:', all.Name)
round_14 = all_trimmed[all_trimmed['Name']==player_14]

player_15 = st.selectbox('Select a player to draft in Round 15:', all.Name)
round_15 = all_trimmed[all_trimmed['Name']==player_15]

player_16 = st.selectbox('Select a player to draft in Round 16:', all.Name)
round_16 = all_trimmed[all_trimmed['Name']==player_16]

player_17 = st.selectbox('Select a player to draft in Round 17:', all.Name)
round_17 = all_trimmed[all_trimmed['Name']==player_17]

player_18 = st.selectbox('Select a player to draft in Round 18:', all.Name)
round_18 = all_trimmed[all_trimmed['Name']==player_18]

player_19 = st.selectbox('Select a player to draft in Round 19:', all.Name)
round_19 = all_trimmed[all_trimmed['Name']==player_19]

player_20 = st.selectbox('Select a player to draft in Round 20:', all.Name)
round_20 = all_trimmed[all_trimmed['Name']==player_20]

player_21 = st.selectbox('Select a player to draft in Round 21:', all.Name)
round_21 = all_trimmed[all_trimmed['Name']==player_21]

player_22 = st.selectbox('Select a player to draft in Round 22:', all.Name)
round_22 = all_trimmed[all_trimmed['Name']==player_22]

player_23 = st.selectbox('Select a player to draft in Round 23:', all.Name)
round_23 = all_trimmed[all_trimmed['Name']==player_23]

player_24 = st.selectbox('Select a player to draft in Round 24:', all.Name)
round_24 = all_trimmed[all_trimmed['Name']==player_24]

player_25 = st.selectbox('Select a player to draft in Round 25:', all.Name)
round_25 = all_trimmed[all_trimmed['Name']==player_25]

player_26 = st.selectbox('Select a player to draft in Round 26:', all.Name)
round_26 = all_trimmed[all_trimmed['Name']==player_26]

#compiled player stats from each round. all 
draft = pd.DataFrame(round_1,columns=round_1.columns)

draft = draft.append([round_2, round_3,round_4,round_5,round_6,round_7,round_8,round_9,round_10,round_11,round_12,round_13,
                     round_14,round_15,round_16,round_17,round_18,round_19,round_20,round_21,round_22,round_23,round_24,round_25,
                     round_26])


st.write('Draft Results',draft)

#All stats for selected players
team_1 = all[all['Name']==player_1]
team_2 = all[all['Name']==player_2]
team_3 = all[all['Name']==player_3]
team_4 = all[all['Name']==player_4]
team_5 = all[all['Name']==player_5]
team_6 = all[all['Name']==player_6]
team_7 = all[all['Name']==player_7]
team_8 = all[all['Name']==player_8]
team_9 = all[all['Name']==player_9]
team_10 = all[all['Name']==player_10]
team_11 = all[all['Name']==player_11]
team_12 = all[all['Name']==player_12]
team_13 = all[all['Name']==player_13]
team_14 = all[all['Name']==player_14]
team_15 = all[all['Name']==player_15]
team_16 = all[all['Name']==player_16]
team_17 = all[all['Name']==player_17]
team_18 = all[all['Name']==player_18]
team_19 = all[all['Name']==player_19]
team_20 = all[all['Name']==player_20]
team_21 = all[all['Name']==player_21]
team_22 = all[all['Name']==player_22]
team_23 = all[all['Name']==player_23]
team_24 = all[all['Name']==player_24]
team_25 = all[all['Name']==player_25]
team_26 = all[all['Name']==player_26]

team_draft = pd.DataFrame(team_1,columns=team_1.columns)
team_draft = team_draft.append([team_2,team_3,team_4,team_5,team_6,team_7,team_8,team_9,team_10,team_11,team_12,team_13,
                                team_14,team_15,team_16,team_17,team_18,team_19,team_20,team_21,team_22,team_23,team_24,
                                team_25,team_26])


draft_totals = team_draft.drop(['Name','AVG','ERA','WHIP','IP','ER','H','BB','HR_all','HR_perc','BB_perc','K_perc','AB','OBP','SLG','OPS','K_%','B_%'],axis=1)
draft_totals = draft_totals.sum(axis=0)

team_draft['pitch_weight']= team_draft['IP'] / team_draft['IP'].sum()
team_draft['Team_ERA'] = team_draft['pitch_weight']*team_draft['ERA']
team_draft['Team_WHIP'] = team_draft['pitch_weight']*team_draft['WHIP']

team_draft['hit_weight']= team_draft['AB'] / team_draft['AB'].sum()
team_draft['Team_AVG'] = team_draft['hit_weight']*team_draft['AVG']

results = team_draft.drop(['Name','IP','ER','H','BB','HR_all','HR_perc','K_perc','BB_perc','AB','ERA','WHIP','AVG','OBP','SLG','OPS','K_%','B_%','pitch_weight','hit_weight'],axis=1)
results = results[['R', 'HR', 'RBI', 'SB', 'Team_AVG','K','W','SV','Team_ERA','Team_WHIP']]

results = results.sum(axis=0)
#results = results*.7

ten_teams = [['R',1184],['HR',356],['RBI',1134],['SB',128],['Team_AVG',.270],['K',1449],['W',92],['SV',80],['Team_ERA',3.42],['Team_WHIP',1.12]]
targets = pd.DataFrame(ten_teams,columns=['Category','Target'])

col1, col2 = st.columns((1,1))
with col1:
    st.write(""" # 2022 Team Projections""",results)
with col2:
    st.write(""" # 2021 80th Percentile""",targets)
