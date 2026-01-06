import requests

def fetch_repo(repo_url):
    owner, repo = repo_url.split("/")[-2:]
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    res = requests.get(api_url)
    files = res.json()

    code = ""

    for file in files:
        if file["type"] == "file" and file["name"].endswith((".py",".js",".java",".cpp")):
            raw_url = file["download_url"]
            code += requests.get(raw_url).text + "\n\n"

    return code
