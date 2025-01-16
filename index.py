import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Read the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Convert rows to a list of dictionaries
        data = [row for row in csv_reader]

    # Write data to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

# Example usage
csv_file_path = 'projects.csv'  # Replace with your CSV file path
json_file_path = 'projects.json'  # Replace with your desired JSON output path
csv_to_json(csv_file_path, json_file_path)
print(f"CSV has been converted to JSON and saved to {json_file_path}")
