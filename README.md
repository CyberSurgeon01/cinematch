

CineMatch - Intelligent Movie Recommendation System

CineMatch is a content-based movie recommendation system designed to
deliver a highly relevant film suggestion from a large-scale dataset of
over 900,000 titles. The system analyzes user preferences across seven
structured parameters and applies a multi-criteria scoring algorithm to
identify the single best matching movie.

The goal of CineMatch is to reduce decision fatigue by enabling users to
receive a tailored recommendation in seconds rather than spending long
periods browsing through streaming platforms.

🌐 Live on : https://cinematch-production-10ae.up.railway.app

⸻

Overview

Selecting a movie can often take longer than watching one. CineMatch
addresses this problem by combining content-based filtering, feature
engineering, and weighted scoring techniques to deliver an intelligent
recommendation.

The system collects seven user inputs, processes them through a
two-stage filtering and ranking pipeline, and returns the most relevant
movie based on similarity and popularity signals.

The project demonstrates the complete machine learning system
development workflow, including:
	•	Large-scale dataset processing
	•	Data cleaning and feature engineering
	•	Recommendation algorithm design
	•	Backend API development
	•	Frontend interface design
	•	Cloud deployment and version control

⸻

Features
	•	Genre filtering across 12 categories
	•	Natural language mood and keyword matching
	•	Release year range selection
	•	Minimum rating threshold using an IMDb-style Bayesian weighted rating
	•	Popularity preference selection (mainstream, balanced, hidden gems)
	•	Multi-language filtering including English, Bengali, Korean, Hindi,
French, Japanese, Spanish, and German
	•	Runtime filtering across four duration ranges
	•	Modern glassmorphism-based responsive UI

⸻

Technology Stack

Layer	Technology
Programming Language	Python 3
Web Framework	Flask
Data Processing	Pandas, NumPy
Machine Learning Utilities	Scikit-learn
Dataset	TMDB Movies Dataset (~930K titles)
Frontend	HTML5, CSS3
Deployment	Render.com
Version Control	Git & GitHub


⸻

Recommendation Algorithm

CineMatch uses a two-stage recommendation pipeline to ensure both
accuracy and computational efficiency.

Stage 1 — Hard Filtering

The system first eliminates movies that do not meet the user’s
non-negotiable criteria:
	•	Genre
	•	Language
	•	Release year range
	•	Minimum rating threshold
	•	Runtime category

This step significantly reduces the candidate search space.

Stage 2 — Weighted Scoring

Remaining candidates are ranked using a composite score derived from
three signals:

Score = Weighted Rating   × 0.50
      + Popularity Score  × 0.30
      + Keyword Match     × 0.20

The Weighted Rating follows the Bayesian formula used by IMDb,
balancing a movie’s average rating with its vote count. This prevents
low-vote movies with artificially high ratings from ranking above
well-established films.

⸻

Project Structure

cinematch/
│
├── app.py
│   Flask application and route handling
│
├── recommender.py
│   Core recommendation and scoring logic
│
├── movies_clean.csv
│   Preprocessed TMDB dataset
│
├── requirements.txt
│   Python dependencies
│
├── render.yaml
│   Render deployment configuration
│
└── templates/
    └── index.html
        Frontend user interface


⸻

Running the Project Locally

Prerequisites: Python 3.8+

# Clone the repository
git clone https://github.com/CyberSurgeon01/cinematch.git

# Navigate to the project directory
cd cinematch

# Install dependencies
pip install -r requirements.txt

# Start the Flask development server
python app.py

The application will be accessible at:

http://127.0.0.1:5000


⸻

Dataset

CineMatch uses the TMDB Movies Dataset available on Kaggle. The
dataset contains approximately 930,000 movies and TV titles along
with extensive metadata including:
	•	Genre
	•	Language
	•	Release date
	•	Popularity score
	•	Vote average
	•	Vote count
	•	Runtime
	•	Movie overview

Dataset Source:
https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies

⸻

Deployment

The application is deployed on Render.com using Gunicorn as the
WSGI server.

Each push to the main branch automatically triggers a redeployment
pipeline.

Note: Render’s free tier spins down after 50 seconds of inactivity.
The first request after inactivity may take 30–60 seconds to respond
while the server instance restarts.

⸻

Author

CyberSurgeon01
GitHub: https://github.com/CyberSurgeon01

⸻

License

This project is released under the MIT License, allowing free use,
modification, and distribution.

