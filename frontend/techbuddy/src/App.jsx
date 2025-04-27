import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const searchUsers = async () => {
    if (!query) return;
    setLoading(true);
    try {
      const response = await axios.post('http://127.0.0.1:8000/search/', {
        query: query,
        top_n: 5,
      });
      setResults(response.data.recommended_users);
    } catch (error) {
      console.error('Error fetching users:', error);
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      <h1>User Search System 🚀</h1>
      <div className="search-box">
        <input
          type="text"
          placeholder="Describe the user you want..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={searchUsers}>Search</button>
      </div>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <div className="results">
          {results.map((user, index) => (
            <div key={index} className="user-card">
              <h2>{user.name}</h2>
              <p><strong>Matched:</strong> {user.match_percentage}%</p>
              <p><strong>Skills:</strong> {user.known_skills}</p>
              <p><strong>Domains:</strong> {user.preferred_domains}</p>
              <p><strong>Dream Companies:</strong> {user.dream_companies}</p>
              <p><strong>Bio:</strong> {user.bio}</p>
              <p><strong>Personality:</strong> {user.personality_type}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
