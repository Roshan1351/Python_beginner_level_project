import re

def extract_emails(input_file, output_file):
    try:
        # Read text from input file
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()

        # Find all email addresses using regex
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)

        # Save extracted emails to output file
        with open(output_file, "w", encoding="utf-8") as f:
            for email in emails:
                f.write(email + "\n")

        print(f"✅ Extracted {len(emails)} emails to {output_file}")

    except FileNotFoundError:
        print("❌ Input file not found. Please check the file path.")

if __name__ == "__main__":
    # Example usage: create a file 'sample.txt' with some emails inside it
    extract_emails("sample.txt", "emails.txt")