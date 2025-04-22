def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],  # Insert
                                  dp[i-1][j],  # Remove
                                  dp[i-1][j-1]  # Replace
                                  )

    return dp[m][n]

def correct_spelling(query, dictionary):
    corrected_query = query.lower()  # Convert to lowercase for case-insensitive correction
    suggestions = []

    for word in dictionary:
        distance = edit_distance(corrected_query, word.lower())
        if distance <= 2:  # You can adjust this threshold based on your preference
            suggestions.append((word, distance))

    suggestions.sort(key=lambda x: x[1])  # Sort by distance in ascending order
    return suggestions

# Example usage
dictionary = ["information", "retrieval", "spelling", "correction", "system"]

query = input("Enter your query: ")
suggestions = correct_spelling(query, dictionary)

if suggestions:
    print("Did you mean:")
    for suggestion, distance in suggestions:
        print(f"{suggestion} (Edit Distance: {distance})")
else:
    print("No suggestions found.")
