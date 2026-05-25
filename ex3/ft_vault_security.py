def secure_archive(filename, action="read", content=None):
    try:
        if action == "read":
            with open(filename, "r") as f:
                data = f.read()
            return (True, data)

        elif action == "write":
            with open(filename, "w") as f:
                f.write(content if content else "")
            return (True, "Content successfully written to file")

        else:
            return (False, "Invalid action")


    except FileNotFoundError:
        return (False, f"[Errno 2] No such file or directory: '{filename}'")

    except PermissionError:
        return (False, f"[Errno 13] Permission denied: '{filename}'")

    except Exception as e:
        return (False, str(e))


print("=== Cyber Archives Security ===")

print("Using 'secure_archive' to read from a nonexistent file:")
print(secure_archive("/not/existing/file", "read"))

print("\nUsing 'secure_archive' to read from an inaccessible file:")
print(secure_archive("/etc/master.passwd", "read"))

print("\nUsing 'secure_archive' to read from a regular file:")
print(secure_archive("ancient_fragment.txt", "read"))

print("\nUsing 'secure_archive' to write previous content to a new file:")
print(secure_archive("new_file.txt", "write", "Test content"))