import React, { useState } from 'react';
import { MapContainer, TileLayer, Polyline } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

function App() {
  const [route, setRoute] = useState(null);

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    
    reader.onload = (event) => {
      const coords = JSON.parse(event.target.result);
      setRoute(coords);
    };
    
    reader.readAsText(file);
  };

  const center = [48.35, 32.5]; // Центр между точками

  return (
    <div style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      <div style={{ 
        padding: '20px', 
        background: '#fff', 
        borderBottom: '1px solid #ddd',
        zIndex: 1000 
      }}>
        <input 
          type="file" 
          accept=".json" 
          onChange={handleFileUpload}
          style={{ fontSize: '16px' }}
        />
      </div>
      
      <MapContainer 
        center={center} 
        zoom={7} 
        style={{ height: '100%', width: '100%' }}
      >
<TileLayer
  attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
  url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"
/>
            
        {route && (
          <Polyline 
            positions={route} 
            color="#FF6B00" 
            weight={4}
            opacity={0.8}
          />
        )}
      </MapContainer>
    </div>
  );
}

export default App;