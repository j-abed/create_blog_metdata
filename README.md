# Blog Metadata Creator

A simple Python tool for generating blog post metadata in JSON format. Supports both a graphical user interface (GUI) and a command-line interface (CLI).

## Features
- Enter blog metadata via a user-friendly Tkinter form (GUI)
- Optional command-line mode for quick entry
- Date format validation with clear error messages
- Sensible default values for all fields
- Save generated metadata to a JSON file

## Requirements
- Python 3.x
- Tkinter (included with standard Python installations)

## Usage

### GUI Mode (default)
Run the script normally to launch the graphical interface:

```pwsh
python create_blog_metadata.py
```

Fill in the fields and click "Create Metadata". The generated JSON will be displayed and you can choose to save it to a file.

### Command-Line Mode
Run with the `--cli` flag to use the command-line interface:

```pwsh
python create_blog_metadata.py --cli
```

You will be prompted for each field. Press Enter to accept the default value shown in brackets. The generated JSON will be printed, and you can choose to save it to a file.

## Date Format
Accepted date formats include:
- Jun 10 2025
- June 10 2025
- June 10, 2025
- 10 June 2025
- 06/10/25
- 06/10/2025

If an invalid date is entered, a clear error message will be shown.

## Output
The metadata is output as a JSON object with the following fields:
- id
- title
- excerpt
- date
- readTime
- image
- author
- category
- slug

## License
MIT
