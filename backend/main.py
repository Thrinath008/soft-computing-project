from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import os
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Initialize app
app = FastAPI()

# CORS middleware (important for frontend-backend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data
file_path = os.path.join(os.path.dirname(__file__), "user_data.csv")
df = pd.read_csv(file_path)

# Combine important fields
def combine_fields(row):
    fields = [
        row['known_skills'],
        row['learning_goals'],
        row['preferred_domains'],
        row['tech_stack_familiarity'],
        row['dream_companies'],
        row['bio']
    ]
    return ' '.join([str(f) for f in fields if pd.notnull(f)])

df['combined_text'] = df.apply(combine_fields, axis=1)

# Load model
model = SentenceTransformer('thenlper/gte-large')
embeddings = model.encode(df['combined_text'].tolist())

# Request Body model
class SearchRequest(BaseModel):
    query: str
    top_n: int = 5

@app.post("/search/")
def search_users(request: SearchRequest):
    query_embedding = model.encode([request.query])
    sim_scores = cosine_similarity(query_embedding, embeddings)[0]

    top_indices = sim_scores.argsort()[::-1][:request.top_n]

    results = []
    for idx in top_indices:
        user = df.iloc[idx]
        results.append({
            "name": user["name"],
            "known_skills": user["known_skills"],
            "preferred_domains": user["preferred_domains"],
            "dream_companies": user["dream_companies"],
            "bio": user["bio"],
            "personality_type": user["personality_type"],
            "match_percentage": round(sim_scores[idx] * 100, 2)  # Here we add match %
        })

    return {"recommended_users": results}

@app.get("/")
def root():
    return {"message": "Search User API is running 🚀"}
