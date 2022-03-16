#LOADING DATASETS
player_rater <- read.csv("2021_Player_Rater.csv")
#top 550 players in 2021 only

draft <- read.csv("2021_draft.csv")

total_record <- read.csv("Total_Record.csv")

weekly_record <- read.csv("Weekly_Records.csv")

categories <- read.csv("Categories.csv")

adp <- read.csv("adp.csv")

library(dplyr)
library(gghighlight)
library(RColorBrewer)
library(ggthemes)
library(ggplot2)
library(tidyr)
library(hrbrthemes)
library(ggsci)
library(reshape2)

#MANUALLY FILLING IN MISSING DATA
draft <- draft %>% rename("Player" = "PLAYER")
draft_player_rater <- left_join(draft,player_rater,by="Player")
draft_player_rater <- draft_player_rater %>% rename("Team" = "Team.x")
draft_player_rater <- draft_player_rater %>% rename("year_end_team" = "Team.y")
draft_player_rater$type_count1 <- ifelse(draft_player_rater$Type=="H",1,0)
draft_player_rater$type_count2 <- ifelse(draft_player_rater$Type=="P",1,0)

#Following players finished the 2021 season ranked lower than 550 by Player Rater. Looked up individual score and assigned
draft_player_rater[draft_player_rater$Player=="Cody Bellinger","Player_Rater"] <- -2.33
draft_player_rater[draft_player_rater$Player=="Cody Bellinger","year_end_team"] <- "MASO"
draft_player_rater[draft_player_rater$Player=="Anthony Rendon","Player_Rater"] <- -1.29
draft_player_rater[draft_player_rater$Player=="Anthony Rendon","year_end_team"] <- "FA"
draft_player_rater[draft_player_rater$Player=="Marcell Ozuna","Player_Rater"] <- -2.11
draft_player_rater[draft_player_rater$Player=="Marcell Ozuna","year_end_team"] <- "JEFF"
draft_player_rater[draft_player_rater$Player=="Stephen Strasburg","Player_Rater"] <- -1.42
draft_player_rater[draft_player_rater$Player=="Stephen Strasburg","year_end_team"] <- "FA"
draft_player_rater[draft_player_rater$Player=="Keston Hiura","Player_Rater"] <- -3.11
draft_player_rater[draft_player_rater$Player=="Keston Hiura","year_end_team"] <- "FA"
draft_player_rater[draft_player_rater$Player=="Cavan Biggio","Player_Rater"] <- -1.24
draft_player_rater[draft_player_rater$Player=="Jesus Luzardo","Player_Rater"] <- -2.84
draft_player_rater[draft_player_rater$Player=="Victor Robles","Player_Rater"] <- -1.62
draft_player_rater[draft_player_rater$Player=="Mike Moustakas","Player_Rater"] <- -2.43
draft_player_rater[draft_player_rater$Player=="Dinelson Lamet","Player_Rater"] <- -1.01
draft_player_rater[draft_player_rater$Player=="Patrick Corbin","Player_Rater"] <- -1.22
draft_player_rater[draft_player_rater$Player=="Patrick Corbin","year_end_team"] <- "$"
draft_player_rater[draft_player_rater$Player=="Hyun Jin","Player_Rater"] <- 4.65
draft_player_rater[draft_player_rater$Player=="Hyun Jin","year_end_team"] <- "MASO"
draft_player_rater[draft_player_rater$Player=="Travis d'Arnaud","Player_Rater"] <- -1.98
draft_player_rater[draft_player_rater$Player=="Travis d'Arnaud","year_end_team"] <- "WAR"
draft_player_rater[draft_player_rater$Player=="Ramon Laureano","Player_Rater"] <- 2.59
draft_player_rater[draft_player_rater$Player=="Mike Soroka","Player_Rater"] <- 0
draft_player_rater[draft_player_rater$Player=="Didi Gregorius","Player_Rater"] <- -.27
draft_player_rater[draft_player_rater$Player=="Sixto Sanchez", "Player_Rater"] <- 0
draft_player_rater[draft_player_rater$Player=="Trevor Rosenthal","Player_Rater"] <- 0
draft_player_rater[draft_player_rater$Player=="Kyle Lewis","Player_Rater"] <- -1.95
draft_player_rater[draft_player_rater$Player=="Luke Voit","Player_Rater"] <- -.69
draft_player_rater[draft_player_rater$Player=="Jarred Kelenic","Player_Rater"] <- -.80
draft_player_rater[draft_player_rater$Player=="Jarred Kelenic","year_end_team"] <- "GRAF"
draft_player_rater[draft_player_rater$Player=="Dallas Keuchel","Player_Rater"] <- -1.62
draft_player_rater[draft_player_rater$Player=="Dallas Keuchel","year_end_team"] <- "$"
draft_player_rater[draft_player_rater$Player=="Jordan Hicks","Player_Rater"] <- -1.93
draft_player_rater[draft_player_rater$Player=="Clint Frazier","Player_Rater"] <- -2.9
draft_player_rater[draft_player_rater$Player=="Carlos Carrasco","Player_Rater"] <- -2.25
draft_player_rater[draft_player_rater$Player=="Carlos Carrasco","year_end_team"] <- "LOY"
draft_player_rater[draft_player_rater$Player=="James McCann","Player_Rater"] <- -.54
draft_player_rater[draft_player_rater$Player=="James Paxton","Player_Rater"] <- -1.77
draft_player_rater[draft_player_rater$Player=="Eloy Jimenez","Player_Rater"] <- -.6
draft_player_rater[draft_player_rater$Player=="Eloy Jimenez","year_end_team"] <- "LOY"
draft_player_rater[draft_player_rater$Player=="Nick Madrigal","Player_Rater"] <- -.28
draft_player_rater[draft_player_rater$Player=="Nick Madrigal","year_end_team"] <- "SICK"
draft_player_rater[draft_player_rater$Player=="Cristian Pache","Player_Rater"] <- -4.25
draft_player_rater[draft_player_rater$Player=="Elieser Hernandez","Player_Rater"] <- -.91
draft_player_rater[draft_player_rater$Player=="Rafael Montero","Player_Rater"] <- -.59
draft_player_rater[draft_player_rater$Player=="Brian Anderson","Player_Rater"] <- -.5
draft_player_rater[draft_player_rater$Player=="Nate Pearson","Player_Rater"] <- -1.67
draft_player_rater[draft_player_rater$Player=="Chris Martin","Player_Rater"] <- -.34
draft_player_rater[draft_player_rater$Player=="Chris Martin","year_end_team"] <- "WAR"
draft_player_rater[draft_player_rater$Player=="Rowdy Tellez","Player_Rater"] <- -.36
draft_player_rater[draft_player_rater$Player=="A.J. Puk","Player_Rater"] <- -2.31
draft_player_rater[draft_player_rater$Player=="Bobby Witt","Player_Rater"] <- 0
draft_player_rater[draft_player_rater$Player=="Bobby Witt","year_end_team"] <- "GRAF"
draft_player_rater[draft_player_rater$Player=="Dylan Bundy","Player_Rater"] <- -1.91
draft_player_rater[draft_player_rater$Player=="Drew Waters","Player_Rater"] <- 0
draft_player_rater[draft_player_rater$Player=="Noah Syndergaard","Player_Rater"] <- -1.93
draft_player_rater[draft_player_rater$Player=="Noah Syndergaard","year_end_team"] <- "LGM"
draft_player_rater[draft_player_rater$Player=="MacKenzie Gore","Player_Rater"] <- 0
draft_player_rater[draft_player_rater$Player=="Andres Gimenez","Player_Rater"] <- -.52
draft_player_rater[draft_player_rater$Player=="Julio Rodriguez","Player_Rater"] <- 0
draft_player_rater[draft_player_rater$Player=="Julio Rodriguez","year_end_team"] <- "GRAF"
draft_player_rater[draft_player_rater$Player=="Matt Harvey","Player_Rater"] <- -3.08

#Manually assigning Keeper status. This is technically unofficial, and recorded offline from ESPN.
draft_player_rater$keeper <- 0
draft_player_rater[1,"keeper"] <- 1
draft_player_rater[1,"keeper"] <- 1
draft_player_rater[3,"keeper"] <- 1
draft_player_rater[4,"keeper"] <- 1
draft_player_rater[6,"keeper"] <- 1
draft_player_rater[7,"keeper"] <- 1
draft_player_rater[10,"keeper"] <- 1
draft_player_rater[14,"keeper"] <- 1
draft_player_rater[20,"keeper"] <- 1
draft_player_rater[21,"keeper"] <- 1
draft_player_rater[24,"keeper"] <- 1
draft_player_rater[26,"keeper"] <- 1
draft_player_rater[30,"keeper"] <- 1
draft_player_rater[38,"keeper"] <- 1
draft_player_rater[50,"keeper"] <- 1
draft_player_rater[52,"keeper"] <- 1
draft_player_rater[53,"keeper"] <- 1
draft_player_rater[66,"keeper"] <- 1
draft_player_rater[69,"keeper"] <- 1
draft_player_rater[72,"keeper"] <- 1
draft_player_rater[79,"keeper"] <- 1
draft_player_rater[93,"keeper"] <- 1
draft_player_rater[97,"keeper"] <- 1
draft_player_rater[116,"keeper"] <- 1
draft_player_rater[118,"keeper"] <- 1
draft_player_rater[119,"keeper"] <- 1
draft_player_rater[159,"keeper"] <- 1
draft_player_rater[176,"keeper"] <- 1
draft_player_rater[225,"keeper"] <- 1
draft_player_rater[247,"keeper"] <- 1
draft_player_rater[248,"keeper"] <- 1

#For players ranked below 550 for Player Rater, assigning rank of 550 instead of searching for each rank.
draft_player_rater$movement <- draft_player_rater$NO- draft_player_rater$Ranking
draft_player_rater[draft_player_rater$Player=="Cody Bellinger","movement"] <- 9 - 550
draft_player_rater[draft_player_rater$Player=="Anthony Rendon","movement"] <- 29 - 550
draft_player_rater[draft_player_rater$Player=="Marcell Ozuna","movement"] <- 50 - 550
draft_player_rater[draft_player_rater$Player=="Stephen Strasburg","movement"] <- 64 - 550
draft_player_rater[draft_player_rater$Player=="Keston Hiura","movement"] <- 77 - 550
draft_player_rater[draft_player_rater$Player=="Cavan Biggio","movement"] <- 85 - 550
draft_player_rater[draft_player_rater$Player=="Jesus Luzardo","movement"] <- 88 - 550
draft_player_rater[draft_player_rater$Player=="Victor Robles","movement"] <- 94 - 550
draft_player_rater[draft_player_rater$Player=="Mike Moustakas","movement"] <- 102 - 550
draft_player_rater[draft_player_rater$Player=="Dinelson Lamet","movement"] <- 106 - 550
draft_player_rater[draft_player_rater$Player=="Patrick Corbin","movement"] <- 112 - 550
draft_player_rater[draft_player_rater$Player=="Hyun Jin","Ranking"] <- 173
draft_player_rater[draft_player_rater$Player=="Hyun Jin","movement"] <- 119 - 173
draft_player_rater[draft_player_rater$Player=="Travis d'Arnaud","movement"] <- 120 - 550
draft_player_rater[draft_player_rater$Player=="Ramon Laureano","movement"] <- 127 - 550
draft_player_rater[draft_player_rater$Player=="Didi Gregorius","movement"] <- 138 - 550
draft_player_rater[draft_player_rater$Player=="Trevor Rosenthal","movement"] <- 147 - 550
draft_player_rater[draft_player_rater$Player=="Kyle Lewis","movement"] <- 153 - 550
draft_player_rater[draft_player_rater$Player=="Luke Voit","movement"] <- 156 - 550
draft_player_rater[draft_player_rater$Player=="Jarred Kelenic","movement"] <- 165 - 550
draft_player_rater[draft_player_rater$Player=="Dallas Keuchel","movement"] <- 172 - 550
draft_player_rater[draft_player_rater$Player=="Jordan Hicks","movement"] <- 177 - 550
draft_player_rater[draft_player_rater$Player=="Clint Frazier","movement"] <- 180 - 550
draft_player_rater[draft_player_rater$Player=="Carlos Carrasco","movement"] <- 182 - 550
draft_player_rater[draft_player_rater$Player=="James McCann","movement"] <- 194 - 550
draft_player_rater[draft_player_rater$Player=="James Paxton","movement"] <- 195 - 550
draft_player_rater[draft_player_rater$Player=="Eloy Jimenez","movement"] <- 196 - 550
draft_player_rater[draft_player_rater$Player=="Nick Madrigal","movement"] <- 200 - 550
draft_player_rater[draft_player_rater$Player=="Cristian Pache","movement"] <- 211 - 550
draft_player_rater[draft_player_rater$Player=="Elieser Hernandez","movement"] <- 212 - 550
draft_player_rater[draft_player_rater$Player=="Rafael Montero","movement"] <- 215 - 550
draft_player_rater[draft_player_rater$Player=="Brian Anderson","movement"] <- 219 - 550
draft_player_rater[draft_player_rater$Player=="Nate Pearson","movement"] <- 223 - 550
draft_player_rater[draft_player_rater$Player=="Chris Martin","movement"] <- 231 - 550
draft_player_rater[draft_player_rater$Player=="Rowdy Tellez","movement"] <- 242 - 550
draft_player_rater[draft_player_rater$Player=="A.J. Puk","movement"] <- 243 - 550
draft_player_rater[draft_player_rater$Player=="Dylan Bundy","movement"] <- 247 - 550
draft_player_rater[draft_player_rater$Player=="Noah Syndergaard","movement"] <- 252 - 550
draft_player_rater[draft_player_rater$Player=="Andres Gimenez","movement"] <- 254 - 550
draft_player_rater[draft_player_rater$Player=="Matt Harvey","movement"] <- 257 - 550

total_record_2021 <- total_record %>% filter(Year==2021) 
total_record_2021$GM <- c("Tripp Gordon","Jeff Harter","Spencer Hunt","Bob McGregor","Caleb Mason","Matt Heard","Harley Grafton","Kyle Klinedinst","Clint Sickert","Collin Loy")
total_record_2021$Name <- c("Commissioner Gordon","Sox it to Ya!","Dollar Dog Night","Chang Phuak Warriors","Ryu's Ruff Riders","Meet Em Greet Em","Burlington Sock-Puppets","Iron Man 8","Snow Hill Billies","Freddie's Revenge")
recap <- total_record_2021 %>% select(GM,Name,Team,X.) %>% arrange(desc(X.))
recap




#_______________________________________________________

#SEASON RECAP

#10 Snow Hill Billies
clint <- draft_player_rater %>% filter(keeper==0)
clint
clint <-  aggregate(Player_Rater~ROUND,clint,mean)
clint
clint <- clint %>% rename("avg" = "Player_Rater")
clint2 <- draft_player_rater %>% filter(keeper==1)
clint2 <- left_join(clint2,clint,"ROUND")
clint2

clint2$VORP <- clint2$Player_Rater - clint2$avg
clint2 <-  aggregate(VORP~Team,clint2,sum)
clint2 %>% ggplot(aes(reorder(Team,VORP),VORP,fill=Team))+
  geom_bar(color="black",stat="identity")+
  xlab("Team")+
  ylab("Player-Rater Value Above Average")+
  ggtitle("Keeper Value Above the Average Value of Players Drafted in Same Round")+
  theme_tufte()+
  theme(legend.position = "none")+
  scale_fill_jco()+
  coord_flip()


#__________________________________________________
#9 Dollar Dog Night
spencer <- draft_player_rater %>% filter(keeper==1)
spencer <- aggregate(Player_Rater~Team,spencer,sum)

spencer %>% ggplot(aes(reorder(Team,Player_Rater),Player_Rater,fill=Team)) +
  geom_bar(color="black",stat="identity")+
  theme_tufte()+
  theme(legend.position="none")+
  xlab("Team")+
  ylab("Player Rater Value")+
  ggtitle("Combined 2021 Player Rater for Keepers")+
  theme_tufte()+
  theme(legend.position = "none")+
  scale_fill_jco()+
  coord_flip()


#______________________________________________
#8 Sox it to Ya!
jeff <- draft_player_rater %>% filter(keeper==0)
jeff <- aggregate(Player_Rater~ROUND,draft_player_rater,mean)
jeff <- jeff %>% rename("adp_player_rater" = "Player_Rater")

jeff%>% ggplot(aes(ROUND,adp_player_rater))+
  geom_line(color="black")+
  geom_point(color="black")+
  geom_hline(aes(yintercept=6.53),color="red",linetype="dashed")+
  annotate("text",1.8,6.3,label="Top 100",color="red")+
  geom_hline(aes(yintercept=5.29),color="blue",linetype="dashed")+
  annotate("text",1.8,5,label="Top 150",color="blue")+
  theme_minimal()+
  scale_x_continuous(breaks = seq(min(jeff$ROUND), max(jeff$ROUND), by = 1))+
  ylab("Player Rater")+
  ggtitle("Player Rater Average By 2021 Draft Round (Not Including Keepers)")

jeff %>% ggplot(aes(ROUND,adp_player_rater))+
  geom_line(color="black")+
  geom_point(color="black")+
  geom_hline(aes(yintercept=6.53),color="red",linetype="dashed")+
  annotate("text",1.8,6.3,label="Top 100",color="red")+
  geom_hline(aes(yintercept=5.29),color="blue",linetype="dashed")+
  annotate("text",1.8,5,label="Top 150",color="blue")+
  theme_minimal()+
  scale_x_continuous(breaks = seq(1, 26, by = 1))+
  ylab("Player Rater")+
  ggtitle("Player Rater Average By 2021 Draft Round (Not Including Keepers)")+
  annotate("rect", fill = "salmon", color="black",alpha = 0.3, 
           xmin = 10.5, xmax = 16.5,
           ymin = -Inf, ymax = Inf)+
  annotate("rect", fill = "light green", color="black",alpha = 0.3, 
           xmin = .5, xmax = 5.5,
           ymin = -Inf, ymax = Inf)+
  annotate("rect", fill = "yellow", color="black",alpha = 0.3, 
           xmin = 5.5, xmax = 10.5,
           ymin = -Inf, ymax = Inf)

#_________________________________________

#7 Freddies Revenge
collin <- categories %>% select(-c(Total_R,Total_HR,Total_RBI,Total_SB,AVG_AVG,Total_K,Total_W,Total_SV,AVG_ERA,AVG_WHIP))
collin <- collin %>% gather(stat,total_value,-c(Team,Week))
collin <- aggregate(total_value~stat+Week,collin,median)
collin
categories

collin2 <- categories %>% select(-c(Total_R,Total_HR,Total_RBI,Total_SB,AVG_AVG,Total_K,Total_W,Total_SV,AVG_ERA,AVG_WHIP))
collin2
collin2 <- collin2 %>% gather(stat,value,-c(Team,Week))
collin2 <- left_join(collin2,collin,by=c("Week","stat"))
collin2
collin2$exp_win <- ifelse(collin2$value > collin2$total_value,1,0)
collin2$exp_loss <- ifelse(collin2$value < collin2$total_value,1,0)
collin2$exp_tie <- ifelse(collin2$value == collin2$total_value,1,0)
collin2
#40,48,51,57,59,59,60,60,60,66
collin_win <- aggregate(exp_win~Team,collin2,sum)

collin_loss <- aggregate(exp_loss~Team,collin2,sum)
collin_tie <- aggregate(exp_tie~Team,collin2,sum)
collin3 <- left_join(collin_win,collin_loss,"Team")
collin3 <- left_join(collin3,collin_tie,"Team")
collin3$Year <- 2021
collin3 <- left_join(collin3,total_record,by=c("Team","Year"))
collin3$exp_perc <- ((2*collin3$exp_win)+collin3$exp_tie) / (2*(collin3$exp_win+collin3$exp_loss+collin3$exp_tie))
collin3
collin3$perc_dif <- collin3$X. - collin3$exp_perc
collin3$games_dif <- ((collin3$W/(collin3$W+collin3$L))*210) - ((collin3$exp_win/(collin3$exp_win+collin3$exp_loss))*210)

collin3 %>% ggplot(aes(reorder(Team,games_dif),games_dif))+
  geom_bar(color="black",stat="identity",fill="salmon")+
  xlab("Team")+
  ylab("Difference")+
  ggtitle("# of Wins Above / Below Expected # Of Wins")+
  theme_tufte()+
  theme(legend.position ="none")+
  gghighlight(Team=="LOY")+
  coord_flip()

#__________________________________________________

#6 Burlington Sock-Puppets
harley <- left_join(draft_player_rater,adp,"Player")
harley <- harley %>% select(NO,Player,ROUND,Team.x,ADP,keeper,Player_Rater)
harley[harley$Player=="Jose Abreu","ADP"] <- 37.4
harley$ADP <- ceiling(harley$ADP/10)
harley <- harley %>% filter(keeper==1)
harley$round_dif <- harley$ROUND - harley$ADP

harley <- left_join(harley,jeff,"ROUND")
harley$value_dif <- harley$Player_Rater - harley$adp_player_rater


harley %>% ggplot(aes(Team.x,ROUND,color=value_dif))+geom_point(aes(size=round_dif))+
  scale_color_continuous(low="black",high="green")+
  geom_hline(yintercept=12,color="red",linetype="dashed")+
  scale_size_continuous(range = c(min(harley$round_dif), max(harley$round_dif)))+
  xlab("Team")+
  ylab("Draft Round")+
  ggtitle("Keeper Value by Performance Relative to Draft Price Discount")+
  labs(color="Draft Round Value Difference",size="ADP Round Difference")+
  annotate("text",x=3,y=18,label="Kyle Tucker",color="black")+
  theme_hc()+
  theme(legend.position="none")+
  coord_flip()

#________________________________________

#5 Chang Phuak Warriors 
head(categories)
bob <- categories %>% filter(Week==21) %>% select(Team,Total_R,Total_HR,Total_RBI,Total_SB,AVG_AVG,Total_K,Total_W,Total_SV,AVG_ERA,AVG_WHIP)
bob(totals)
bob <- bob %>% rename("R" = "Total_R")
bob <- bob %>% rename("HR" = "Total_HR")
bob <- bob %>% rename("RBI" = "Total_RBI")
bob <- bob %>% rename("SB" = "Total_SB")
bob <- bob %>% rename("AVG" = "AVG_AVG")
bob <- bob%>% rename("K" = "Total_K")
bob <- bob %>% rename("W" = "Total_W")
bob <- bob %>% rename("SV" = "Total_SV")
bob <- bob %>% rename("ERA" = "AVG_ERA")
bob <- bob %>% rename("WHIP" = "AVG_WHIP")

bob2 <- bob %>% gather(categories,totals,-Team)
bob3 <- aggregate(totals~categories,bob2,max)
aggregate(totals~categories,bob2,min)
bob3[bob3$categories=="ERA","totals"] <- 3.1780
bob3[bob3$categories=="WHIP","totals"] <- 1.11
bob4 <- left_join(bob2,bob3,"categories")
bob4$highlight <- ifelse(bob4$totals.x == bob4$totals.y,1,0)

bob4 %>% ggplot(aes( x = Team,totals.x,fill=highlight)) + 
  geom_bar(color="black",stat = "identity" ) + 
  xlab("Team")+
  ylab("Season Totals")+
  theme(axis.text.x= element_text(angle=90),legend.position = "none")+
  facet_wrap(categories~.,5,2,scales="free_y")

#____________________________________________

#4 Ryu's Ruff Ryders
caleb <- draft_player_rater %>% select(NO,Player,ROUND,Team,Ranking,Player_Rater)
caleb <- aggregate(Player_Rater~Team,caleb,sum)
team_ord <- levels(with(caleb,reorder(Team,-Player_Rater)))
caleb %>% ggplot(aes(reorder(Team,Player_Rater),Player_Rater)) +
  geom_bar(aes(fill=Team),color="black",stat="identity") +
  ggtitle("Total 2021 Player Rater Values if Opening Day Rosters Never Changed")+
  xlab("Team")+
  theme_tufte()+
  theme(axis.text.x=element_text(angle=90),legend.position="none")+
  scale_fill_discrete(breaks=team_ord)+
  scale_fill_jco()+
  coord_flip()

#________________________________________________

#3 Iron Man 8
kyle <- draft_player_rater %>% filter(movement >0)
kyle <- aggregate(movement~Team,kyle,sum)
kyle %>% ggplot(aes(reorder(Team,-movement),movement,fill=Team,color="black"))+
  geom_bar(color="black",stat="identity")+
  xlab("Team")+
  ylab("Player Rankings Improvement")+
  ggtitle("Player Movement From Draft Spot to End-Of-Season-Ranking (Positives Only)")+
  theme_tufte()+
  theme(legend.position="none")+
  scale_fill_jco()+
  coord_flip()


weekly_record %>% ggplot(aes(Week,Total_.,color=Team))+
  geom_line(color="orange",size=2)+
  gghighlight(Team=="O'S", keep_scales=TRUE)+
  ylab("2021 Season Win %")+
  ggtitle("Cumulative Winning % For 2021")+
  theme_tufte()+
  geom_vline(xintercept=10,linetype="dashed")+
  geom_hline(yintercept=.5,linetype="dashed")


#_______________________________________________

#2 Commissioner Gordon
tripp <- aggregate(X.~Team,total_record,mean)

tripp %>% ggplot(aes(reorder(Team,X.),X.,fill=Team))+
  geom_bar(color="black",stat="identity")+
  ggtitle("Highest Regular Season Win % Over Two Seasons")+
  xlab("Team")+
  ylab("Win %")+
  theme_tufte()+
  theme(axis.text.x=element_text(angle=90),legend.position="none")+
  scale_fill_jco()+
  coord_flip()

#___________________________________________

#1 Meet Em Greet Em 
weekly_record %>% select(Team,Total_.,Week) %>% filter(Week==9)
weekly_record %>% ggplot(aes(Week,Total_.,color=Team))+
  geom_line(color="royal blue",size=2)+
  gghighlight(Team=="MASO")+
  ylab("2021 Season Win %")+
  ggtitle("Cumulative Winning % For 2021")+
  theme_tufte()+
  geom_vline(xintercept=10,linetype="dashed")+
  geom_hline(yintercept=.5,linetype="dashed")
