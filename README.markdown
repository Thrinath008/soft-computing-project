# 🚀 Student Recommendation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python) ![React](https://img.shields.io/badge/React-18-blue?style=flat-square&logo=react) ![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?style=flat-square&logo=fastapi) ![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

Welcome to the **Student Recommendation System**, a cutting-edge platform that uses **machine learning** to match students based on their skills, goals, and interests. Powered by **FastAPI** and **React**, this system delivers a futuristic search experience with a sleek UI and smart recommendations. 🌌

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup Instructions](#-setup-instructions)
- [API Endpoints](#-api-endpoints)
- [Data Format](#-data-format)
- [How It Works](#-how-it-works)
- [Screenshots](#-screenshots)
- [Future Improvements](#-future-improvements)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 Overview
This project is a **Student Recommendation System** designed to connect students with similar technical skills, career aspirations, and project interests. Using **sentence embeddings** from the `all-mpnet-base-v2` model, it matches profiles based on a search query and displays results with a **match percentage**. The backend is built with **FastAPI** for speed, and the frontend uses **React (Vite.js)** for a smooth, futuristic UI. 🎮

---

## ✨ Features
- 🔍 **Smart Search**: Find students by typing keywords (e.g., "AI developer with Python skills").
- 📊 **Match Percentage**: Shows how closely each student matches the query.
- 👤 **Rich Profiles**: Displays name, skills, domains, dream companies, bio, and personality type.
- 📱 **Responsive Design**: Looks great on desktop and mobile.
- ⚡ **Blazing Fast**: Optimized backend with FastAPI and efficient embeddings.
- 🤖 **Advanced AI**: Uses `all-mpnet-base-v2` for high-accuracy recommendations.

---

## 🛠 Tech Stack

### Backend
- 🐍 **Python 3.8+**: Core language for the backend.
- ⚡ **FastAPI**: High-performance API framework.
- 🤖 **Sentence-Transformers**: Generates text embeddings.
- 📈 **Scikit-learn**: Computes cosine similarity.
- 🗄 **Pandas**: Manages user data from CSV.
- 🌐 **Uvicorn**: ASGI server for FastAPI.

### Frontend
- ⚛ **React 18 (Vite.js)**: Fast and modern UI framework.
- 📡 **Axios**: Handles API requests.
- 🎨 **CSS**: Custom styles for a futuristic look.

---

## 📂 Project Structure
```
soft-computer-final-project/
├── backend/
│   ├── main.py              💻 FastAPI application
│   ├── user_data.csv       📊 Student profile data
│   └── requirements.txt    📜 Backend dependencies
├── frontend/
│   ├── src/
│   │   ├── App.jsx         🖼 Main React component
│   │   ├── App.css         🎨 Frontend styles
│   └── package.json        📜 Frontend dependencies
├── .gitignore              🚫 Ignored files (e.g., node_modules, venv)
└── README.md               📝 Project documentation
```

---

## 🖥 Setup Instructions

### Prerequisites
- 🐍 **Python 3.8+**
- 🌐 **Node.js 18+**
- 📦 **Git**

### Backend Setup
1. Navigate to the backend folder:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   🖥 Backend runs at `http://127.0.0.1:8000`.

### Frontend Setup
1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the Vite dev server:
   ```bash
   npm run dev
   ```
   🌐 Frontend runs at `http://localhost:5173`.

---

## 🌐 API Endpoints

### `POST /search/`
- **Description**: Returns top N students matching the search query.
- **Request Body**:
  ```json
  {
    "query": "Python developer with AI experience",
    "top_n": 5
  }
  ```
- **Response**:
  ```json
  {
    "recommended_users": [
      {
        "name": "Tanya Sharma",
        "known_skills": "AWS, Java, Pandas",
        "preferred_domains": "Edge Computing, Cybersecurity",
        "dream_companies": "Microsoft, Amazon",
        "bio": "I love Robotics and Azure",
        "personality_type": "ENTP",
        "match_percentage": 87.53
      },
      ...
    ]
  }
  ```

### `GET /`
- **Description**: Confirms the API is running.
- **Response**:
  ```json
  {
    "message": "Search User API is running 🚀"
  }
  ```

---

## 📊 Data Format
Student profiles are stored in `user_data.csv`. Each row includes:
- `user_id`: Unique ID.
- `name`: Student’s name.
- `known_skills`: Technical skills.
- `preferred_domains`: Interest areas (e.g., AI, Cybersecurity).
- `dream_companies`: Aspired companies.
- `bio`: Short description.
- `personality_type`: MBTI type (e.g., ENTP).

**Example Row**:
```csv
user_id,name,email,known_skills,preferred_domains,dream_companies,bio,personality_type
u10086,Tanya,tanya180@example.com,"['AWS', 'Java', 'Pandas']","['Edge Computing', 'Cybersecurity']","['Microsoft', 'Amazon']","I love Robotics and Azure","ENTP"
```

---

## ⚙ How It Works
1. **Data Loading**: Backend reads `user_data.csv` and combines profile fields into text strings.
2. **Embedding Generation**: `all-mpnet-base-v2` converts profiles and queries into vectors.
3. **Matching**: Cosine similarity ranks students by relevance to the query.
4. **Frontend**: React sends queries via Axios and displays results as styled user cards with match percentages.

---

## 📸 Screenshots
*(Add your app’s UI screenshot here for extra flair!)*  
To add a screenshot:
1. Take a screenshot of your app.
2. Upload it to the repo (e.g., `screenshots/app.png`).
3. Add this Markdown:  
   ```markdown
   ![App Screenshot](screenshots/app.png)
   ```

---

## 🔮 Future Improvements
- 🔒 **Authentication**: Add login for profile management.
- 🎛 **Filters**: Filter by skills, domains, or personality.
- 🌙 **Dark Mode**: Toggle between light and dark themes.
- ⏳ **Loading Animations**: Add spinners for a slick UX.
- 📣 **Feedback**: Let users rate recommendations to refine the model.

---

## 📜 License
This project is licensed under the **[MIT License](LICENSE)**. Free to use, modify, and share! 🚀

---

## 📬 Contact
Questions? Issues? Open a ticket in the [GitHub Issues](https://github.com/yourusername/student-recommendation-app/issues) section.

Built with 💻 and ☕ for a futuristic student experience!