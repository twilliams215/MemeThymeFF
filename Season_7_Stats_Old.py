#
#Resources: https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html

import numpy as np
import matplotlib.pyplot as plt
import math
from prettytable import PrettyTable

#Initializing Player Order
Players = ['Trent', 'Tanner', 'Marco', 'Josh', 'Dylan', 'Jarod', 'Wyatt', 'Marcus', 'Jacob', 'Jagan']
Week = [1, 2, 3, 4, 5, 6]
CurrentPosition = []

LeaguePointsFor = []
LeaguePointsAgainst = []
LeaguePosition = []


WeeklyPoints = []
WeeklyAvgPointsFor = []
WeeklyAvgPointsAgainst = []

x = PrettyTable()

#TotalLeaguePointsAgainst = 0

def Trent():
    Position = [1, 8, 8, 9, 9, 10] #Holds Overall Weekly Position
    PersonalPoints = [120.46, 87.5, 81.54, 87.08, 104.82, 85.8] #Holds Weekly Points
    PointsAgainst = [112.08, 132.04, 111.02, 91.38, 119.46, 118.08] #Holds Points Against

    TotalPointsFor = sum(PersonalPoints) #Sum of Points For
    TotalPointsAgainst = sum(PointsAgainst) #Sum of Points Against

    LeaguePointsFor.append(TotalPointsFor) #Adding Total Points For to Array to Graph
    LeaguePointsAgainst.append(TotalPointsAgainst) #Adding Total Points Against to Array to Graph

    LeaguePosition.append(Position) #Adding Player's Position Array to League Position Array
    CurrentPosition.append(Position[len(Position)-1])

    WeeklyPoints.append(PersonalPoints) #Adding Player's Points Array to Weekly Array
    Difference = TotalPointsFor - TotalPointsAgainst #Difference between the two

    #TotalLeaguePointsAgainst += TotalPointsAgainst #Adding Total League


def Tanner():
    Position = [10, 7, 9, 3, 3, 6] #Holds Overall Weekly Position
    PersonalPoints = [60.12, 127.6, 98.04, 147.52, 119.46, 84.5] #Holds Weekly Points
    PointsAgainst = [100.7, 102.28, 98.9, 64.62, 104.82, 117.06] #Holds Points Against

    TotalPointsFor = sum(PersonalPoints)  # Sum of Points For
    TotalPointsAgainst = sum(PointsAgainst)  # Sum of Points Against

    LeaguePointsFor.append(TotalPointsFor)  # Adding Total Points For to Array to Graph
    LeaguePointsAgainst.append(TotalPointsAgainst)  # Adding Total Points Against to Array to Graph

    LeaguePosition.append(Position)  # Adding Player's Position Array to League Position Array
    CurrentPosition.append(Position[len(Position) - 1])

    WeeklyPoints.append(PersonalPoints)  # Adding Player's Points Array to Weekly Array
    Difference = TotalPointsFor - TotalPointsAgainst  # Difference between the two

    #TotalLeaguePointsAgainst += TotalPointsAgainst  # Adding Total League

def Marco():
    Position = [5, 3, 2, 2, 1, 4] #Holds Overall Weekly Position
    PersonalPoints = [94.68, 82.12, 109.04, 91.38, 129.12, 94.2] #Holds Weekly Points
    PointsAgainst = [92.56, 106.32, 104.88, 87.08, 76.5, 109.7] #Holds Points Against

    TotalPointsFor = sum(PersonalPoints)  # Sum of Points For
    TotalPointsAgainst = sum(PointsAgainst)  # Sum of Points Against

    LeaguePointsFor.append(TotalPointsFor)  # Adding Total Points For to Array to Graph
    LeaguePointsAgainst.append(TotalPointsAgainst)  # Adding Total Points Against to Array to Graph

    LeaguePosition.append(Position)  # Adding Player's Position Array to League Position Array
    CurrentPosition.append(Position[len(Position) - 1])

    WeeklyPoints.append(PersonalPoints)  # Adding Player's Points Array to Weekly Array
    Difference = TotalPointsFor - TotalPointsAgainst  # Difference between the two

    #TotalLeaguePointsAgainst += TotalPointsAgainst  # Adding Total League
    #print(len(PersonalPoints))
    #print(len(PointsAgainst))

def Josh():
    Position = [7, 9, 3, 7, 5, 2] #Holds Overall Weekly Position
    PersonalPoints = [95.7, 111.56, 111.02, 64.62, 136.9, 123.32] #Holds Weekly Points
    PointsAgainst = [120.26, 95.52, 81.54, 147.52, 79.16, 118.04]  #Holds Points Against

    TotalPointsFor = sum(PersonalPoints)  # Sum of Points For
    TotalPointsAgainst = sum(PointsAgainst)  # Sum of Points Against

    LeaguePointsFor.append(TotalPointsFor)  # Adding Total Points For to Array to Graph
    LeaguePointsAgainst.append(TotalPointsAgainst)  # Adding Total Points Against to Array to Graph

    LeaguePosition.append(Position)  # Adding Player's Position Array to League Position Array
    CurrentPosition.append(Position[len(Position) - 1])

    WeeklyPoints.append(PersonalPoints)  # Adding Player's Points Array to Weekly Array
    Difference = TotalPointsFor - TotalPointsAgainst  # Difference between the two

    #TotalLeaguePointsAgainst += TotalPointsAgainst  # Adding Total League

def Dylan():
    Position = [9, 6, 4, 5, 8, 5] #Holds Overall Weekly Position
    PersonalPoints = [92.56, 109.90,  86.44, 75.82, 79.16, 117.06] #Holds Weekly Points
    PointsAgainst = [94.68, 106.16, 93.84, 92.82, 136.9, 84.5] #Holds Points Against

    TotalPointsFor = sum(PersonalPoints)  # Sum of Points For
    TotalPointsAgainst = sum(PointsAgainst)  # Sum of Points Against

    LeaguePointsFor.append(TotalPointsFor)  # Adding Total Points For to Array to Graph
    LeaguePointsAgainst.append(TotalPointsAgainst)  # Adding Total Points Against to Array to Graph

    LeaguePosition.append(Position)  # Adding Player's Position Array to League Position Array
    CurrentPosition.append(Position[len(Position) - 1])

    WeeklyPoints.append(PersonalPoints)  # Adding Player's Points Array to Weekly Array
    Difference = TotalPointsFor - TotalPointsAgainst  # Difference between the two

    #TotalLeaguePointsAgainst += TotalPointsAgainst  # Adding Total League

def Jarod():
    Position = [8, 2, 5, 8, 7, 8] #Holds Overall Weekly Position
    PersonalPoints = [92.96, 132.04, 104.88, 117.76, 129.34, 95.58] #Holds Weekly Points
    PointsAgainst = [119.16, 87.50, 109.04, 76.3, 144.38, 134.18] #Holds Points Against

    TotalPointsFor = sum(PersonalPoints)  # Sum of Points For
    TotalPointsAgainst = sum(PointsAgainst)  # Sum of Points Against

    LeaguePointsFor.append(TotalPointsFor)  # Adding Total Points For to Array to Graph
    LeaguePointsAgainst.append(TotalPointsAgainst)  # Adding Total Points Against to Array to Graph

    LeaguePosition.append(Position)  # Adding Player's Position Array to League Position Array
    CurrentPosition.append(Position[len(Position) - 1])

    WeeklyPoints.append(PersonalPoints)  # Adding Player's Points Array to Weekly Array
    Difference = TotalPointsFor - TotalPointsAgainst  # Difference between the two

    #TotalLeaguePointsAgainst += TotalPointsAgainst  # Adding Total League

def Wyatt():
    Position = [6, 10, 7, 4, 4, 3] #Holds Overall Weekly Position
    PersonalPoints = [112.08, 95.52, 98.9, 92.82, 145.08, 134.18] #Holds Weekly Points
    PointsAgainst = [120.46, 111.56, 98.04, 75.82, 105.48, 95.58] #Holds Points Against

    TotalPointsFor = sum(PersonalPoints)  # Sum of Points For
    TotalPointsAgainst = sum(PointsAgainst)  # Sum of Points Against

    LeaguePointsFor.append(TotalPointsFor)  # Adding Total Points For to Array to Graph
    LeaguePointsAgainst.append(TotalPointsAgainst)  # Adding Total Points Against to Array to Graph

    LeaguePosition.append(Position)  # Adding Player's Position Array to League Position Array
    CurrentPosition.append(Position[len(Position) - 1])

    WeeklyPoints.append(PersonalPoints)  # Adding Player's Points Array to Weekly Array
    Difference = TotalPointsFor - TotalPointsAgainst  # Difference between the two

    #TotalLeaguePointsAgainst += TotalPointsAgainst  # Adding Total League

def Marcus():
    Position = [4, 5, 6, 10, 10, 9] #Holds Overall Weekly Position
    PersonalPoints = [100.7, 106.16, 75.78, 76.3, 76.7, 118.08] #Holds Weekly Points
    PointsAgainst = [60.12, 109.9, 76.52, 117.76, 129.12, 85.8] #Holds Points Against

    TotalPointsFor = sum(PersonalPoints)  # Sum of Points For
    TotalPointsAgainst = sum(PointsAgainst)  # Sum of Points Against

    LeaguePointsFor.append(TotalPointsFor)  # Adding Total Points For to Array to Graph
    LeaguePointsAgainst.append(TotalPointsAgainst)  # Adding Total Points Against to Array to Graph

    LeaguePosition.append(Position)  # Adding Player's Position Array to League Position Array
    CurrentPosition.append(Position[len(Position) - 1])

    WeeklyPoints.append(PersonalPoints)  # Adding Player's Points Array to Weekly Array
    Difference = TotalPointsFor - TotalPointsAgainst  # Difference between the two

    #TotalLeaguePointsAgainst += TotalPointsAgainst  # Adding Total League

def Jacob():
    Position = [2, 4, 10, 6, 2, 1] #Holds Overall Weekly Position
    PersonalPoints = [120.26, 102.28, 83.84, 106.64, 144.38, 109.70] #Holds Weekly Points
    PointsAgainst = [95.7, 127.6, 86.44, 106.56, 129.34, 94.20] #Holds Points Against

    TotalPointsFor = sum(PersonalPoints)  # Sum of Points For
    TotalPointsAgainst = sum(PointsAgainst)  # Sum of Points Against

    LeaguePointsFor.append(TotalPointsFor)  # Adding Total Points For to Array to Graph
    LeaguePointsAgainst.append(TotalPointsAgainst)  # Adding Total Points Against to Array to Graph

    LeaguePosition.append(Position)  # Adding Player's Position Array to League Position Array
    CurrentPosition.append(Position[len(Position) - 1])

    WeeklyPoints.append(PersonalPoints)  # Adding Player's Points Array to Weekly Array
    Difference = TotalPointsFor - TotalPointsAgainst  # Difference between the two

    #TotalLeaguePointsAgainst += TotalPointsAgainst  # Adding Total League

def Jagan():
    Position = [3, 1, 1, 1, 6, 7] #Holds Overall Weekly Position
    PersonalPoints = [119.16, 106.32, 76.52, 106.56, 105.48, 118.04] #Holds Weekly Points
    PointsAgainst = [92.96, 82.12, 75.78, 106.64, 145.08, 123.32] #Holds Points Against

    TotalPointsFor = sum(PersonalPoints)  # Sum of Points For
    TotalPointsAgainst = sum(PointsAgainst)  # Sum of Points Against

    LeaguePointsFor.append(TotalPointsFor)  # Adding Total Points For to Array to Graph
    LeaguePointsAgainst.append(TotalPointsAgainst)  # Adding Total Points Against to Array to Graph

    LeaguePosition.append(Position)  # Adding Player's Position Array to League Position Array
    CurrentPosition.append(Position[len(Position) - 1])

    WeeklyPoints.append(PersonalPoints)  # Adding Player's Points Array to Weekly Array
    Difference = TotalPointsFor - TotalPointsAgainst  # Difference between the two

    #TotalLeaguePointsAgainst += TotalPointsAgainst  # Adding Total League

def PointsForPointsAgainst():
    Trent()
    Tanner()
    Marco()
    Josh()
    Dylan()
    Jarod()
    Wyatt()
    Marcus()
    Jacob()
    Jagan()


    n = len(Players)
    # Creating Plot
    fig, ax = plt.subplots()
    index = np.arange(n)
    bar_width = .45
    opactiy = .85
    # Points For Bar
    Points_For = plt.bar(index + .2, LeaguePointsFor, bar_width,
                         alpha=opactiy, color='g', label='Total Points For')
    # Points Against Bar
    Points_Against = plt.bar(index + bar_width + .2, LeaguePointsAgainst, bar_width,
                             alpha=opactiy, color='r', label='Total Points Against')
    plt.title('Points for Vs. Points Against')  # Graph Title
    plt.xticks(index + bar_width, Players)  # Players with Bars
    plt.legend()
    plt.legend(loc = 'lower center')
    plt.show()


def AvgPointsForAgainst():

    Trent()
    AvgPersonalPointsFor = LeaguePointsFor[0] / len(Week)  # Avg Points For Per Week
    AvgPersonalPointsAgainst = LeaguePointsAgainst[0] / len(Week)  # Avg Points Against Per Week
    WeeklyAvgPointsFor.append(AvgPersonalPointsFor)  # Appending to Array
    WeeklyAvgPointsAgainst.append(AvgPersonalPointsAgainst)  # Appending to Array

    Tanner()
    AvgPersonalPointsFor = LeaguePointsFor[1] / len(Week)  # Avg Points For Per Week
    AvgPersonalPointsAgainst = LeaguePointsAgainst[1] / len(Week)  # Avg Points Against Per Week
    WeeklyAvgPointsFor.append(AvgPersonalPointsFor)  # Appending to Array
    WeeklyAvgPointsAgainst.append(AvgPersonalPointsAgainst)  # Appending to Array

    Marco()
    AvgPersonalPointsFor = LeaguePointsFor[2] / len(Week)  # Avg Points For Per Week
    AvgPersonalPointsAgainst = LeaguePointsAgainst[2] / len(Week)  # Avg Points Against Per Week
    WeeklyAvgPointsFor.append(AvgPersonalPointsFor)  # Appending to Array
    WeeklyAvgPointsAgainst.append(AvgPersonalPointsAgainst)  # Appending to Array

    Josh()
    AvgPersonalPointsFor = LeaguePointsFor[3] / len(Week)  # Avg Points For Per Week
    AvgPersonalPointsAgainst = LeaguePointsAgainst[3] / len(Week)  # Avg Points Against Per Week
    WeeklyAvgPointsFor.append(AvgPersonalPointsFor)  # Appending to Array
    WeeklyAvgPointsAgainst.append(AvgPersonalPointsAgainst)  # Appending to Array

    Dylan()
    AvgPersonalPointsFor = LeaguePointsFor[4] / len(Week)  # Avg Points For Per Week
    AvgPersonalPointsAgainst = LeaguePointsAgainst[4] / len(Week)  # Avg Points Against Per Week
    WeeklyAvgPointsFor.append(AvgPersonalPointsFor)  # Appending to Array
    WeeklyAvgPointsAgainst.append(AvgPersonalPointsAgainst)  # Appending to Array

    Jarod()
    AvgPersonalPointsFor = LeaguePointsFor[5] / len(Week)  # Avg Points For Per Week
    AvgPersonalPointsAgainst = LeaguePointsAgainst[5] / len(Week)  # Avg Points Against Per Week
    WeeklyAvgPointsFor.append(AvgPersonalPointsFor)  # Appending to Array
    WeeklyAvgPointsAgainst.append(AvgPersonalPointsAgainst)  # Appending to Array

    Wyatt()
    AvgPersonalPointsFor = LeaguePointsFor[6] / len(Week)  # Avg Points For Per Week
    AvgPersonalPointsAgainst = LeaguePointsAgainst[6] / len(Week)  # Avg Points Against Per Week
    WeeklyAvgPointsFor.append(AvgPersonalPointsFor)  # Appending to Array
    WeeklyAvgPointsAgainst.append(AvgPersonalPointsAgainst)  # Appending to Array

    Marcus()
    AvgPersonalPointsFor = LeaguePointsFor[7] / len(Week)  # Avg Points For Per Week
    AvgPersonalPointsAgainst = LeaguePointsAgainst[7] / len(Week)  # Avg Points Against Per Week
    WeeklyAvgPointsFor.append(AvgPersonalPointsFor)  # Appending to Array
    WeeklyAvgPointsAgainst.append(AvgPersonalPointsAgainst)  # Appending to Array

    Jacob()
    AvgPersonalPointsFor = LeaguePointsFor[8] / len(Week)  # Avg Points For Per Week
    AvgPersonalPointsAgainst = LeaguePointsAgainst[8] / len(Week)  # Avg Points Against Per Week
    WeeklyAvgPointsFor.append(AvgPersonalPointsFor)  # Appending to Array
    WeeklyAvgPointsAgainst.append(AvgPersonalPointsAgainst)  # Appending to Array

    Jagan()
    AvgPersonalPointsFor = LeaguePointsFor[9] / len(Week)  # Avg Points For Per Week
    AvgPersonalPointsAgainst = LeaguePointsAgainst[9] / len(Week)  # Avg Points Against Per Week
    WeeklyAvgPointsFor.append(AvgPersonalPointsFor)  # Appending to Array
    WeeklyAvgPointsAgainst.append(AvgPersonalPointsAgainst)  # Appending to Array
    Luck()

    x.field_names = ['Player', 'Position', 'Avg. Points For', 'Avg. Points Against']
    x.add_row([Players[0], CurrentPosition[0], round(WeeklyAvgPointsFor[0], 3), round(WeeklyAvgPointsAgainst[0], 3)])
    x.add_row([Players[1], CurrentPosition[1], round(WeeklyAvgPointsFor[1], 3), round(WeeklyAvgPointsAgainst[1], 3)])
    x.add_row([Players[2], CurrentPosition[2], round(WeeklyAvgPointsFor[2], 3), round(WeeklyAvgPointsAgainst[2], 3)])
    x.add_row([Players[3], CurrentPosition[3], round(WeeklyAvgPointsFor[3], 3), round(WeeklyAvgPointsAgainst[3], 3)])
    x.add_row([Players[4], CurrentPosition[4], round(WeeklyAvgPointsFor[4], 3), round(WeeklyAvgPointsAgainst[4], 3)])
    x.add_row([Players[5], CurrentPosition[5], round(WeeklyAvgPointsFor[5], 3), round(WeeklyAvgPointsAgainst[5], 3)])
    x.add_row([Players[6], CurrentPosition[6], round(WeeklyAvgPointsFor[6], 3), round(WeeklyAvgPointsAgainst[6], 3)])
    x.add_row([Players[7], CurrentPosition[7], round(WeeklyAvgPointsFor[7], 3), round(WeeklyAvgPointsAgainst[7], 3)])
    x.add_row([Players[8], CurrentPosition[8], round(WeeklyAvgPointsFor[8], 3), round(WeeklyAvgPointsAgainst[8], 3)])
    x.add_row([Players[9], CurrentPosition[9], round(WeeklyAvgPointsFor[9], 3), round(WeeklyAvgPointsAgainst[9], 3)])
    print(x)

def Luck():
    PersonalLuck = []

    TotalLeaguePointsAgainst = sum(WeeklyAvgPointsAgainst) / len(Players)
    PersonalLuck.append(TotalLeaguePointsAgainst - WeeklyAvgPointsAgainst[0])
    PersonalLuck.append(TotalLeaguePointsAgainst - WeeklyAvgPointsAgainst[1])
    PersonalLuck.append(TotalLeaguePointsAgainst - WeeklyAvgPointsAgainst[2])
    PersonalLuck.append(TotalLeaguePointsAgainst - WeeklyAvgPointsAgainst[3])
    PersonalLuck.append(TotalLeaguePointsAgainst - WeeklyAvgPointsAgainst[4])
    PersonalLuck.append(TotalLeaguePointsAgainst - WeeklyAvgPointsAgainst[5])
    PersonalLuck.append(TotalLeaguePointsAgainst - WeeklyAvgPointsAgainst[6])
    PersonalLuck.append(TotalLeaguePointsAgainst - WeeklyAvgPointsAgainst[7])
    PersonalLuck.append(TotalLeaguePointsAgainst - WeeklyAvgPointsAgainst[8])
    PersonalLuck.append(TotalLeaguePointsAgainst - WeeklyAvgPointsAgainst[9])

    print(PersonalLuck)
    n = len(Players)
    # Creating Plot
    fig, ax = plt.subplots()
    index = np.arange(n)
    bar_width = .45
    opactiy = .85
    Colors = []
    for i in PersonalLuck:
        if i >= 0:
            Colors.append('g')
        else:
            Colors.append('r')
    plt.bar(index + .5, PersonalLuck, bar_width, alpha=opactiy, color=Colors, label='Personal Luck')
    plt.axhline(y=0, color = 'b')
    plt.title('Who is the Luckiest?')  # Graph Title
    plt.xticks(index + bar_width, Players)  # Players with Bars
    plt.legend()
    plt.show()

def WeeklyPosition():
    Trent()
    plt.plot(Week, LeaguePosition[0], color='darkblue', label='Trent')  # Create Plot for Playe
    Tanner()
    plt.plot(Week, LeaguePosition[1], color='slateblue', label='Tanner')  # Create Plot for Player
    Marco()
    plt.plot(Week,LeaguePosition[2], color='rebeccapurple', label='Marco')  # Create Plot for Player

    Josh()
    plt.plot(Week,LeaguePosition[3], color='teal', label='Josh')  # Create Plot for Player
    Dylan()
    plt.plot(Week, LeaguePosition[4], color='turquoise', label='Dylan')  # Create Plot for Player
    Jarod()
    plt.plot(Week,LeaguePosition[5], color='cyan', label='Jarod')  # Create Plot for Player
    Wyatt()
    plt.plot(Week, LeaguePosition[6], color='lime', label='Wyatt')  # Create Plot for Player
    Marcus()
    plt.plot(Week, LeaguePosition[7], color='yellow', label='Marcus')  # Create Plot for Player
    Jacob()
    plt.plot(Week, LeaguePosition[8], color='tomato', label='Jacob')  # Create Plot for Player
    Jagan()
    plt.plot(Week, LeaguePosition[9], color='goldenrod', label='Jagan')  # Create Plot for Player



    plt.gca().invert_yaxis() #Reverses Y axis
    plt.title('Weekly Position') #Plot Title
    plt.xticks(Week) #Setting X-Axis
    plt.xlabel('Week #') #X label title
    plt.ylabel('Position') #Y label title
    #plt.legend(bbox_to_anchor=(1.05, 1))
    plt.legend(bbox_to_anchor=(1, 1.0), loc='upper left', prop={'size': 6})
    #plt.legend(loc = 'lower center') #Make legend
    plt.show() #Display Plot

def WeeklyPointsFor():
    Trent()
    plt.plot(Week, WeeklyPoints[0], color='darkblue', label='Trent')  # Create Plot for Playe
    Tanner()
    plt.plot(Week, WeeklyPoints[1], color='slateblue', label='Tanner')  # Create Plot for Player
    Marco()
    plt.plot(Week, WeeklyPoints[2], color='rebeccapurple', label='Marco')  # Create Plot for Player
    Josh()
    plt.plot(Week, WeeklyPoints[3], color='teal', label='Josh')  # Create Plot for Player
    Dylan()
    plt.plot(Week, WeeklyPoints[4], color='turquoise', label='Dylan')  # Create Plot for Player
    Jarod()
    plt.plot(Week, WeeklyPoints[5], color='cyan', label='Jarod')  # Create Plot for Player
    Wyatt()
    plt.plot(Week, WeeklyPoints[6], color='lime', label='Wyatt')  # Create Plot for Player
    Marcus()
    plt.plot(Week, WeeklyPoints[7], color='orange', label='Marcus')  # Create Plot for Player
    Jacob()
    plt.plot(Week, WeeklyPoints[8], color='tomato', label='Jacob')  # Create Plot for Player
    Jagan()
    plt.plot(Week, WeeklyPoints[9], color='goldenrod', label='Jagan')  # Create Plot for Player



    plt.title('Weekly Points Scored') #Plot Title
    plt.xticks(Week)
    plt.xlabel('Week #') #X label title
    plt.ylabel('Points Scored') #Y label title
    #plt.legend(loc = 'lower center') #Make legend
    plt.legend(bbox_to_anchor=(1, 1.0), loc='upper left', prop={'size': 6})
    plt.show() #Display Plot

def Plots():
    PointsForPointsAgainst()
    WeeklyPosition()
    WeeklyPointsFor()
    AvgPointsForAgainst()

Plots()
