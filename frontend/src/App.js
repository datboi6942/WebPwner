import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Analyze from './components/Analyze';
import Suggest from './components/Suggest';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/analyze" component={Analyze} />
          <Route path="/suggest" component={Suggest} />
          <Route path="/" component={Home} />
        </Switch>
      </div>
    </Router>
  );
}

function Home() {
  return <h1>Welcome to the Hacker Interface</h1>;
}

export default App;
