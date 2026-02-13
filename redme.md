# 🗺️ Route Visualization Demo

Interactive route visualization on a map using Google Directions API and React + Leaflet.

## 📸 Preview

Vinnytsia → Dnipro route with 55,000+ points for maximum precision.

## 🎯 Features

- ✅ Route fetching via Google Directions API
- ✅ Detailed visualization (55k+ points) with Canvas rendering for performance
- ✅ Interactive map powered by Leaflet
- ✅ Load routes from JSON files
- ✅ Auto-fit bounds to route
- ✅ Lightweight and fast UI

## 🛠️ Tech Stack

**Backend:**
- Python 3.x
- Google Directions API
- polyline (route decoding)

**Frontend:**
- React
- Leaflet / React-Leaflet
- CartoDB tiles (light map style)

## 🚀 Quick Start

### 1. Fetch Route (Python)
```bash
# Install dependencies
pip install requests polyline

# Run script
python get_coord.py
```

This creates `route.json` with route coordinates.

### 2. Visualize (React)
```bash
# Install dependencies
npm install

# Start dev server
npm run dev
```

Open http://localhost:5173 and upload `route.json` via the interface.

## 📁 Project Structure
```
.
├── get_coord.py          # Google API route fetcher
├── route.json            # Sample route (55k points)
├── src/
│   ├── App.jsx           # Main map component
│   └── main.jsx          # Entry point
├── package.json
└── README.md
```

## ⚙️ Configuration

### Google API Key

Set your API key in `get_coord.py`:
```python
GOOGLE_API_KEY = "your_key_here"
```

Get your key at [Google Cloud Console](https://console.cloud.google.com/).

### Route Setup

Change points A and B in `get_coord.py`:
```python
origin = "48.516707,29.211951"      # Point A (lat,lng)
destination = "48.195792,35.806096"  # Point B (lat,lng)
```

## 🎨 Customization

### Change Map Style

In `App.jsx`, replace tile provider:
```jsx
// Light style (current)
url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"

// Dark style
url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"

// Basic OSM
url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
```

### Change Route Color
```jsx
<Polyline 
  positions={route} 
  color="#FF6B00"  // Change color here
  weight={4}
  opacity={0.8}
/>
```

## 📊 Performance

- **Route points:** 55,000+
- **JSON size:** ~528KB
- **Rendering:** Canvas (optimized for large routes)
- **Load time:** <1 second on modern internet

## 🔮 Future Improvements

- [ ] Multiple routes on one map
- [ ] Drag & drop for points A and B
- [ ] Export route to PDF/PNG
- [ ] Compare routes from different providers (Google vs Mapbox vs OSRM)
- [ ] Display distance and duration info

## 📝 License

MIT

## 👨‍💻 Author

Created as a demonstration of maps and routing API integration.

---

**Built with ❤️ using React + Leaflet**