import React, { useState } from 'react';
import axios from 'axios';

function Suggest() {
  const [suggestionType, setSuggestionType] = useState('');
  const [suggestionContent, setSuggestionContent] = useState('');
  const [results, setResults] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/suggest', { suggestionType, suggestionContent });
      setResults(response.data);
    } catch (error) {
      console.error('Error suggesting:', error);
    }
  };

  return (
    <div>
      <h2>Suggest</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" value={suggestionType} onChange={(e) => setSuggestionType(e.target.value)} placeholder="Suggestion Type" required />
        <input type="text" value={suggestionContent} onChange={(e) => setSuggestionContent(e.target.value)} placeholder="Suggestion Content" required />
        <button type="submit">Suggest</button>
      </form>
      {results && <pre>{JSON.stringify(results, null, 2)}</pre>}
    </div>
  );
}

export default Suggest;
