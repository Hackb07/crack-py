import os
from langflow.main import run

if __name__ == "__main__":
    os.environ["GROQ_API_KEY"] = "your-key"  # or use dotenv
    run()
