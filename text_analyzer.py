#!/usr/bin/env python
# coding: utf-8

# In[2]:


def read_file(sample):
    try:
        with open(sample, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file {sample} does not exist.")
        return None

def count_words(text):
    words = text.split()
    return len(words)

def count_lines(text):
    lines = text.split('\n')
    return len(lines)

def count_characters(text):
    return len(text)

def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def display_results(text):
    print(f"Word count: {count_words(text)}")
    print(f"Line count: {count_lines(text)}")
    print(f"Character count: {count_characters(text)}")
    print("\nWord frequencies:")
    frequencies = word_frequency(text)
    for word, count in sorted(frequencies.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}: {count}")

if __name__ == "__main__":
    filename = 'sample.txt'
    text_content = read_file(filename)
    if text_content:
        display_results(text_content)


# In[4]:


# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Function to read the content of a file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None

# Function to count the number of words in the text
def count_words(text):
    words = text.split()
    return len(words)

# Function to count the number of lines in the text
def count_lines(text):
    lines = text.split('\n')
    return len(lines)

# Function to count the number of characters in the text
def count_characters(text):
    return len(text)

# Function to calculate the frequency of each word in the text
def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Function to display the analysis results and plot the word frequencies
def display_results(text):
    print(f"Word count: {count_words(text)}")
    print(f"Line count: {count_lines(text)}")
    print(f"Character count: {count_characters(text)}")
    
    # Calculate word frequencies
    frequencies = word_frequency(text)
    
    # Print word frequencies
    print("\nWord frequencies:")
    for word, count in sorted(frequencies.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}: {count}")
    
    # Plot word frequencies
    plot_word_frequencies(frequencies)

# Function to plot word frequencies
def plot_word_frequencies(frequencies):
    # Convert frequency dictionary to a DataFrame
    freq_df = pd.DataFrame(list(frequencies.items()), columns=['Word', 'Frequency'])
    
    # Sort the DataFrame by frequency in descending order
    freq_df = freq_df.sort_values(by='Frequency', ascending=False)
    
    # Plot the frequencies
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Frequency', y='Word', data=freq_df.head(20))  # Plotting top 20 words
    plt.title('Top 20 Word Frequencies')
    plt.xlabel('Frequency')
    plt.ylabel('Word')
    plt.show()

# Sample text content
sample_text_content = """
This is a sample text file.
It contains multiple lines and multiple words.
This file is used to demonstrate a text file analyzer.

Feel free to add more content to test the text file analyzer project.
This project helps in understanding file handling and text processing in Python.
Analyzing text files can be very useful in various applications.

Enjoy learning Python programming!
"""

# Save the sample text content to a file named sample.txt
with open('sample.txt', 'w') as file:
    file.write(sample_text_content)

# Read and analyze the file content
filename = 'sample.txt'
text_content = read_file(filename)
if text_content:
    display_results(text_content)


# In[8]:


# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Function to read the content of a file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None

# Function to count the number of words in the text
def count_words(text):
    words = text.split()
    return len(words)

# Function to count the number of lines in the text
def count_lines(text):
    lines = text.split('\n')
    return len(lines)

# Function to count the number of characters in the text
def count_characters(text):
    return len(text)

# Function to calculate the frequency of each word in the text
def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Function to display the analysis results and plot the word frequencies
def display_results(text):
    print(f"Word count: {count_words(text)}")
    print(f"Line count: {count_lines(text)}")
    print(f"Character count: {count_characters(text)}")
    
    # Calculate word frequencies
    frequencies = word_frequency(text)
    
    # Print word frequencies
    print("\nWord frequencies:")
    for word, count in sorted(frequencies.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}: {count}")
    
    # Plot word frequencies
    plot_word_frequencies(frequencies)

# Function to plot word frequencies as a pie chart
def plot_word_frequencies(frequencies):
    # Convert frequency dictionary to a DataFrame
    freq_df = pd.DataFrame(list(frequencies.items()), columns=['Word', 'Frequency'])
    
    # Sort the DataFrame by frequency in descending order
    freq_df = freq_df.sort_values(by='Frequency', ascending=False)
    
    # Select the top 20 words
    top_words = freq_df.head(20)
    
    # Plot the frequencies as a pie chart
    plt.figure(figsize=(10, 8))
    plt.pie(top_words['Frequency'], labels=top_words['Word'], autopct='%1.1f%%', startangle=140)
    plt.title('Top 20 Word Frequencies')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

# Sample text content
sample_text_content = """
This is a sample text file.
It contains multiple lines and multiple words.
This file is used to demonstrate a text file analyzer.

Feel free to add more content to test the text file analyzer project.
This project helps in understanding file handling and text processing in Python.
Analyzing text files can be very useful in various applications.

Enjoy learning Python programming!
"""

# Save the sample text content to a file named sample.txt
with open('sample.txt', 'w') as file:
    file.write(sample_text_content)

# Read and analyze the file content
filename = 'sample.txt'
text_content = read_file(filename)
if text_content:
    display_results(text_content)


# In[ ]:




