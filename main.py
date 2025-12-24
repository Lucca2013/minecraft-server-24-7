import subprocess

try:
    subprocess.run(
        ["/workspaces/minecraft-server-24-7/minecraft/run_crafty.sh"],
        check=True
    )

except subprocess.CalledProcessError as e:
    print(f"Error on executing the script: {e}")
except FileNotFoundError:
    print("File .sh not found")
