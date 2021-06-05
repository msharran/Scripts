import subprocess as sb

process = sb.run(["ls", "-la", "dne"], capture_output=True, text=True)
if process.returncode != 0:
    print("Error", process.stderr)
else:
    print("Success", process.stdout)

