def read_and_write_files():
    input_name = input("Enter the name of the file to read: ")

    try:
        
        with open(input_name, 'r') as file:
            data = file.read()

        
        output_filename = "modified_" + input_name
        with open(output_filename, "w") as output_file:
            output_file.write(data)
        
        print(f"Modified content written to: {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_name}' does not exist.")
    except IOError as e:
        print(f"Error: An error occurred while reading or writing the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_and_write_files()
