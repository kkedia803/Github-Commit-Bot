import requests

def fetch_joke():
    """Fetch a random joke from the API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"{data['setup']} {data['punchline']}"
    else:
        return "Joke generator has taken a leave today. Do some work today!!!!"

def update_html(joke):
    """Update the HTML file with the new joke."""
    html_file = "index.html"
    with open(html_file, "r") as file:
        content = file.readlines()

    # Find the joke placeholder in the HTML
    for i, line in enumerate(content):
        if "<div id=\"joke\">" in line:
            content[i+1] = f"        <p>{joke}</p>\n"
            break

    with open(html_file, "w") as file:
        file.writelines(content)

if __name__ == "__main__":
    joke = fetch_joke()
    update_html(joke)
