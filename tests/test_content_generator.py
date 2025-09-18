import pytest
from src.content_generator import ContentGenerator
from src.config import Config

def test_content_generator_initialization():
    # This will fail if no API key is set
    if Config.OPENAI_API_KEY:
        generator = ContentGenerator()
        assert generator.api_key == Config.OPENAI_API_KEY

def test_prompt_building():
    generator = ContentGenerator("test-key")
    prompt = generator._build_campaign_prompt(
        "Test Campaign", "Test Audience", "Test Message", "professional"
    )
    assert "Test Campaign" in prompt
    assert "SATA CommHealth" in prompt