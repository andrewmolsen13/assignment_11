import pandas as pd

#Read the CSV file
raw_video_games = pd.read_csv("video_games_raw.csv")

#Ask user for a specific row
menu = raw_video_games.index.tolist()
menu_run = True

print(f"Video Game Catalog\n")
while menu_run:
    try:
        selection = int(input(f"Please select a row to examine from this list {menu}: "))
        while selection not in menu:
            selection = int(input("Please enter a number from the list: "))
        menu_run = False
    except ValueError:
        print("Please enter a number\n")

#Use iloc[] to display selected game
selected_game = raw_video_games.iloc[selection]
print("\n")
print(selected_game.to_string())

#Ask user to enter new status: Backlog, Playing, Completed, or Dropped
status_menu = raw_video_games["Status"].unique().tolist()
new_status_menu = True
while new_status_menu:
    new_status = input(f"Enter a new status for {selected_game['Title']} (Backlog, Playing, Completed, or Dropped): ").capitalize()
    new_status_menu = False
    while new_status not in status_menu:
            new_status = input("Please input a valid status").capitalize()

#use .at[] to update the selected games status
raw_video_games.at[selection, "Status"] = new_status

#add a recommended column to the panda
raw_video_games["Recommended"] = "No"
#set recommended to yes for games that have a rating of 8 and price is <= $40
#and no for everything else
raw_video_games.loc[(raw_video_games["Rating"]>=8)& (raw_video_games["Price"]<=40), "Recommended"] = "Yes"

#use .query() to display recommended games 
print(raw_video_games.query("Recommended == 'Yes'")[["Title", "Platform", "Price", "Rating", "Recommended"]]) 

#save updated data to a new file named video_games_cleaned.csv
raw_video_games.to_csv("video_games_cleaned.csv", index = False)