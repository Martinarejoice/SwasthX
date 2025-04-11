# SwasthX - Health Companion

A comprehensive health companion application that provides medicine verification, health tips, and AI-powered health assistance.

## Features

- Medicine Verification: Verify the authenticity of medicines using AI
- Daily Health Tips: Get personalized health tips with emojis
- AI Health Assistant: Get answers to your health-related questions
- Multi-language Support: Voice responses in English, Hindi, and Telugu
- Interactive UI: Engaging interface with sound effects and animations

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/swasthx.git
cd swasthx
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with the following variables:
```
FLASK_APP=app.py
FLASK_ENV=development
SESSION_SECRET=your-secret-key-here
DATABASE_URL=sqlite:///swasthx.db
# OPENAI_API_KEY=your-openai-api-key
# GOOGLE_API_KEY=your-google-api-key
```

5. Initialize the database:
```bash
flask db upgrade
```

6. Run the application:
```bash
flask run
```

## Project Structure

```
swasthx/
├── app.py              # Main application file
├── config.py           # Configuration settings
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
├── .gitignore         # Git ignore file
├── static/            # Static files
│   ├── css/          # CSS stylesheets
│   ├── js/           # JavaScript files
│   └── sounds/       # Sound effects
├── templates/         # HTML templates
├── utils/            # Utility modules
└── migrations/       # Database migrations
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 