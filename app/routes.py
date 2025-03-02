from flask import Blueprint, request, jsonify, render_template,session
from app.services.notion_service import test_notion_connection
from app.services.youtube_service import get_transcript
from app.services.openai_service import summarize_text
from app.services.notion_service import create_notion_page

main_routes = Blueprint('main', __name__)

@main_routes.route('/', methods=['GET'])
def connect():
    return render_template('connect_notion.html')

@main_routes.route('/main', methods=['GET'])
def index():
    return render_template('index.html')

@main_routes.route('/connect-notion', methods=['POST'])
def connect_notion():
    data = request.json
    notion_api_key = data.get('notion_api_key')
    notion_database_id = data.get('notion_database_id')

    if not notion_api_key or not notion_database_id:
        return jsonify({"error": "Missing Notion API key or Database ID"}), 400

    try:
        # Test the Notion connection
        test_notion_connection(notion_api_key, notion_database_id)

        # Store the API key and Database ID in the session
        session['notion_api_key'] = notion_api_key
        session['notion_database_id'] = notion_database_id

        return jsonify({"message": "Notion connected successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@main_routes.route('/summarize', methods=['POST'])
def summarize():
    print(session['notion_api_key'])
    print(session['notion_database_id'])
        
    data = request.json
    video_url = data.get('video_url')
    notion_api_key = session['notion_api_key']
    notion_database_id = session['notion_database_id']

    if not video_url or not notion_database_id:
        return jsonify({"error": "Missing video URL or Notion database ID"}), 400

    try:
        # Extract video ID from URL
        video_id = video_url.split('v=')[1]

        # Get transcript
        transcriptDic = get_transcript(video_id)

        transcript = transcriptDic.get("transcript")
        # Summarize transcript
        summary = summarize_text(transcript)
        # Send summary to Notion
        create_notion_page(notion_api_key, notion_database_id, "YouTube Summary", summary)

        return jsonify({"message": "Summary sent to Notion successfully!"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500