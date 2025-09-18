import openai
import json
import logging
from typing import Dict, List, Optional
from .config import Config

logging.basicConfig(level=getattr(logging, Config.LOG_LEVEL))
logger = logging.getLogger(__name__)

class ContentGenerator:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or Config.OPENAI_API_KEY
        if not self.api_key:
            raise ValueError("OpenAI API key is required")
        
        self.client = openai.OpenAI(api_key=self.api_key)
        logger.info("ContentGenerator initialized")
    
    def generate_campaign_content(
        self, 
        campaign_type: str, 
        target_audience: str, 
        key_message: str,
        tone: str = None
    ) -> Dict:
        """Generate comprehensive campaign content"""
        
        tone = tone or Config.BRAND_GUIDELINES["tone"]
        
        prompt = self._build_campaign_prompt(
            campaign_type, target_audience, key_message, tone
        )
        
        try:
            response = self.client.chat.completions.create(
                model=Config.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": self._get_system_prompt()},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=Config.MAX_TOKENS,
                temperature=Config.TEMPERATURE
            )
            
            content = response.choices[0].message.content
            logger.info(f"Generated content for campaign: {campaign_type}")
            
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                return {"raw_content": content}
                
        except Exception as e:
            logger.error(f"API call failed: {str(e)}")
            return {"error": f"API call failed: {str(e)}"}
    
    def _get_system_prompt(self) -> str:
        """Get the system prompt for the AI"""
        return f"""You are an expert healthcare marketing specialist creating content for {Config.BRAND_GUIDELINES['organization']} ({Config.BRAND_GUIDELINES['full_name']}).

Mission: {Config.BRAND_GUIDELINES['mission']}
Region: {Config.BRAND_GUIDELINES['target_region']}
Tone: {Config.BRAND_GUIDELINES['tone']}

Always ensure content is culturally appropriate, medically accurate, and maintains the dignity of vulnerable populations."""
    
    def _build_campaign_prompt(self, campaign_type: str, target_audience: str, key_message: str, tone: str) -> str:
        """Build the campaign generation prompt"""
        return f"""
        Create a complete healthcare campaign for {Config.BRAND_GUIDELINES['organization']}.
        
        Campaign Details:
        - Type: {campaign_type}
        - Target Audience: {target_audience}
        - Key Message: {key_message}
        - Tone: {tone}
        
        Generate the following content:
        1. Campaign title (catchy and memorable)
        2. Main tagline
        3. Facebook post (engaging, 150-200 words)
        4. LinkedIn post (professional, 200-250 words)
        5. Instagram caption (casual but informative, 100-150 words with hashtags)
        6. Email subject line
        7. Call-to-action text
        
        Format as valid JSON with clear sections.
        """