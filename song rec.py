'''import csv
f=open("val.csv","w")
data = [
    ["mood", "song"],
    ["happy", "Pharrell Williams - Happy"],
    ["happy", "Bruno Mars - Treasure"],
    ["happy", "Katy Perry - Firework"],
    ["sad", "Adele - Someone Like You"],
    ["sad", "Billie Eilish - idontwannabeyouanymore"],
    ["sad", "Lewis Capaldi - Before You Go"],
    ["chill", "Joji - Slow Dancing in the Dark"],
    ["chill", "Lauv - I Like Me Better"],
    ["chill", "Keshi - Right Here"],
    ["energetic", "Imagine Dragons - Believer"],
    ["energetic", "Linkin Park - Burn It Down"],
    ["energetic", "David Guetta - Titanium"]
]
wr= csv.writer(f)
wr.writerows(data)
f.close()
'''
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("val.csv")  # your CSV name

# Separate input (mood) and output (song)
X = df['mood']   # words like happy, sad, etc.
y = df['song']   # songs

# Convert text moods into numerical vectors
vectorizer = CountVectorizer()
X_vectors = vectorizer.fit_transform(X)

# Encode song names into numbers
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Build the model
model = LogisticRegression()
model.fit(X_vectors, y_encoded)

# ---- TEST ----
test_mood = "happy"     # you can change this
test_vec = vectorizer.transform([test_mood])
pred = model.predict(test_vec)
song = encoder.inverse_transform(pred)[0]

print("Recommended song:", song)
