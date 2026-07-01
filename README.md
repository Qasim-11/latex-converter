# LaTeX Converter

A small clipboard utility that reads an image from the clipboard, sends it to Gemini for text and math transcription, and copies the result back to the clipboard.

## Requirements

- Python 3.10+
- A `GOOGLE_API_KEY` set in your `.env` file
- Install dependencies with `pip install -r requirements.txt`

## Run

```bash
python app.py
```

## Usage

1. Copy an image to your clipboard. (on windows, it's automatically done with any screenshot)
2. Press `Alt+C` to convert it.
3. The output is copied as text to your clipboard.
4. Press `Esc` to quit.

## Notes

- `list_available_models.py` can be used to inspect available Gemini models.
- If no image is found in the clipboard, the app shows a small popup and exits the conversion attempt.
