# Flask Notion Integration

This is a demo Flask application that integrates with the Notion API. It allows users to submit a form with their name, email, and mood. The submitted data is then pushed to a Notion database. There is also a page that pulls and displays the data from the Notion database.

## Installation

First, clone the repository:

```bash
  git clone https://github.com/basileMarchand/flask-notion-demo.git
  cd flask-notion-demo
```

Then, install the required Python packages:

```bash
  pip install -r requirements.txt
```

## Usage

To run the application:

```bash
  python app.py
```

Then, open your web browser and navigate to http://localhost:5000.

## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

`NOTION_API_KEY` - Your Notion API key.

`DATABASE_ID` - The ID of your Notion database.

## Deployment

This project is deployed on Vercel. You can find it [here](https://flask-notion-demo.vercel.app/).

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
