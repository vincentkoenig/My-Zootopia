# My Zootopia 🦁

A Python tool that fetches live animal data from the **API-Ninjas Animals API** and generates a styled HTML webpage — one card per animal, with diet, location, and type. Built to practice API integration and dynamic HTML generation.

## How It Works

1. You enter an animal name in the terminal
2. The app fetches data from the API-Ninjas Animals API
3. Each animal is serialized into an HTML card
4. A template HTML file is populated with the generated cards
5. The final page is saved as `animals.html`

## Features

- 🌐 **Live API data** — fetches real animal information via API-Ninjas
- 🃏 **Card-based HTML output** — each animal gets a card with name, diet, location, and type
- 📄 **Template-based generation** — clean separation between structure (HTML template) and data (Python)
- ⚠️ **Graceful fallback** — displays a friendly message if the animal doesn't exist in the API
- 🔑 **Secure API key** — loaded from a `.env` file, never hardcoded

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)

- **Python 3.x**
- **requests** — HTTP calls to the API-Ninjas Animals endpoint
- **python-dotenv** — secure API key management
- **HTML/CSS** — styled card-based output template

## Project Structure

```
My-Zootopia/
├── animals_web_generator.py   # Main app — fetches data & generates HTML
├── data_fetcher.py            # API-Ninjas API integration
├── animals_template.html      # HTML template with placeholder
├── animals.html               # Generated output (created on run)
├── animals_data.json          # Sample animal data
├── requirements.txt
└── .gitignore
```

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/vincentkoenig/My-Zootopia.git
cd My-Zootopia
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Create a `.env` file with your API key**
```
API_KEY=your_api_key_here
```
> Get a free key at [api-ninjas.com](https://api-ninjas.com/)

**4. Run the app**
```bash
python animals_web_generator.py
```

**5. Open the result**
```
Open animals.html in your browser
```

## Example Output

```
Enter a name of an animal: Fox
Website was successfully generated to the file animals.html.
```

The generated page displays cards like:

```
🦊 Red Fox
Diet: Omnivore
Location: Asia
Type: Mammal
```

## What I Learned

- Integrating a third-party REST API with secure key management via `python-dotenv`
- Separating data fetching, HTML serialization, and file generation into distinct functions
- Using template-based HTML generation with string placeholder replacement
- Handling missing or incomplete API data gracefully with `.get()` defaults
