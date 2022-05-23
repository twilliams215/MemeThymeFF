import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import prettytable




#Currently trying to import the individual's numbers from the excel file
#So that I can just update the sheet instead of the code each time.
#Then I'll create individual sheets for position/points against etc.

Players = ['Trent', 'Tanner', 'Marco', 'Josh', 'Dylan', 'Jarod', 'Wyatt', 'Marcus', 'Jacob', 'Jagan']
Colors = ['lightcoral', 'orangered', 'gold', 'greenyellow', 'darkgreen',
          'aquamarine', 'dodgerblue', 'indigo', 'deeppink', 'tan']
Week = [1, 2, 3, 4, 5, 6]

def read_data():
    #global Players
    df_pos = pd.read_excel('Team_Scores.xlsx', sheet_name = 'Team_Position')
    df_pf = pd.read_excel('Team_Scores.xlsx', sheet_name = 'Team_Scores_For')
    df_pa = pd.read_excel('Team_Scores.xlsx', sheet_name = 'Team_Scores_Against')

    for name in Players:
        globals()[name] = []
        globals()[name].append(df_pos[name][0:len(Week)].to_numpy()) #Appending Weekly Position to Player Array
        globals()[name].append(df_pf[name][0:len(Week)].to_numpy()) #Appending Points For to Player Array
        globals()[name].append(df_pa[name][0:len(Week)].to_numpy()) #Appending Points Against to Player Array

read_data()

def PointsForAgainst():

    TotalPointsFor = []
    TotalPointsAgainst = []

    for name in Players:
        TotalPointsFor.append(sum(globals()[name][1])) #Taking the sum of the weekly points for array
        TotalPointsAgainst.append(sum(globals()[name][2])) #Taking the sum of the weekly points against array


    n = len(Players)
    # Creating Plot
    fig, ax = plt.subplots()
    index = np.arange(n)
    bar_width = .45
    opactiy = .85
    # Points For Bar
    Points_For = plt.bar(index + .2, TotalPointsFor, bar_width,
                         alpha=opactiy, color='g', label='Total Points For')
    # Points Against Bar
    Points_Against = plt.bar(index + bar_width + .2, TotalPointsAgainst, bar_width,
                             alpha=opactiy, color='r', label='Total Points Against')
    plt.title('Points for Vs. Points Against')  # Graph Title
    plt.xticks(index + bar_width, Players)  # Players with Bars
    plt.legend()
    plt.legend(loc = 'lower center')
    plt.show()

def WeeklyPosition():
    count = 0
    for name in Players:
        plt.plot(Week, globals()[name][0], color = Colors[count], label = Players[count])
        count += 1

    plt.gca().invert_yaxis() #Reverses Y axis
    plt.title('Weekly Position') #Plot Title
    plt.xticks(Week) #Setting X-Axis
    plt.xlabel('Week #') #X label title
    plt.ylabel('Position') #Y label title
    #plt.legend(bbox_to_anchor=(1.05, 1))
    plt.legend(bbox_to_anchor=(1, 1.0), loc='upper left', prop={'size': 6})
    #plt.legend(loc = 'lower center') #Make legend
    plt.show() #Display Plot

PointsForAgainst()
WeeklyPosition()


#print(Trent)



#Trent = df_pf['Trent'][0:6].to_numpy()
#Tanner = Points_For['Tanner'][0:6].to_numpy()
#Marco = Points_For['Marco'][0:6].to_numpy()
#Josh = Points_For['Josh'][0:6].to_numpy()
#Dylan = Points_For['Dylan'][0:6].to_numpy()
#Jarod = Points_For['Jarod'][0:6].to_numpy()
#Wyatt = Points_For['Wyatt'][0:6].to_numpy()
#Marcus = Points_For['Marcus'][0:6].to_numpy()
#Jagan = Points_For['Jagan'][0:6].to_numpy()
#Jacob = Points_For['Jacob'][0:6].to_numpy()


#Sources
#
#Using Globals to create and assign names to list
#https://stackoverflow.com/questions/4687364/assigning-values-to-variables-in-a-list-using-a-loop
