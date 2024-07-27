import React, { useState } from 'react';
import axios from 'axios';

function Analyze() {
  const [url, setUrl] = useState('');
  const [method, setMethod] = useState('GET');
  const [vulnerabilityType, setVulnerabilityType] = useState('');
  const [results, setResults] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/analyze', { url, method, vulnerabilityType });
      setResults(response.data.results);
    } catch (error) {
      console.error('Error analyzing:', error);
    }
  };

  return (
    <div>
      <h2>Analyze</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" value={url} onChange={(e) => setUrl(e.target.value)} placeholder="URL" required />
        <select value={method} onChange={(e) => setMethod(e.target.value)}>
          <option value="GET">GET</option>
          <option value="POST">POST</option>
        </select>
        <input type="text" value={vulnerabilityType} onChange={(e) => setVulnerabilityType(e.target.value)} placeholder="Vulnerability Type" required />
        <button type="submit">Analyze</button>
      </form>
      {results && <pre>{JSON.stringify(results, null, 2)}</pre>}
    </div>
  );
}

export default Analyze;
