from notion_client import Client

def test_notion_connection(notion_api_key, database_id):
    try:
        notion = Client(auth=notion_api_key)
        # Test by fetching the database
        notion.databases.retrieve(database_id)
        return True
    except Exception as e:
        raise Exception(f"Failed to connect to Notion: {str(e)}")
    

def create_notion_page(notion_api_key, database_id, title, content):
    try:
        notion = Client(auth=notion_api_key)
        notion.pages.create(
            parent={"database_id": database_id},
            properties={
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": title
                            }
                        }
                    ]
                }
            },
            children=[
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": content
                                }
                            }
                        ]
                    }
                }
            ]
        )
    except Exception as e:
        raise Exception(f"Failed to create Notion page: {str(e)}")