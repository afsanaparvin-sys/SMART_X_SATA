# SATA Content Generator

AI-powered content generation tool for SATA CommHealth healthcare campaigns.

## Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Set up environment variables in `.env` file
6. Run tests: `pytest`

## Usage
```python
from src.content_generator import ContentGenerator

generator = ContentGenerator()
result = generator.generate_campaign_content(
    campaign_type="Diabetes Awareness",
    target_audience="Seniors 65+",
    key_message="Early detection saves lives"
)