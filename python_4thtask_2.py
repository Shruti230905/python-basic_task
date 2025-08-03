# write_append_read_file.py

def write_append_read_file(filename):
    # Step 1: Write user input
    user_input = input("Enter some text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')

    # Step 2: Append more data
    additional_input = input("Enter more text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(additional_input + '\n')

    # Step 3: Read and display the content
    print("\nFinal content of the file:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# Call the function
write_append_read_file("output.txt")
