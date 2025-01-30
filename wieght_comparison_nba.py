from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

player_dict = players.find_players_by_full_name("LeBron James")
player_id = player_dict[0]['id']


# Get detailed player info, including weight
player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_data_frames()[0]

# Extract player's weight
player_weight = player_info['WEIGHT'][0]
print(f"LeBron James weighs {player_weight} lbs")



from nba_api.stats.endpoints import LeagueDashPlayerShotLocations
seasons = ['2005-06','2006-07','2007-08','2012-13','2013-14','2014-15','2021-22','2022-23','2023-24']
season_numbers = [5, 6, 7, 12,13,14,21,22,23]



#note for later: Convert Center - forward to center and forward center to forward

df = pd.read_csv('players_weights.csv',sep = ';')
#Turn lbs into kg
df['WEIGHT'] = df['WEIGHT']*0.453

#split by the years you wanna hold
num_1 = (5,6,7)
num_2 = (12,13,14)
num_3 = (22,23,24)
df1 = df[df['SEASON_NUMBER'].isin(num_1)]
df2 = df[df['SEASON_NUMBER'].isin(num_2)]
df3 = df[df['SEASON_NUMBER'].isin(num_3)]


 #Just from this kdeplot it becomes evident that players nowadays tend to be lighter than they used to be. But how is that translated to specific positions?  
import seaborn as sns

# Plot all three KDE plots on the same figure
sns.kdeplot(data=df1, x='WEIGHT', fill=True, label='df1')
sns.kdeplot(data=df2, x='WEIGHT', fill=True, label='df2')
sns.kdeplot(data=df3, x='WEIGHT', fill=True, label='df3')

# Add a legend to differentiate the KDE plots
plt.legend()

# Display the plot
plt.show()

#split them into one picture
#Here we can actually see that players over 140kg are almost extinct today
# Create a 1x3 grid of subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns

# Plot each KDE plot on a separate subplot
sns.kdeplot(data=df1, x='WEIGHT', fill=True, ax=axes[0])
axes[0].set_title('WEIGHT Distribution for 2005-2007')

sns.kdeplot(data=df2, x='WEIGHT', fill=True, ax=axes[1])
axes[1].set_title('WEIGHT Distribution for 2012-2014')

sns.kdeplot(data=df3, x='WEIGHT', fill=True, ax=axes[2])
axes[2].set_title('WEIGHT Distribution for 2022-2024')

# Adjust layout
plt.tight_layout()

# Display the figure
plt.show()


#split by position
#guards
df1_G = df1[df1['POSITION']=='Guard']
df2_G = df2[df2['POSITION']=='Guard']
df3_G = df3[df3['POSITION']=='Guard']

#forwards
df1_F = df1[df1['POSITION']=='Forward']
df2_F = df2[df2['POSITION']=='Forward']
df3_F = df3[df3['POSITION']=='Forward']

#centers
df1_C = df1[df1['POSITION']=='Center']
df2_C = df2[df2['POSITION']=='Center']
df3_C = df3[df3['POSITION']=='Center']



#GUARDS
# Plot all three KDE plots on the same figure
sns.kdeplot(data=df1_G, x='WEIGHT', fill=True, label='df1')
sns.kdeplot(data=df2_G, x='WEIGHT', fill=True, label='df2')
sns.kdeplot(data=df3_G, x='WEIGHT', fill=True, label='df3')

# Add a legend to differentiate the KDE plots
plt.legend()

# Display the plot
plt.show()

#split them into one picture
#Here we can actually see that players over 140kg are almost extinct today
# Create a 1x3 grid of subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns

# Plot each KDE plot on a separate subplot
sns.kdeplot(data=df1_G, x='WEIGHT', fill=True, ax=axes[0])
axes[0].set_title('Guard WEIGHT Distribution for 2005-2007')

sns.kdeplot(data=df2_G, x='WEIGHT', fill=True, ax=axes[1])
axes[1].set_title('Guard WEIGHT Distribution for 2012-2014')

sns.kdeplot(data=df3_G, x='WEIGHT', fill=True, ax=axes[2])
axes[2].set_title('Guard WEIGHT Distribution for 2022-2024')



#FORWARDS
sns.kdeplot(data=df1_F, x='WEIGHT', fill=True, label='df1')
sns.kdeplot(data=df2_F, x='WEIGHT', fill=True, label='df2')
sns.kdeplot(data=df3_F, x='WEIGHT', fill=True, label='df3')

# Add a legend to differentiate the KDE plots
plt.legend()

# Display the plot
plt.show()

#split them into one picture
#Here we can actually see that players over 140kg are almost extinct today
# Create a 1x3 grid of subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns

# Plot each KDE plot on a separate subplot
sns.kdeplot(data=df1_F, x='WEIGHT', fill=True, ax=axes[0])
axes[0].set_title('Forward WEIGHT Distribution for 2005-2007')

sns.kdeplot(data=df2_F, x='WEIGHT', fill=True, ax=axes[1])
axes[1].set_title('Forward WEIGHT Distribution for 2012-2014')

sns.kdeplot(data=df3_F, x='WEIGHT', fill=True, ax=axes[2])
axes[2].set_title('Forward WEIGHT Distribution for 2022-2024')




#CENTERS
sns.kdeplot(data=df1_C, x='WEIGHT', fill=True, label='df1')
sns.kdeplot(data=df2_C, x='WEIGHT', fill=True, label='df2')
sns.kdeplot(data=df3_C, x='WEIGHT', fill=True, label='df3')

# Add a legend to differentiate the KDE plots
plt.legend()

# Display the plot
plt.show()

#split them into one picture
#Here we can actually see that players over 140kg are almost extinct today
# Create a 1x3 grid of subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns

# Plot each KDE plot on a separate subplot
sns.kdeplot(data=df1_C, x='WEIGHT', fill=True, ax=axes[0])
axes[0].set_title('Center WEIGHT Distribution for 2005-2007')

sns.kdeplot(data=df2_C, x='WEIGHT', fill=True, ax=axes[1])
axes[1].set_title('Center WEIGHT Distribution for 2012-2014')

sns.kdeplot(data=df3_C, x='WEIGHT', fill=True, ax=axes[2])
axes[2].set_title('Center WEIGHT Distribution for 2022-2024')





import seaborn as sns
import matplotlib.pyplot as plt

# Create a 3x3 grid of subplots
fig, axes = plt.subplots(3, 3, figsize=(15, 10))  # 3 rows, 3 columns

# Plot each KDE plot on a separate subplot
# Guard WEIGHT distributions
sns.kdeplot(data=df1_G, x='WEIGHT', fill=True, ax=axes[0, 0])
axes[0, 0].set_title('Guard WEIGHT Distribution for 2005-2007')

sns.kdeplot(data=df2_G, x='WEIGHT', fill=True, ax=axes[0, 1])
axes[0, 1].set_title('Guard WEIGHT Distribution for 2012-2014')

sns.kdeplot(data=df3_G, x='WEIGHT', fill=True, ax=axes[0, 2])
axes[0, 2].set_title('Guard WEIGHT Distribution for 2022-2024')

# Forward WEIGHT distributions
sns.kdeplot(data=df1_F, x='WEIGHT', fill=True, ax=axes[1, 0])
axes[1, 0].set_title('Forward WEIGHT Distribution for 2005-2007')

sns.kdeplot(data=df2_F, x='WEIGHT', fill=True, ax=axes[1, 1])
axes[1, 1].set_title('Forward WEIGHT Distribution for 2012-2014')

sns.kdeplot(data=df3_F, x='WEIGHT', fill=True, ax=axes[1, 2])
axes[1, 2].set_title('Forward WEIGHT Distribution for 2022-2024')

# Center WEIGHT distributions
sns.kdeplot(data=df1_C, x='WEIGHT', fill=True, ax=axes[2, 0])
axes[2, 0].set_title('Center WEIGHT Distribution for 2005-2007')

sns.kdeplot(data=df2_C, x='WEIGHT', fill=True, ax=axes[2, 1])
axes[2, 1].set_title('Center WEIGHT Distribution for 2012-2014')

sns.kdeplot(data=df3_C, x='WEIGHT', fill=True, ax=axes[2, 2])
axes[2, 2].set_title('Center WEIGHT Distribution for 2022-2024')

# Adjust layout to avoid overlapping
plt.tight_layout()

# Display the figure
plt.show()



sns.boxplot(data=df1_C, x='WEIGHT')



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Combine the data into one DataFrame
df1_G['Position'] = 'Guard'
df1_G['Period'] = '2005-2007'
df2_G['Position'] = 'Guard'
df2_G['Period'] = '2012-2014'
df3_G['Position'] = 'Guard'
df3_G['Period'] = '2022-2024'

df1_F['Position'] = 'Forward'
df1_F['Period'] = '2005-2007'
df2_F['Position'] = 'Forward'
df2_F['Period'] = '2012-2014'
df3_F['Position'] = 'Forward'
df3_F['Period'] = '2022-2024'

df1_C['Position'] = 'Center'
df1_C['Period'] = '2005-2007'
df2_C['Position'] = 'Center'
df2_C['Period'] = '2012-2014'
df3_C['Position'] = 'Center'
df3_C['Period'] = '2022-2024'

# Concatenate all the data into one DataFrame
df_combined = pd.concat([df1_G, df2_G, df3_G, df1_F, df2_F, df3_F, df1_C, df2_C, df3_C])

# Create a boxplot with WEIGHT as the x-axis, and Position and Period as the y-axis
plt.figure(figsize=(10, 8))
sns.boxplot(x='WEIGHT', y='Position', hue='Period', data=df_combined)

# Show the plot
plt.tight_layout()
plt.show()
