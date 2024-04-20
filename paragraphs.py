import pandas as pd
import spacy
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Load the English model
en = spacy.load('en_core_web_sm')

# Open the file in read mode
with open('random_paragraphs.txt', 'r') as file:
    # Read the entire random_paragraphs content
    random_paragraphs_content = file.readlines()

# Create a DataFrame from random_paragraphs.txt
df = pd.DataFrame(random_paragraphs_content, columns=['Content'])

# Print the DataFrame
print(df.tail())

# Print the column names
print(df.columns)

# Check for null values
print(df.isnull().sum())

# Remove stop words
df['content_clean'] = df['Content'].apply(lambda text: ' '.join([token.text for token in en(text) if not token.is_stop]))

# Print the head of the DataFrame
print(df.head())

# Drop the 'Content' column
df.drop(columns=['Content'], inplace=True)

# Print the tail of the DataFrame
print(df.tail())

# Count the frequency of each word in the processed text
word_frequency = Counter()

# Iterate through each row
for text in df['content_clean']:
    word_frequency.update(text.split())

# Convert to DataFrame and sort it
word_frequency_df = pd.DataFrame(word_frequency.items(), columns=['words', 'frequency'])
word_frequency_df = word_frequency_df.sort_values(by='frequency', ascending=True)

# Print the shape of the DataFrame
print(word_frequency_df.shape)

# Print the top 7 most frequent words
print(word_frequency_df.head(7))

# Set the style and color palette
sns.set_style("whitegrid")
palette = sns.color_palette("viridis", len(word_frequency_df['words'][1010:1025]))

# Create a bar plot
plt.figure(figsize=(12, 8))
sns.barplot(x=word_frequency_df['words'][1010:1025], y=word_frequency_df['frequency'][1010:1025], palette=palette)

# Set labels and title
plt.xlabel('Words', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('Top 15 Most Frequent Words', fontsize=16)

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Prevent clipping of labels
plt.tight_layout()

# Show the plot
plt.show()

# Print the word frequency count to the console
print("Word Frequency Count:")
for index, row in word_frequency_df.iterrows():
    print(f"Word: {row['words']}, Frequency: {row['frequency']}")
