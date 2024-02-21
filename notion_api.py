import requests


import dotenv
import os
dotenv.load_dotenv()

NOTION_API_KEY = os.getenv('NOTION_API_KEY')
DATABASE_ID = os.getenv('DATABASE_ID')

def push_to_notion(nom, prenom, mail, humeur):
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Nom": {
                "title": [
                    {
                        "text": {
                            "content": nom
                        }
                    }
                ]
            },
            "Prenom": {
                "rich_text": [
                    {
                        "text": {
                            "content": prenom
                        }
                    }
                ]
            },
            "Email": {
                "email": mail
            },
            "Humeur": {
                "select": {
                    "name": humeur
                }
            }
        }
    }
    response = requests.post('https://api.notion.com/v1/pages', headers=headers, json=data)
    if response.status_code != 200:
        print("Failed to push on notion database :", response.text)

def pull_from_notion():
    url = f'https://api.notion.com/v1/databases/{DATABASE_ID}/query'
    
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": "2022-06-28"
    }
    
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        resultats = []
        for item in data['results']:
            entry = {
                'Nom': item['properties']['Nom']['title'][0]['text']['content'],
                'Prenom': item['properties']['Prenom']['rich_text'][0]['text']['content'],
                'Email': item['properties']['Email']['email'],
                'Humeur': item['properties']['Humeur']['select']['name']
            }
            resultats.append(entry)
        return resultats
    else:
        print("Fail to pull data from notion :", response.text)
        return []