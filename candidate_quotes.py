import re

def extract_records(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        dataset = file.read()

    # Revised regular expression pattern to capture the entire record
    pattern = r'^(.*?)(?=\n\n|\Z)'
    
    # Find all matches in the dataset
    matches = re.findall(pattern, dataset, re.DOTALL | re.MULTILINE)

    records = []
    for match in matches:
        # Splitting each record into its components
        parts = match.strip().split('\n')
        if len(parts) >= 3:
            statement = parts[0].strip()
            source = parts[-1].strip()
            content = '\n'.join(parts[1:-1]).strip()
            record = {
                "Statement": statement,
                "Content": content,
                "Source": source
            }
            records.append(record)

    return records

def main(file_path):
    records = extract_records(file_path)
    for record in records:
        print(f"Statement: {record['Statement']}\nContent: {record['Content']}\n{record['Source']}\n\n")


if __name__ == '__main__':
    main('candidates/president/republican/trump/DonaldTrumpOnTheIssuesCorporations.txt')