import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import ast

df = pd.read_csv('movies_clean.csv')

def parse_genres(val):
    if isinstance(val, str):
        try:
            parsed = ast.literal_eval(val)
            if isinstance(parsed, list):
                return [item['name'].lower() if isinstance(item, dict)
                        else str(item).lower() for item in parsed]
        except:
            return [g.strip().lower() for g in val.split(',') if g.strip()]
    return []

df['genres_list'] = df['genres'].apply(parse_genres)

C = df['vote_average'].mean()
m = df['vote_count'].quantile(0.70)
df['weighted_rating'] = (
    (df['vote_count'] / (df['vote_count'] + m)) * df['vote_average'] +
    (m / (df['vote_count'] + m)) * C
)

df['popularity_norm'] = (
    (df['popularity'] - df['popularity'].min()) /
    (df['popularity'].max() - df['popularity'].min() + 1e-9)
)

def runtime_bucket(mins):
    if mins <= 0:    return 'unknown'
    elif mins < 60:  return 'short'
    elif mins < 100: return 'medium'
    elif mins < 150: return 'standard'
    else:            return 'long'

df['runtime_bucket'] = df['runtime'].apply(runtime_bucket)

def recommend_movie(
    genre=None, mood_keywords=None, year_range=None,
    min_rating=0.0, popularity="any", language=None, runtime=None
):
    data = df.copy()

    if genre:
        data = data[data['genres_list'].apply(
            lambda g: genre.strip().lower() in g)]
    if year_range:
        data = data[
            (data['release_year'] >= year_range[0]) &
            (data['release_year'] <= year_range[1])]
    if min_rating > 0:
        data = data[data['vote_average'] >= min_rating]
    if language and language.lower() != 'any':
        data = data[data['original_language'] == language.lower()]
    if runtime and runtime.lower() != 'any':
        data = data[data['runtime_bucket'] == runtime.lower()]

    if data.empty:
        return None

    data = data.copy()
    scaler = MinMaxScaler()
    data['score'] = scaler.fit_transform(data[['weighted_rating']]) * 0.50

    if popularity == 'high':
        data['score'] += data['popularity_norm'] * 0.30
    elif popularity == 'low':
        data['score'] += (1 - data['popularity_norm']) * 0.30
    else:
        data['score'] += data['popularity_norm'] * 0.10

    if mood_keywords:
        def kw_score(row):
            text = str(row.get('overview', '')).lower()
            hits = sum(1 for kw in mood_keywords if kw.lower() in text)
            return hits / len(mood_keywords)
        data['score'] += data.apply(kw_score, axis=1) * 0.20

    best = data.nlargest(1, 'score').iloc[0]

    return {
        'title':    best['title'],
        'year':     int(best['release_year']),
        'rating':   round(float(best['vote_average']), 1),
        'language': best['original_language'].upper(),
        'runtime':  int(best['runtime']),
        'genres':   ', '.join(best['genres_list']),
        'overview': str(best['overview'])[:300]
    }
