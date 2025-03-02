from youtube_transcript_api import YouTubeTranscriptApi
from config import Config

def get_transcript(video_id):
    proxy = {
        "https": f"https://{Config.PROXY_USERNAME}:{Config.PROXY_PASSWORD}@gate.smartproxy.com:10001"
        }

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, proxies=proxy)
        transcript_text = " ".join([t['text'] for t in transcript])
        return {"transcript": transcript_text, "videoId": video_id}
    except Exception as e:
        raise Exception(f"Failed to fetch transcript: {str(e)}")