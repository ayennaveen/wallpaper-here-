import React, { useState, useEffect } from 'react';
import './index.css'; 

function App() {
  const [wallpapers, setWallpapers] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  
  // 1. State to track if dark mode is active
  const [isDarkMode, setIsDarkMode] = useState(false); 

  // Fetch wallpapers from the API
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    let url = '/api/?';
    
    if (params.has('type')) {
      url += 'type=' + params.get('type');
    }
    if (params.has('device')) {
      url += (url.endsWith('?') ? '' : '&') + 'device=' + params.get('device');
    }
    if (params.has('search')) {
      url += (url.endsWith('?') ? '' : '&') + 'search=' + params.get('search');
    }

    if (url.endsWith('?')) {
      url = '/api/';
    }

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        setWallpapers(data.wallpapers);
      })
      .catch((error) => console.error('Error fetching wallpapers:', error));
  }, [window.location.search]);

  // 2. Run this once when the page loads to check browser memory
  useEffect(() => {
    const savedTheme = localStorage.getItem('theme');
    const body = document.body;
    body.style.transition = '0.5s';
    
    if (savedTheme === 'dark') {
      setIsDarkMode(true);
      body.style.backgroundColor = '#363434';
      body.style.color = '#fff';
    } else {
      setIsDarkMode(false);
      body.style.backgroundColor = '#f4f4f4'; 
      body.style.color = '#111';
    }
  }, []); // The empty array [] means this only runs on page load

  // 3. Handle toggling the switch
  const handleThemeChange = (event) => {
    const isChecked = event.target.checked;
    const body = document.body;
    
    setIsDarkMode(isChecked); 
    body.style.transition = '0.5s';

    if (isChecked) {
        // NIGHT MODE
        body.style.backgroundColor = '#363434';
        body.style.color = '#fff';
        localStorage.setItem('theme', 'dark'); 
    } else {
        // DAY MODE
        body.style.backgroundColor = '#f4f4f4';
        body.style.color = '#111';
        localStorage.setItem('theme', 'light'); 
    }
  };

  const handleSearch = (e) => {
    e.preventDefault();
    console.log("Searching for:", searchQuery);
  };

  return (
    <>
      <div className="header">
        <nav>
          <h1>WALLPAPER HERE</h1>
          <ul>
            <a href="/"><li>All</li></a>
            <a href="/?type=anime"><li>Anime</li></a>
            <a href="/?type=nature"><li>Nature</li></a>
            <a href="/?type=games"><li>Games</li></a>
            <a href="/?type=mountain"><li>Mountain</li></a>

            <div className="theme-switch-container">
              <label className="theme-slider" htmlFor="checkbox">
                <input 
                  onChange={handleThemeChange} 
                  checked={isDarkMode} 
                  type="checkbox" 
                  id="checkbox" 
                  className="checkbox" 
                />
                <div className="round slider"></div>
              </label>
            </div>
          </ul>
        </nav>
      </div>

      <div className="search-container">
        <form onSubmit={handleSearch}>
          <input 
            type="text" 
            placeholder="Search..." 
            name="search"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          <button type="submit">Search</button>
        </form>
      </div>

      <div className="device-filter">
        <a href="/?device=desktop" className="device-btn">🖥 Desktop</a>
        <a href="/?device=mobile" className="device-btn">📱 Mobile</a>
      </div>

      <div className="wallpaper-container">
        {wallpapers.map((wallpaper, index) => (
          <div 
            key={index} 
            className={`card ${wallpaper.device === 'desktop' ? 'desktop' : 'mobile'}`}
          >
            <img src={wallpaper.img_url} alt={wallpaper.title} />

            <a href={wallpaper.img_url} download className="download-btn">
              ⬇
            </a>
          </div>
        ))}
      </div>
    </>
  );
}

export default App;