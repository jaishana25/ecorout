// src/Home.js
import React from 'react';
import './Home.css';

function Home() {
  return (
    <div className="Home">
      <div className="Home-rectangle">
      <input type="text" className="Home-input" placeholder="Input 1" />
      <input type="text" className="Home-input" placeholder="Input 2" />
      <div className='plan'>
        Plan

      </div>
      </div>
    </div>
  );
}

export default Home;
