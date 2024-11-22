# Wallpaper Manager

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![OS](https://img.shields.io/badge/OS-Windows%20|%20Linux%20|%20MacOS-orange.svg)]()

An intelligent wallpaper management system that automatically changes your desktop background based on current weather conditions and time of day. The application uses real-time weather data and local time to select appropriate wallpapers from your collection.

## Features

- **Weather-based Wallpapers**: Automatically changes wallpaper based on current weather conditions
- **Time-sensitive**: Different wallpapers for different parts of the day
- **Cross-platform**: Supports Windows 10, Ubuntu 20.04, and MacOS (untested)
- **Customizable**: Easy to add new wallpapers and categories
- **Location-aware**: Uses geolocation to fetch accurate weather data

## Installation

1. Clone the repository:
```bash
git clone https://github.com/amirrezaes/Wallpaper-Manager.git
cd Wallpaper-Manager
```

2. Install required dependencies:
```bash
pip install geocoder
```

## Configuration

### Image Mapping
Add your wallpapers to the `images` folder and map them in `image_map.json`:

```json
{
    "weather": {
        "sunny": ["sunny1.jpg", "sunny2.jpg"],
        "rainy": ["rain1.jpg", "rain2.jpg"],
        "snowy": ["snow1.jpg", "snow2.jpg"]
    },
    "time": {
        "morning": ["morning1.jpg", "morning2.jpg"],
        "evening": ["evening1.jpg", "evening2.jpg"],
        "night": ["night1.jpg", "night2.jpg"]
    }
}
```

### System Configuration
Adjust settings in `config.json` according to your preferences.

## Usage

Run the main script:
```bash
python wallpaper_manager.py
```

## Project Structure

```
.
├── images/                 # Wallpaper directory
├── OperationSystems.py     # OS-specific implementations
├── api.py                  # Weather API integration
├── config.json            # Configuration file
├── image_map.json         # Wallpaper mapping
└── wallpaper_manager.py   # Main application
```

## Roadmap

- [x] Background service implementation for automatic updates
- [x] Hybrid mode (combining weather and time conditions)
- [ ] MacOS
- [ ] Code refactoring and optimization
- [ ] GUI interface
- [x] Custom weather-time combinations

## Supported Operating Systems

- ✅ Windows 10
- ✅ Ubuntu 20.04
- ⚠️ MacOS (untested)

