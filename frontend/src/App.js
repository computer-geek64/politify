import React from 'react';
import MainForm from './components/MainForm.jsx';
import Scale from './components/Scale.jsx';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Scale score={50}/>
      </header>
    </div>
  );
}

export default App;
