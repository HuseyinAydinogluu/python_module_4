import sys


print("=== Cyber Archives Recovery ===")


if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
    sys.exit()


filename = sys.argv[1]

print(f"Accessing file '{filename}'")


file = None
content = ""

try:
    file = open(filename, "r") 
    content = file.read()
    print("---\n")
    print(content, end="")
    print("---")


except FileNotFoundError as e:
    print(f"Error opening file '{filename}': {e}")

except PermissionError as e:
    print(f"Error opening file '{filename}': {e}")

finally:
    if file:
        file.close()
        print(f"File '{filename}' closed.")

print(f"Transform data:")
print(f"---\n")
lines = content.split("\n")
new_lines = [line + "#" for line in lines]
new_content = "\n".join(new_lines)
print(new_content)
print("---")

input_filename = input(f"Enter new file name (or empty):")

if input_filename == "":
    print(f"Not saving data.")
else:
    print(f"Saving data to '{input_filename}'")

    last_file = open(input_filename, "w")
    last_file.write(new_content)
    last_file.close()

    print(f"Data saved in file '{input_filename}.")
    
