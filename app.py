from flask import Flask
import subprocess
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system details
    name = "Richa Saurabh"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")

    # Run `top` command and capture output
    top_output = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True).stdout

    # Create response
    return f"""
    <pre>
    Name: {name}
    Username: {username}
    Server Time (IST): {server_time}

    TOP output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
