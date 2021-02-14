import React from 'react';
import Main from './components/Main.jsx';
import logo from './logo.jpg'
import './App.css';

function App() {
  return (
    <div className="App">
        <Main image={logo}/>
    </div>
  );
}

export default App;
