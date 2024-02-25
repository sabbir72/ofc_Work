import os

def count_lines_in_file(file_path):
    """Count the number of lines in a file."""
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

def count_lines_in_folder(folder_path):
    """Count the number of lines in each text file inside a folder."""
    line_count = 0
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                line_count += count_lines_in_file(file_path)
    return line_count

def main():
    folder_path = r'Enter File path here'  # Change this to the desired folder path
    total_lines = count_lines_in_folder(folder_path)
    print(f"Total number of lines in all .txt files: {total_lines}")

if __name__ == "__main__":
    main()
