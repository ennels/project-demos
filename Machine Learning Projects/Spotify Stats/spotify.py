# AICC 210 - Machine Learning - Lab 1 - Elijah Walker

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


train = pd.read_csv('spotify_data_processed.csv')


# --- Manual data previews ---
# print(train.shape, test.shape)
# train.info()
# print(train.describe())
# print(train.head())
# print(train['SalePrice'].describe())
# print(train['YearBuilt'].max())


# --- Handle missing data ---
missing = train.isnull().sum()
missing = missing[missing > 0]
pct = (missing / len(train) * 100).round(1)
pd.DataFrame({'n_missing': missing,
              'pct_missing': pct}
             ).sort_values('pct_missing', ascending=False)
# print(f"MISSING (VALUES):\n\n({missing}\n\n\n"
#       f"MISSING (PERCENTAGES):\n\n{pct}\n")

# The Spotify dataset doesn't have any missing values,
# so we don't have to do anything there. Yippee.

# It's also largely classification/categorical data,
# so no need to address outliers.


# --- Encode categoricals ---
# Ordinal
dow_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
           'Friday': 4, 'Saturday': 5, 'Sunday': 6}
train['release_day_of_week'] = train['release_day_of_week'].map(dow_map)

# Bools
train['is_weekend_release'] = train['is_weekend_release'].astype(int)
train['is_explicit_bool']   = train['is_explicit_bool'].astype(int)

# Nominal
train = pd.get_dummies(train, columns=['genre', 'country', 'label'],
                       drop_first=True, dtype=int)

# Drop text duplicates of numeric columns
train = train.drop(columns=['key_name', 'mode_name', 'loudness_category'])


# --- Get rid of select columns and split for testing ---
# "Let’s assume I am not interested in the track_id,
# track_name, artist_name, or album_name."
x = train.drop(columns=['track_id', 'track_name', 'artist_name', 'album_name',
                        'release_date',
                        'popularity', 'popularity_category'])
y = train['popularity']  # assuming that's what we're predicting...
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)


# --- Feature scaling ---
num_cols = ['duration_ms', 'loudness', 'tempo', 'danceability', 'energy',
            'instrumentalness', 'upbeat_score', 'release_year',
            'artist_track_count', 'stream_count', 'log_stream_count']

scaler = StandardScaler()
x_train[num_cols] = scaler.fit_transform(x_train[num_cols])
x_test[num_cols] = scaler.transform(x_test[num_cols])


# --- Visualize it! (correlation heatmap + boxplot) ---
# corr = train.corr(numeric_only=True)
# top = corr['popularity'].abs().sort_values(ascending=False)[1:11]

# sns.heatmap(train[top.index.tolist() + ['popularity']].corr(),
#             annot=True, cmap='RdBu_r', vmin=-1, vmax=1)
# plt.figure()
# sns.boxplot(data=train, x='genre', y='popularity')
# plt.xticks(rotation=45)
# plt.show()
