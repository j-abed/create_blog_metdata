import uuid
import json
from datetime import datetime

title = input('Enter the title: ')
excerpt = input('Enter the excerpt: ')
while True:
    date_input = input(
        "Enter the date (e.g., Month DD YYYY): "
    )
    if not date_input.strip():
        print("Date cannot be empty. Please enter a valid date.")
        continue
    formats = [
        "%b %d %Y",      # MMM DD YYYY
        "%B %d %Y",      # MONTH DD YYYY
        "%B %d, %Y",     # MONTH DD, YYYY
        "%b %d, %Y",     # MMM DD, YYYY
        "%d %B %Y",      # DD MONTH YYYY
        "%m/%d/%y",      # MM/DD/YY
        "%m/%d/%Y",      # MM/DD/YYYY
    ]
    for fmt in formats:
        try:
            date_obj = datetime.strptime(date_input, fmt)
            date = date_obj.strftime("%b %d, %Y")
            break
        except ValueError:
            continue
    else:
        print(
            "Invalid date format. Please use one of: "
            "'Jun 10 2025', 'June 10 2025', 'June 10, 2025', '10 June 2025', '06/10/25', or '06/10/2025'."
        )
        continue
    break
minutes = input('Enter the read time in minutes: ')
read_time = f"{minutes} min read"
image = input('Enter the image path: ')
author = input('Enter the author: ')
category = input('Enter the category: ')
slug = input('Enter the slug: ')

result = {
    "id": str(uuid.uuid4()),
    "title": title,
    "excerpt": excerpt,
    "date": date,
    "readTime": read_time,
    "image": image,
    "author": author,
    "category": category,
    "slug": slug
}

print(json.dumps(result, indent=2))
