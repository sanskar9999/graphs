# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Create a dictionary of participants and their scores
participants = {
    "Mores": [47,73,53,67,70,63,93,50,47],
    "Caff": [67,80,100,63,97,73,80,27,100],
    "Callum": [43,87,100,87,63,83,57,93,90],
    "Yuzu": [97,63,100,80,100,93,83,80,10],
    "Ruru": [83,70,47,37,57,50,57,13,100],
    "Geo": [67,53,73,43,60,67,90,63,93],
    "Sparkie": [93,97,80,60,83,77,97,70,100],
    "Cummy": [67,77,40,83,73,90,80,77,70]
}
# Create a list of intelligence types
intelligences = ["Linguistic", "Logical-mathematical", "Musical", "Bodily-kinesthetic", "Spatial-Visual", "Inter-personal", "Intra-personal", "Naturalistic", "Existential"]
# Create a pandas dataframe from the dictionary
df = pd.DataFrame(participants)
# Set the index of the dataframe to the intelligence types
df.index = intelligences
# Transpose the dataframe to swap rows and columns
df = df.T
# Plot a heatmap of the dataframe using seaborn
plt.figure(figsize=(12,8)) # Set the figure size
sns.heatmap(df,cmap="YlGnBu",annot=True) # Create a heatmap with color map and annotations
plt.title("Scores of participants in an intelligence test") # Set the title of the plot
plt.xlabel("Intelligence type") # Set the x-axis label
plt.ylabel("Participant name") # Set the y-axis label
plt.show() # Show the plot
