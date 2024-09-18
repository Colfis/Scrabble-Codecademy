Python Code Below:

# List of letters and their corresponding point values
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Combine letters and points into a dictionary
letter_to_points = dict(zip(letters, points))
# Add a blank tile with a point value of 0
letter_to_points[" "] = 0

# Function to calculate the score of a word
def score_word(word):
    point_total = 0
    # Loop through each letter in the word and add its point value
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total

# Example word to test the function
brownie_points = score_word("BROWNIE")
print(brownie_points)  # Should output 15

# Dictionary of players and the words they've played
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# Dictionary to store the total points of each player
player_to_points = {}

# Calculate points for each player
for player, words in player_to_words.items():
    player_points = 0
    # Sum the points for each word the player has played
    for word in words:
        player_points += score_word(word)
    # Store the total points for the player
    player_to_points[player] = player_points

# Print out the current standings
print(player_to_points)

