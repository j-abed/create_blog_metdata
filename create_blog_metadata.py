

import uuid
import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import sys

DEFAULTS = {
    "title": "Sample Blog Title",
    "excerpt": "A short summary of the blog post.",
    "date": datetime.now().strftime("%b %d, %Y"),
    "minutes": "5",
    "image": "image.jpg",
    "author": "Author Name",
    "category": "General",
    "slug": "sample-blog-title"
}


def parse_date(date_input):
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
            return date_obj.strftime("%b %d, %Y")
        except ValueError:
            continue
    raise ValueError(
        "Invalid date format. Please use one of: 'Jun 10 2025', 'June 10 2025', 'June 10, 2025', '10 June 2025', '06/10/25', or '06/10/2025'."
    )


def submit():
    title = title_var.get()
    excerpt = excerpt_var.get()
    date_input = date_var.get()
    minutes = minutes_var.get()
    image = image_var.get()
    author = author_var.get()
    category = category_var.get()
    slug = slug_var.get()

    if not title or not excerpt or not date_input or not minutes or not image or not author or not category or not slug:
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        date = parse_date(date_input)
    except ValueError as e:
        # Show error in the UI, not just a popup
        output_text.config(state='normal')
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {str(e)}")
        output_text.config(state='disabled')
        messagebox.showerror("Date Error", str(e))
        return

    read_time = f"{minutes} min read"
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

    json_str = json.dumps(result, indent=2)
    output_text.config(state='normal')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, json_str)
    output_text.config(state='disabled')

    # Save to file
    if messagebox.askyesno("Save", "Do you want to save the metadata to a file?"):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(json_str)
            messagebox.showinfo("Saved", f"Metadata saved to {file_path}")

def run_cli():
    print("Command-line Blog Metadata Creator")
    def get_input(prompt, default):
        val = input(f"{prompt} [{default}]: ").strip()
        return val if val else default

    title = get_input("Enter the title", DEFAULTS["title"])
    excerpt = get_input("Enter the excerpt", DEFAULTS["excerpt"])
    while True:
        date_input = get_input("Enter the date (e.g., Month DD YYYY)", DEFAULTS["date"])
        try:
            date = parse_date(date_input)
            break
        except ValueError as e:
            print(f"Error: {e}")
    minutes = get_input("Enter the read time in minutes", DEFAULTS["minutes"])
    image = get_input("Enter the image path", DEFAULTS["image"])
    author = get_input("Enter the author", DEFAULTS["author"])
    category = get_input("Enter the category", DEFAULTS["category"])
    slug = get_input("Enter the slug", DEFAULTS["slug"])

    read_time = f"{minutes} min read"
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
    json_str = json.dumps(result, indent=2)
    print(json_str)
    save = input("Save metadata to file? (y/N): ").strip().lower()
    if save == "y":
        file_path = input("Enter filename to save (default: metadata.json): ").strip()
        if not file_path:
            file_path = "metadata.json"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(json_str)
        print(f"Metadata saved to {file_path}")


def run_gui():
    global title_var, excerpt_var, date_var, minutes_var, image_var, author_var, category_var, slug_var, output_text
    root = tk.Tk()
    root.title("Blog Metadata Creator")

    fields = [
        ("Title", "title_var"),
        ("Excerpt", "excerpt_var"),
        ("Date (e.g., Month DD YYYY)", "date_var"),
        ("Read Time (minutes)", "minutes_var"),
        ("Image Path", "image_var"),
        ("Author", "author_var"),
        ("Category", "category_var"),
        ("Slug", "slug_var"),
    ]

    title_var = tk.StringVar(value=DEFAULTS["title"])
    excerpt_var = tk.StringVar(value=DEFAULTS["excerpt"])
    date_var = tk.StringVar(value=DEFAULTS["date"])
    minutes_var = tk.StringVar(value=DEFAULTS["minutes"])
    image_var = tk.StringVar(value=DEFAULTS["image"])
    author_var = tk.StringVar(value=DEFAULTS["author"])
    category_var = tk.StringVar(value=DEFAULTS["category"])
    slug_var = tk.StringVar(value=DEFAULTS["slug"])

    vars_map = {
        "title_var": title_var,
        "excerpt_var": excerpt_var,
        "date_var": date_var,
        "minutes_var": minutes_var,
        "image_var": image_var,
        "author_var": author_var,
        "category_var": category_var,
        "slug_var": slug_var,
    }

    for idx, (label, varname) in enumerate(fields):
        tk.Label(root, text=label).grid(row=idx, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(root, textvariable=vars_map[varname], width=40).grid(row=idx, column=1, padx=5, pady=5)

    tk.Button(root, text="Create Metadata", command=submit).grid(row=len(fields), column=0, columnspan=2, pady=10)

    output_text = scrolledtext.ScrolledText(root, width=60, height=15, state='disabled')
    output_text.grid(row=len(fields)+1, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        run_cli()
    else:
        run_gui()
