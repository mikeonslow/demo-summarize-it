# demo-summarize-it

## Requirements:
- Python 3.10.x+
- Open AI API access
- Deepgram API access

## Setup

Make sure you have python 3.11.x installed (https://docs.python.org/3/whatsnew/3.11.html) and pipenv (https://pipenv.pypa.io/en/latest/) installed.

Create an `.env` file in the root of the project with the following variables:

```bash
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
DEEPGRAM_API_KEY=<YOUR_OPENAI_API_KEY>
```

## Running the Project

```bash
pipenv shell
pipenv run python call_aggregator.py "https://res.cloudinary.com/deepgram/video/upload/v1663090406/dg-audio/Upgrading-phone-plan_pmfsfm.m4a"
```