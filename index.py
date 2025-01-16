import csv
import json
import unicodedata
import re

def slugify(value: str) -> str:
    """
    Converts a string to a URL-friendly slug.
    - Replaces spaces with underscores.
    - Removes special characters and accents.
    """
    # Normalize string to remove accents
    value = unicodedata.normalize('NFD', value).encode('ascii', 'ignore').decode('utf-8')
    # Replace spaces with underscores and remove non-alphanumeric characters
    value = re.sub(r'\s+', '_', value)  # Replace spaces with underscores
    value = re.sub(r'[^\w_]', '', value)  # Remove special characters except underscores
    return value.lower()  # Convert to lowercase

def csv_to_json_with_slug(csv_file_path, json_file_path):
    # Read the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Convert rows to a list of dictionaries with an additional 'project_slug' field
        data = []
        for row in csv_reader:
            row['PROJECT_SLUG'] = slugify(row['PROJECT'])  # Create the slug from the 'Project' column
            data.append(row)

    # Write data to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

# Example usage
csv_file_path = 'projects.csv'  # Replace with your CSV file path
json_file_path = 'projects.json'  # Replace with your desired JSON output path
csv_to_json_with_slug(csv_file_path, json_file_path)
print(f"CSV has been converted to JSON with slugs and saved to {json_file_path}")
