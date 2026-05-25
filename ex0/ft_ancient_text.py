import sys


print("=== Cyber Archives Recovery ===")


if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
    sys.exit()


filename = sys.argv[1]

print(f"Accessing file '{filename}'")


file = None

try:
    file = open(filename, "r") # dosya read modunda acılır

    print("---\n")

    content = file.read()
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