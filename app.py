from flask import Flask, render_template, request
from recommender import recommend_movie

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result    = None
    error     = None
    warning   = None
    form_data = {}

    if request.method == 'POST':

        genre      = request.form.get('genre') or None
        mood       = request.form.get('mood') or None
        mood_kw    = [k.strip() for k in mood.split(',')] if mood else None
        yr         = request.form.get('year_range') or ''
        year_range = None
        if '-' in yr:
            try:
                parts = yr.split('-')
                year_range = (int(parts[0]), int(parts[1]))
            except:
                year_range = None
        min_rating = float(request.form.get('min_rating') or 0)
        popularity = request.form.get('popularity') or 'any'
        language   = request.form.get('language') or None
        runtime    = request.form.get('runtime') or None

        form_data = {
            'genre':      request.form.get('genre', ''),
            'language':   request.form.get('language', 'any'),
            'mood':       request.form.get('mood', ''),
            'year_range': request.form.get('year_range', ''),
            'min_rating': request.form.get('min_rating', ''),
            'popularity': request.form.get('popularity', 'any'),
            'runtime':    request.form.get('runtime', 'any'),
        }

        # Count how many meaningful inputs were given
        filled = sum([
            1 if genre else 0,
            1 if mood else 0,
            1 if year_range else 0,
            1 if min_rating > 0 else 0,
            1 if popularity != 'any' else 0,
            1 if language and language != 'any' else 0,
            1 if runtime and runtime != 'any' else 0,
        ])

        if filled < 2:
            warning = "Please fill in at least 2 fields so we can find your perfect match!"
        else:
            result = recommend_movie(
                genre         = genre,
                mood_keywords = mood_kw,
                year_range    = year_range,
                min_rating    = min_rating,
                popularity    = popularity,
                language      = language,
                runtime       = runtime
            )
            if result is None:
                error = "No movie found. Try relaxing your filters."

    return render_template('index.html',
                           result=result,
                           error=error,
                           warning=warning,
                           form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)