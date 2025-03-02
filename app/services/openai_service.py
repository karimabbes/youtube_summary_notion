from openai import OpenAI
from config import Config


def summarize_text(text):
    try:
        client = OpenAI(api_key=Config.DEEP_SEEK_API_KEY, base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": f"Extract the main points from the following YouTube video transcript and summarize them in clear, concise bullet points. Focus on key ideas, statistics, arguments, and actionable advice presented in the video. Organize the information logically to ensure the summary is easy to follow and captures the essence of the content: {text}"},
            ],
            stream=False
        )

        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Failed to summarize text: {str(e)}")