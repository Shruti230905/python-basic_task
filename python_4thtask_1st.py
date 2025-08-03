# read_file_with_error_handling.py

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Reading contents of {filename}:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Call the function
read_file("sample.txt")
