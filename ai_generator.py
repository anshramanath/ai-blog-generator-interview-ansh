import cohere
import os
from dotenv import load_dotenv

load_dotenv()
client = cohere.Client(os.getenv("COHERE_API_KEY"))

def generate_post(keyword, seo_data):
    prompt = f"""
        Write a long-form blog post in Markdown format targeting the keyword "{keyword}".
        - Start with a compelling title and introduction
        - Include at least 2 body sections and a conclusion
        - Incorporate SEO stats: search volume ({seo_data['search_volume']}), keyword difficulty ({seo_data['keyword_difficulty']}), and CPC (${seo_data['avg_cpc']})
        - Throughout the post, mention actual-sounding product recommendations relevant to the topic
        - For each recommendation, create a markdown affiliate link with a fake but realistic-looking URL
        Example: [Sony WF-1000XM5](https://www.bestbuy.com/sony-wf1000xm5-aff)
        - Do not use placeholders like {{AFF_LINK}} or example.com — generate the links yourself
        - Do not explain your output — just return the markdown post
    """

    response = client.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=2000,
        temperature=0.7
    )

    return response.generations[0].text