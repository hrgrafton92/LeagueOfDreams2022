import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import altair as alt


recap = pd.read_csv("recap.csv")
weekly_record = pd.read_csv("C:/Users/hrgra/OneDrive/Documents/LeagueOfDreams/weekly_record.csv")
clint2 = pd.read_csv("C:/Users/hrgra/OneDrive/Documents/LeagueOfDreams/clint2.csv")
spencer = pd.read_csv("C:/Users/hrgra/OneDrive/Documents/LeagueOfDreams/spencer.csv")
jeff = pd.read_csv("C:/Users/hrgra/OneDrive/Documents/LeagueOfDreams/jeff.csv")
collin3 = pd.read_csv("C:/Users/hrgra/OneDrive/Documents/LeagueOfDreams/collin3.csv")
harley = pd.read_csv("C:/Users/hrgra/OneDrive/Documents/LeagueOfDreams/harley.csv")
bob4 = pd.read_csv("C:/Users/hrgra/OneDrive/Documents/LeagueOfDreams/bob4.csv")
caleb = pd.read_csv("C:/Users/hrgra/OneDrive/Documents/LeagueOfDreams/caleb.csv")
kyle = pd.read_csv("C:/Users/hrgra/OneDrive/Documents/LeagueOfDreams/kyle.csv")
tripp = pd.read_csv("C:/Users/hrgra/OneDrive/Documents/LeagueOfDreams/tripp.csv")
batter = pd.read_csv("C:/Users/hrgra/OneDrive/Documents/LeagueOfDreams/batter2.csv")
pitcher = pd.read_csv("C:/Users/hrgra/OneDrive/Documents/LeagueOfDreams/pitcher2.csv")

# Intro text

"""
# Winter Meeting is Upon Us!

I'm sure we all 100%, definitely have not forgotten, have our calendars marked for the inaugural League of Dreams Winter Meeting. The meeting is taking place soon on Sunday, February 6th at 2pm. Time to #GetOutTheVote and make your preferences known as we determine whether or not to make any adjustments to the league settings going forward. You can check out the planned itinerary **[here.](https://docs.google.com/spreadsheets/d/1dfJE2ra_Ho1KrxX4azlT-Glt7p7FzSbEDKArG3kZe1Y/edit#gid=1520421931)**

For the sake of time its important that you come into the meeting with at least some initial thoughts about each line item. We are hoping to take a quick vote on each subject, and then further discuss any items without a pro-change majority vote. Don't have to have firm stances in mind, that's what discussion is for after all, but knowing how you will vote will help us stay on schedule. There's a lot to cover.

To build some momentum and get us back in the GM mindset here is a brief rundown on each team, in reverse order of 2021 regular season standings, that serves to recap the 2021 season and look ahead to the 2022 season. Each team is accompanied by one visual with data taken from the league ESPN site that perhaps helps explain their 2021 outcome, or just point out something interesting and distinct about said team. Disclaimer: "value" is subjective. For the purposes of interpreting each chart here are a few tips:

1. "Value" refers to the ESPN Player Rater calculations. This number is inherently subjective (I personally believe it gives too much weight to Stolen Bases for example), but it serves as a consistent baseline for all players.
2. Don't get hung up on exact numbers, but look at comparisons across teams. Certain 2021 information was difficult to find as it had been replaced on ESPN by 2022 information. Everything is pretty accurate but there possibly are small discrepancies between certain variables and the truth. Impossible to say.
3. I stopped grabbing player rater values after the top 550. If a player was worse than that, they were assigned the 550th value for the sake of time.
4. Teams are referred to in the visuals by their abbreviation which are shown immediately below.

As a refresher, here were the regular season standings in 2021 (X. representing Win %):

"""

st.dataframe(recap)


"""

After finishing at the top of the standings in the regular season, plus a flurry of aggressive trades that triggered an arms race among the top contenders, Matt Heard also took home the championship. In his first (!!!) season as a GM Matt has raised the bar for what it takes to come out on top in this league. We will circle back around to Matt at the end, but first, a look at the other seasons that did not go nearly as well. 2021 Key Contributors will refer to Top 50 Player Rater rankings for the purposes of this article. Players acquired near the trade deadline are attributed to their prior owner. Players traded at a point earlier in the season will be attributed to the acquiring team.

# #10 Clint Sickert - Snow Hill Billies (SICK)

Superlative = The Optimist. "There's always next year."

2021 Key Contributors:
none

3 facts about the 2021 season: 

1) The Snow Hill Billies finished in 10th place 

2) Mike Trout took 117 total at-bats and appeared in only 36 games

3) Mike Trout was selected by the Snow Hill Billies in the 1st round. 

There is an easy to see cause and effect taking place between these three facts. Who among us would not also suffer a down season after losing our 1st round pick for the majority of the season? However, Clint faced an uphill battle this season even before Trout's injury by missing the draft. This absence resulted in being assigned his keepers in the first 3 rounds, significantly overpaying for Max Fried and Dansby Swanson (pre-draft rankings of 80 and 92, respectively.) Despite this, looking back at the end of the 2021 season reveals that the players on Clint's Opening Day roster would have tied for the 3rd highest Player Rater over the course of the full season.  However, a total of 12 free-agency acquisitions (3rd lowest overall, lowest among Eastern Time Zone based teams) may have sealed his fate by failing to find extra value on the waiver wire to keep pace with other more active managers and to make up for his draft being run on auto-draft. Clint was an active trade partner however, with more trades than anyone but Jeff (more on him later). While Clint's season as a whole left a lot to be desired, his (roughly) 1st and 2nd half performance splits showed he was still engaged and working to build towards next year. Look how far back he was at the end of the Week 9 matchup. From that point on he steadily makes up ground to end the year...well, not strong, but stronger. It would be easy to mentally clock out after a slow start and one thing I love about this league is that every team is committed. 

"""

#Clint first graph

clint_color = {Team:'red' if Team=='SICK' else 'grey' for Team in weekly_record.Team.unique()}
clint_graph1 = sns.lineplot(data=weekly_record,x="Week",y="Total_.",hue="Team", legend = False,palette=clint_color,linewidth=3)
clint_graph1.set_ylabel("Winning %")
clint_graph1.set_title("Cumulative Winning % in 2021")
clint_graph1.set_xticks(range(len(weekly_record["Week"].unique())))
plt.text(1.5,.15,"SICK",horizontalalignment="left",color="red")
plt.axvline(x=9,linestyle="--",color="grey")
plt.show()
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)


"""
This next graph shows the Keeper Value of each team *relative* to the round they were taken in. AKA: in theory it would be easier for a player drafted in Round 20 to outperform other players taken in his round as we should have low expectations for players in late rounds. Keepers in Round 1 have a higher bar to clear. It should not be surpsing that Clint significantly underperformed this season given a combination of bad luck (injury) and penalties (missing the draft) working against him in the first 3 rounds. The good news is that this is not a reflection of in-season GM skill and a fresh start this season brings new opportunities for Keeper selections. Besides, as will be shown (but not focused on) in later graphs, Clint did quite well from a managerial standpoint in some other metrics. At the very least, he is likely to have better injury luck in 2022.

"""

clint_graph2 = sns.barplot(data=clint2,x="VORP",y="Team",hue="Team",order=clint2.sort_values("VORP", ascending = False).Team,dodge = False)
clint_graph2.set_ylabel("Teams")
clint_graph2.set_xlabel("Player Rater Value Above Average")
clint_graph2.set_title("Keeper Value Relative to Draft Round")
clint_graph2.legend_.remove()
st.pyplot()

#spencer graph

"""
# #9 Spencer Hunt - Dollar Dog Night ($)

Superlative = Ferris Bueller. "Life moves pretty fast. If you don't stop and look around once in awhile, you could miss it."


2021 Key Contributors:
Fernando Tatis Jr., Ozzie Albies, Randy Arozarena

This was a tough year for Spencer. He went from 1 spot away from the top in 2020, to 1 spot away from the bottom in 2021. In fact, Tripp was only team to repeat his playoff appearance from 2020 showing the parity and competition this league is forming. But there is a broader context behind this drop-off that perhaps explains things more than simple league parity. Spencer was also deciding, and then acting on, moving from Thailand to the US. Life moves fast. You don't want to miss it by being occupied by the latest waiver-wire moves. I could be off-base and making some wrong assumptions, but its an explanation that I think makes a lot of sense. Spencer and Bob have always worked with a bit of a disadvantage through time-zones and (I presume) less day-to-day conversations with people around them about MLB. Add in a high level of life-change, and saying goodbyes, and I fantasy would take more of a backseat for me too. Whether this explanation has merit or not, the reality is that Spencer has fewer life transitions taking place this season and has a strong core he will bring back to contend for the title once again.

This chart shows the overall total value of each teams keeper's from last year. Spencer is the leader in this metric and its not particularly close. Using your keeper slots on Mookie Betts and Fernando Tatis Jr. will do that for you I suppose. Heading into next year Spencer still has the option to keep Tatis Jr. at a full round discount in the 2nd, and after drafting uber-propsect Wander Franco in the 15th round last year will likely be retaining his services giving Spencer a good shot to once again get more out of his Keepers than anyone else.
"""

spencer_graph = sns.barplot(data=spencer,x="Player_Rater",y="Team",hue="Team",order=spencer.sort_values("Player_Rater",ascending=False).Team,dodge=False)
spencer_graph.set_xlabel("Total Player Rater Value")
spencer_graph.set_ylabel("Team")
spencer_graph.set_title("Combined 2021 Player Rater For Keepers")
spencer_graph.legend_.remove()
st.pyplot()

#jeff graph

"""
# #8 Jeff Harley - Sox it to Ya! (JEFF)

Superlative = Howie Mendel. "Let's Make a Deal."

2021 Key Contributors:
Liam Hendricks, Rafael Devers, Tim Anderson, Tyler O'Neill, Kenley Jansen

What a reversal for Jeff in 2021. Our (former) reigning champ surprisingly finished in 8th place. Shame, shame. But anyone paying attention knows that looking at his win/loss columns alone will be misleading. Jeff single-handedly re-wrote the rulebook on how to assess the trade market and how to value draft picks. He may have taken a step backward in 2021 but my goodness is the guy being to living the high life on draft day in 2022. He has a staggering 16 picks in his war chest that take place within the first 10 rounds. Eight picks by Round 5, another 8 by Round 10. Jeff is easily my betting favorite to win the championship heading into 2023. Baseball has a long season, and there are surprises every year, but he has given himself the best chance possible to repeat as champion only 3 seasons into the league's existence. 

To get a sense of the value of these first 16 picks, below is the average Player Rater Value per round, excluding Keepers. Essentially after Round 10 you need to be outperforming the field to have a chance of reaching Top 150 value (roughly regarded as the cutoff of players you will keep all year vs streaming), as the typical draft selection beyond this point will fall short of this cutoff. 

Honorable Mention to our collective selections in Round 16: hello Austin Riley, Sandy Alcantara, and Kenley Jansen. 

"""
jeff_graph = sns.lineplot(data=jeff,x="ROUND",y="adp_player_rater",marker="o",color="black")
plt.axhline(y=6.53,linestyle="--",color="red",linewidth=1)
plt.axhline(y=5.29,linestyle="--",color="blue",linewidth=1)
jeff_graph.set_xlabel("Round")
jeff_graph.set_ylabel("Player Rater")
jeff_graph.set_title("Player Rater Average Per 2021 Draft Round (Not Including Keepers)")
plt.text(.5,6,"Top 100",horizontalalignment="left",color="red")
plt.text(.5,4.7,"Top 150",horizontalalignment="left",color="blue")
st.pyplot()

"""
Another way to look at this line is shown below:

- the green is where Jeff has extra picks in the first 5 Rounds. 3 extra picks in addition to his own five.

- the yellow is where Jeff has extra picks in the 6th-10th Rounds. 3 extra picks in addition to his own five.

- the red is where a standard team would be making these other 6 picks. In the 11th-16th Round range. 

"""


jeff_graph = sns.lineplot(data=jeff,x="ROUND",y="adp_player_rater",marker="o",color="black")
plt.axhline(y=6.53,linestyle="--",color="red",linewidth=1)
plt.axhline(y=5.29,linestyle="--",color="blue",linewidth=1)
jeff_graph.set_xlabel("Round")
jeff_graph.set_ylabel("Player Rater")
jeff_graph.set_title("Player Rater Average Per 2021 Draft Round (Not Including Keepers)")
plt.text(.5,6,"Top 100",horizontalalignment="left",color="red")
plt.text(.5,4.7,"Top 150",horizontalalignment="left",color="blue")
rect1=mpatches.Rectangle((1,0),5.5,10,color="palegreen",linewidth=2)
plt.gca().add_patch(rect1)
rect2=mpatches.Rectangle((5.5,0),5,10,color="lightyellow",linewidth=2)
plt.gca().add_patch(rect2)
rect3=mpatches.Rectangle((10.5,0),6,10,color="lightcoral",linewidth=2)
plt.gca().add_patch(rect3)
st.pyplot()

"""

Probability of success is in Jeff's favor. But as we saw with Mike Trout's injury, or breakouts coming from Austin Riley, baseball is never that easily predictable and other teams will surely emerge as challengers.

"""

#collin graph

"""

# #7 Collin Loy - Freddie's Revenge (LOY)

Superlative = Merida from Brave. "If you had the chance to change your fate, would you?"

2021 Key Contributors:
Vladimir Guerrero Jr., Freddie Freeman, Zack Wheeler, Brandon Woodruff, Bryan Reynolds

Collin was in the mix for a potential playoff spot most of the season until the trade deadline approached when he decided to be a Seller, sealing his fate as bottom-5 team for 2021. In full length matchups after the trade deadline he went 13-25-2 to close out the season, dropping 12 games in the standings. A look back at end of season records tells us that Collin missed the playoffs by 11.5 games. A fantastic what-if scenario emerged if Collin had not sold off his team for future draft picks. He was headlined by the breakout season of Vladimir Guerrero Jr. in addition to a top-tier pitching staff. There was a time when Collin rostered Zack Wheeler, Brandon Woodruff, Lance Lynn, Trevor Rogers, Jose Berrios, and Alek Manoah. All top-35 finishes among SP. Ultimately this was still not enough to secure a playoff spot in a competitive league and, facing an uphill climb in the rankings, Collin took the long-view approach to team building. Did he make the right choice? Could he have changed his fate?

This chart shows Collin was one of the more "unlucky" teams this season in the win/loss category. Here we are looking at the difference between expected wins and actual wins during the regular season. Expected wins were calculated by taking the median value of every category, for every week. The top 5 teams in each category, each week, were awarded one expected win. The bottom 5 teams assigned one expected loss, with any team being assigned an expected tie if it matched the median. These 3 categories, expected win/loss/tie, were each summed for each team. Since there were significantly more expected ties than actual ties, I normalized each teams record to a 210 game regular season basis based on Teams win % ignoring ties. For example: win 80 games, lose 100 games, tie 30 games. Calculation = (80 / (80+100))  *  210. Not a perfect metric but I think the observation is clear. Collin had poor luck in his matchups. We know that Caleb held strong with his team (with the one exception of his Gerrit Cole trade with Bob), but Collin transformed into a Seller and missed the playoffs by almost exactly the amount of games he dropped post-trade deadline. Had Collin received some better luck, recorded a few more wins, perhaps have been more confident in his team and not sold at the deadline, how much would the post-season have looked different? Collin helped significantly boost the rosters of Matt and Tripp (our top 2 seeds) in the home stretch after all. Could his trade with Matt have decided our fates last year?

"""
highlight = ["salmon" if x == "LOY" else "grey" for x in collin3["Team"]]
collin_graph = sns.barplot(data=collin3,x="games_dif",y="Team",hue="Team",palette=highlight,order=collin3.sort_values("games_dif",ascending=False).Team,dodge=False)
collin_graph.set_ylabel("Team")
collin_graph.set_xlabel("Difference")
collin_graph.set_title("# of Expected Wins Above / Below Actual Wins")
collin_graph.legend_.remove()
st.pyplot()
#harley graph

"""
# #6 Harley Grafton - Burlington Sock-Puppets (GRAF)

Superlative = The Imagination Box. "Squidward we don't need a television as long as we have our...imagination"

2021 Key Contributors:
Corbin Burnes, Kyle Tucker, Freddy Peralta

With what I assume is the lowest knowledge level of baseball history among our league, it makes sense to look to the future, and imagine what it could hold. (If you don't believe me there was a point last week during our HOF vote text thread that I almost asked about the 3,000 hit guy who was banned...I couldn't remember who Pete Rose was. I just waited for someone else to bring him up and use his name.) 

The main storyline of my season was prospects. Two roster spots were devoted to prospects who never received a call-up to the MLB. The imaginiation of what their careers could become is still just that, an imagination. However, they are currently bother ranked in the top 3 of all prospects. I'll just have to keep waiting and imagining. My season was spent being generally in the playoff hunt, but always on the outside looking in. A glass half-full approach would say that having limited roster flexibility by stashing multiple prospects hampered me, and that be removing that limitation next year it may be enough to break into the playoffs next year. A glass half-empty approach says I had roughly the same finish in 2020 without stashing prospects, so what difference will that make. To be honest I'm not sure.

Below is a visual regarding Keeper value similar to that shown for Clint, but broken out across individual players. There are two variables, color and size. Color is representative of Player Rater Value *above* the average Player Rater Value of their draft round (brighter = higher positive value, darker = lower, possibly even negative value. Size is representative of the discount on draft day the keeper had. This is measured by comparing their draft slot to their Average Draft Position (ADP) across all Yahoo Fantasy Baseball Leagues (ESPN info unavailable). I found it humorous how late my keepers were compared to everyone else. Keep chasing/imagining the ideal world of having the best player also in the lateest round. By the time I took 1 keeper half the league had already draft all 3 of theirs. But you can count on 2022 I'll keep chasing potential keepers at the end of the draft and keep an eye on the future, whether in the form of prospects or high-risk breakout candidates. Final observation, I'm a biased source but I think the overall performance, relative to draft cost, is hard to beat with Kyle Tucker among Keepers. However, it does appear that in general the Keepers taken earlier had better performances last year. This makes sense as players taken earlier are already more proven. Even if players taken late have incredibly high potential, they are not as likely to actually achieve that potential. 

"""
size = (harley["round_dif"]+10)**2
color= harley["value_dif"]
harley_graph = sns.scatterplot(data=harley,x="ROUND",y="Team.x",hue=color,palette=plt.get_cmap('RdYlGn'),s=size)
harley_graph.axvline(x=12,linestyle="--",color="r")
harley_graph.set_xlabel("Draft Round")
harley_graph.set_ylabel("Team")
harley_graph.set_title("Keeper Value by Performance Relative to Draft Price Discount")
plt.text(16,9,"Kyle Tucker",horizontalalignment="left",color="red")
plt.show()
st.pyplot()
#bob graph

"""
# #5 Bob McGregor - Chang Phuak Warriors (WAR)

Superlative = The Real Life Winner. "The Atlanta Braves are your World Series Champions."

2021 Key Contributors:
Walker Buehler, Julio Urias, Paul Goldschmidt, Robbie Ray, Aaron Judge, Charlie Morton, Austin Riley, Javier Baez

With respect to the other Braves fans in the league, Bob stood behind his fandom more than everyone else by drafting eight Braves players, roughly 31% of his entire roster. Don't get your hopes up this year about rostering too many of the defending champs as Bob is sure to have them circled on his draft board. Bob spent the bulk of the season in the 4-6 seed range but was not able to break through to the playoffs. He was involved at the trade deadline but did not go all-in, leaving himself some flexibility heading into this years draft. He will be missing his #2 pick, sent to Caleb in a trade for Gerrit Cole. Outside of that though Bob retains all of his own picks. Bob certainly wasn't the most active GM, with the fewest free agency acquisitions and the 2nd fewest trades made, but he was deliberate in the moves he did make. An early season trade for Paul Goldschmidt brought in a season-long fixture at the position. Free agency acquisition Robbie Ray won the Cy Young. Real life awards are a positive for your fantasy team too. The broader theme here is if something isn't broken, don't try to fix it. 

You might be thinking that a 5th place outside the playoffs isn't exactly broken, but certainly shows a need for some fine-tuning. But this chart shows us that Bob was a powerhouse in the regular season. I'm genuinely surprised he didn't have a better record to show for it. He led the league outright in 4 out of 10 categories during the regular season. Only three other teams can lay claim to the top spot in any category at all last year. I think with the opportunity to compete in the post-season Bob would have been a difficult out, maybe even putting together a run alongside his fellow Braves to win the championship.

The x-axes aren't the same for each graph. Don't know why but keep a sharp eye when comparing graphs.
"""

bob_graph = sns.FacetGrid(bob4, col="categories", hue="highlight",col_wrap=2,sharey=False,sharex=False)
bob_graph.map_dataframe(sns.scatterplot, x="Team", y="totals.x")
for axes in bob_graph.axes.flat:
    _ = axes.set_xticklabels(axes.get_xticklabels(), rotation=90)
plt.tight_layout()
st.pyplot()
#caleb graph

"""
# #4 Caleb Mason - Ryu's Ruff Riders (MASO)

Superlative = Billy Beane. "When your enemy's making mistakes don't interrupt them."

2021 Key Contributors:
Starling Marte, Max Scherzer, Teoscar Hernandez, Bryce Harper, Nick Castellanos, Marcus Semien, Gerrit Cole

Looking back on the 2021 draft Caleb crushed his selections. Round after round he let us keep making mistakes and letting players stick around until Caleb's next pick. Look at the run of selections in his first ten rounds. Gerrit Cole, Bryce Harper, Max Scherzer, Starling Marte, Tim Anderson, Nick Castellanos, Teoscar Hernandez, Trevor Bauer, Edwin Diaz, Marcus Semien. Thats 10/10. Thats a wildly strong core of players to build around. Caleb floated around the 3rd through 6th seed basically all season before locking up the 4th playoff spot. He achieved this despite dealing away his 1st Round pick Gerrit Cole at the trade deadline. The best skill you can have in fantasy is being a talent evaluator. Sure it helps to consume content and coverage or to be a smooth talker in trade negotiations, but nothing is more beneficial to being accurate when determining "will this player have a good season?" Caleb set himself up for success on day 1 by correctly answering that question over and over again, while staying silent and letting us keep making the mistakes of not drafting those aforementioned players. He made good on that potential by making his first playoff appearance. 

Look below at the cumulative Player Rater value from our draft day rosters. Caleb leads the league by a healthy margin. When this is your baseline you are only one or two good free agent pickups or trades away from being a true powerhouse. Now coming into 2022 with 3 top-20 picks you can expect Caleb to reliably identify the best talent available.

"""
fig_dims = (6, 4)
fig, ax = plt.subplots(figsize=fig_dims)
caleb_graph = sns.barplot(data=caleb,x="Player_Rater",y="Team",hue="Team",ax=ax,order=caleb.sort_values("Player_Rater", ascending = False).Team,dodge = False)
caleb_graph.set_ylabel("Teams")
caleb_graph.set_xlabel("Player Rater Value")
caleb_graph.set_title("Draft Selections Player Rater")
caleb_graph.legend_.remove()

st.pyplot()
#kyle graph

"""
# #3 Kyle Klinedinst - Iron Man 8 (O's) 

Superlative = The Rounder. "Guys around here will tell you, you play for a living, it’s like any other job. You don’t gamble, you grind it out...But finally I’ve learned this: if you’re too careful your whole life can become a f*****’ grind."

2021 Key Contributers:
Cedric Mullins, Juan Soto, Adam Wainwright, Manny Machado, Brandon Crawford, Raisel Iglesias

Kyle had a disappointing 2020 with his sights set on a full rebuild. A few weeks into the season he appeared to have failed. As seen below, he generated the least value through the draft of any team and quickly dropped below .500 in the early weeks, bottoming out in Week 3 where he sat in 9th place. But Kyle grinded his way up the rankings, slowly and surely. He crossed the .500 record threshold in Week 10 and never looked back. When a playoff berth started to become a real possibility, Kyle went for it. He didn't want to grind on free agency anymore. Some blockbuster trades nearly paid off as he reached the championship round. Kyle's savviness as a GM must drastically be re-evaluated by the other league managers as we have another force to be reckoned with. If you remember the graph shown for Collin, you may have noticed one team over-performing by much more than anyone else. That team would be Kyle. However, I don't think his season was solely the result of good luck. As seen below Kyle had the lowest "breakout" performances among his draft selections meaning he had to acquire a lot of talent through free agency and trades, both requiring active management. In addition, his constant improvement over 5+ months is too long of a time span and too consistent to be purely luck. Regardless of how you reconcile these different metrics, the pressure is on for 2022 to show whether the 2020 or 2021 season was the more accurate reflection of his skill.

"""

kyle_graph = sns.barplot(data=kyle,x="movement",y="Team",hue="Team",order=kyle.sort_values("movement", ascending = False).Team,dodge = False)
kyle_graph.set_ylabel("Teams")
kyle_graph.set_xlabel("Player Rankings Improvement")
kyle_graph.set_title("Player Rankings Improvement From Draft Spot (Positive movement only)")
kyle_graph.legend_.remove()
st.pyplot()



kyle_color = {Team:'orange' if Team=="O'S" else 'grey' for Team in weekly_record.Team.unique()}
kyle_graph2 = sns.lineplot(data=weekly_record,x="Week",y="Total_.",hue="Team", legend = False,palette=kyle_color,linewidth=3)
kyle_graph2.set_ylabel("Winning %")
kyle_graph2.set_title("Cumulative Winning % in 2021")
kyle_graph2.set_xticks(range(len(weekly_record["Week"].unique())))
plt.axvline(x=10,linestyle="--",color="black")
plt.axhline(y=.5,linestyle="--",color="black")
plt.show()
st.pyplot()
#tripp graph

"""
# #2 Tripp Gordon - Commissioner Gordon (COGO)

Superlative = The Heart Surgeon. "In Japan. Heart Surgeon. Number 1. Steady Hand."

2021 Key Contributors:
Trea Turner, Josh Hader, Jorge Polanco, Jose Altuve

With Commissioner Gordon as your GM, you can rest easy as a fan. He has a steady hand. He is as reliable as they come both as a team GM and league commissioner. Founder of the league. Quick to process trades. Weekly lineup reminders. Playoff team in both years. Watches the most baseball of any GM (unofficial statistic.) Tripp was a top team all season long. In fact, he was the only team besides Matt to be the #1 seed at any point. Tripp crushed the 1st round of the draft by acquiring Trea Turner, the top overall player in fantasy for 2021. Free agency additions of Jorge Polanco and Jake Cronenworth spurred his team on without requiring any draft capital. Some savvy moves at the trade deadline showed a willingness to go for it when there was an opportunity to win the championship but ultimately he came up short. The rest of the league is strategizing for 2022 but its a safe bet that only 3 playoff spots will be up for grabs when Tripp claims one for himself again. (Unless...playoff format change? Idk, come to the Winter Meeting to find out.)

"""
tripp_graph = sns.barplot(data=tripp,x="X.",y="Team",hue="Team",order=tripp.sort_values("X.", ascending = False).Team,dodge = False)
tripp_graph.set_ylabel("Teams")
tripp_graph.set_xlabel("Win %")
tripp_graph.set_title("Highest Regular Season Win % Over Two Seasons")
tripp_graph.legend_.remove()
st.pyplot()

#matt graph

"""
# #1 Matt Heard - Meet Em Greet Em (LGM)

Superlative = The Wunderkind. "People keep calling me a Wunderkind... I don't even know what that means. I mean, I know what it means, it means very successful for your age, so I guess it makes sense, but... it's a weird word."

2021 Key Contributors:
BO Bichette, Jose Ramirez, Shohei Ohtani, Whit Merrifield, Kevin Gausman, Salvador Perez, Carlos Rodon, Matt Olson, Jacob DeGrom

Matt is metaphorically young in League of Dreams GM experience but he has already the highest possible success. At times, in the moment, it felt like Tripp and Kyle's strong roster construction, and their upgrades at the trade deadline, were enough to go toe-to-toe with Meet Em Greet Em. In hindsight this season belonged to Matt from the season opener and his standing as the top team was never in doubt. The man did not suffer a matchup loss until July! Best regular season record, championship. Both Elite and well-rounded in all categories. Not content with his strong start to  the season, Matt showed an aggression to protect his standing through a  series of win-now trades to hold off Tripp and Kyle's own trade upgrades (Caleb is not forgotten in the playoff race, but did not push all his chips to the middle of the table like the other three teams.) They paid off. This may cost him in the 2022 price but hey, you play to win the game. Other teams made similar end-of-season pushes but will enter the draft without the consolation of a championship. I never watched The Wire but the iconic line "You come at the King you best not miss" feels like it applies here. Matt has taken the league by storm in his first year as a GM, however he will have his work cut off for him this year as he will enter the 2022 draft missing four picks from the first ten rounds.  Despite this, he has earned the benefit of the doubt that he will still be competitive as a big reason for his success in his first year was identifying great talent in later rounds of the 2021 draft.

This won't surprise anyone but it should still shock you. Look at how long Matt spends as the #1 seed during the season. Only for the briefest of moments does he ever drop to the #2 spot, then he's right back on the throne. 

"""

matt_color = {Team:'blue' if Team=="LGM" else 'grey' for Team in weekly_record.Team.unique()}
matt_graph = sns.lineplot(data=weekly_record,x="Week",y="Total_.",hue="Team", legend = False,palette=matt_color,linewidth=3)
matt_graph.set_ylabel("Winning %")
matt_graph.set_title("Cumulative Winning % in 2021")
matt_graph.set_xticks(range(len(weekly_record["Week"].unique())))
plt.show()
st.pyplot()

"""
# That's all for the 2021 season recap. It's 2022 now and everyone is technically tied for first. See you all at the Winter Meeting!

If you made it this far reward yourself and play around with some 2021 season stats. Find some interesting player outliers to circle on your draft board who may be in for a big 2022 season.
"""
"""
# Filter 2021 Team Stats - Hitting
"""

selected_x_var = st.selectbox('What category you want the x variable to be? (Cannot be Player)', batter.columns)
selected_y_var = st.selectbox('What about the y? (Cannot be Player)', batter.columns)

batter_final = pd.DataFrame()
batter_final = batter[[selected_x_var,selected_y_var,"Player"]]


x_name = selected_x_var
y_name = selected_y_var
tooltip_name = 'Player'
xx = batter_final[[x_name]]
yy = batter_final[[y_name]]


fun = alt.Chart(batter_final, title = x_name+" vs "+y_name).mark_circle().encode(
    x = x_name,
    y = y_name,
    tooltip = "Player")

st.altair_chart(fun,use_container_width=True)
"""
# Filter 2021 Team Stats - Pitching
"""

selected_x_var_P = st.selectbox('What category you want the x variable to be? (Cannot be Player)', pitcher.columns,key=2)
selected_y_var_P = st.selectbox('What about the y? (Cannot be Player)', pitcher.columns,key=2)

pitcher_final = pd.DataFrame()
pitcher_final = pitcher[[selected_x_var_P,selected_y_var_P,"Player"]]


x_name_P = selected_x_var_P
y_name_P = selected_y_var_P
tooltip_name_P = 'Player'
xx_P = pitcher_final[[x_name_P]]
yy_P = pitcher_final[[y_name_P]]


fun_P = alt.Chart(pitcher_final, title = x_name_P+" vs "+y_name_P).mark_circle().encode(
    x = x_name_P,
    y = y_name_P,
    tooltip = "Player")

st.altair_chart(fun_P,use_container_width=True)
