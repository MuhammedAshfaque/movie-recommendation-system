# Movie Recommendation System 🎬
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Dataset](https://img.shields.io/badge/dataset-TMDB%205000-orange.svg)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
An interactive, content-based Movie Recommendation System built with Python and Streamlit. The application recommends similar movies based on metadata (genres, keywords, cast, crew, and overview) using Natural Language Processing (NLP) and Cosine Similarity.
🔗 **Live Demo:** [View Live Web App](https://movie-recommending-system-uims.onrender.com/)
---
##  Features
* **Content-Based Recommendations:** Recommends the top 5 most relevant movies similar to the user's search.
* **Interactive UI:** A responsive, clean dashboard developed with Streamlit for seamless movie searching.
* **Dynamic Posters:** Fetches real-time movie posters dynamically using the TMDB API.
* **Smart Search:** Auto-suggest list as you type your favorite movie.
---
##  Tech Stack & Libraries
* **Frontend:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Natural Language Processing:** NLTK (Natural Language Toolkit)
* **Machine Learning & Vectorization:** Scikit-Learn
* **API Calls:** Requests (for TMDB Movie Posters)
---
##  How it Works (Under the Hood)
The recommendation engine follows a content-based filtering approach:
```text
[Raw Dataset (TMDB 5000)]
         │
         ▼
[Data Cleaning & Feature Selection] (Extract genres, keywords, cast, crew, overview)
         │
         ▼
[Preprocessing & Stemming] (Using NLTK's PorterStemmer to normalize words)
         │
         ▼
[Text Vectorization] (Bag of Words using CountVectorizer)
         │
         ▼
[Similarity Matrix] (Compute Cosine Similarity between movies)
         │
         ▼
[Recommender Engine] (Fetch Top 5 closest vectors)
```
1. **Preprocessing:** Merges relevant columns (`genres`, `keywords`, `cast`, `director`, `overview`) into a single string tag for each movie.
2. **Stemming (NLP):** Applies `PorterStemmer` from `NLTK` to reduce words to their root forms (e.g., `"loved"`, `"loving"`, `"loves"` $\rightarrow$ `"love"`).
3. **Vectorization:** Converts the tags into a $5000 \times 5000$ dimensional vector space using Scikit-Learn's `CountVectorizer` (retaining the top 5,000 most frequent words, excluding English stop words).
4. **Cosine Similarity:** Measures the cosine of the angle between two movie vectors to determine their similarity. Movies with a higher similarity score are recommended first.
---
##  Local Installation & Setup
Follow these steps to run the application locally on your machine:
### 1. Clone the Repository
```bash
git clone https://github.com/MuhammedAshfaque/movie-recommendation-system.git
cd movie-recommendation-system
```
### 2. Create and Activate a Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate
# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
Make sure you install all the required Python libraries:
```bash
pip install -r requirements.txt
```
### 4. Run the Streamlit Application
```bash
streamlit run app.py
```
This will open the application in your default web browser at `http://localhost:8501`.
---
## Project Structure
```text
movie-recommendation-system/
│
├── dataset/                     # TMDB 5000 movies & credits csv files
│
├── notebooks/
│   └── movie_recommender.ipynb  # Jupyter notebook containing data processing and model testing
│
├── app.py                       # Main Streamlit application
├── model.pkl                    # Serialized DataFrame containing movie details
├── similarity.pkl               # Serialized Cosine Similarity Matrix
├── requirements.txt             # List of python dependencies
└── README.md                    # Project documentation
```
---
## Deployment
This app is optimized and configured for easy deployment on **Render** or **Streamlit Community Cloud**:
1. Upload your code to GitHub.
2. Link your repository to your hosting service.
3. Set the start command to:
   ```bash
   streamlit run app.py
   ```
---
## License
Distributed under the MIT License. See `LICENSE` for more information.
---
## Author
* **Sk Md Ashfaque**
  * GitHub: [@MuhammedAshfaque](https://github.com/MuhammedAshfaque)
  * LinkedIn: [Sk Md Ashfaque](https://linkedin.com/in/sk-md-ashfaque-715662237/)
