import requests

def get_repo_description(repo_url: str) -> str:
    """
    Retrieve and return the description of a GitHub repository.

    Args:
        repo_url (str): The URL of the GitHub repository.

    Returns:
        str: The description of the repository.

    Raises:
        ValueError: If the provided URL is not a valid GitHub repository URL.
        Exception: If there is an error while retrieving information from the repository.
    """

    parts = repo_url.split("/")

    if len(parts) < 5 or parts[2] != "github.com":
        raise ValueError("The URL provided is not a valid GitHub repository URL.")

    user = parts[3]
    repo = parts[4]

    api_url = f"https://api.github.com/repos/{user}/{repo}"

    response = requests.get(api_url)

    if response.status_code == 200:
        repo_info = response.json()
        description = repo_info.get("description", "No description available.")
        return description
    else:
        raise Exception(
            f"Error while retrieving information from the repository: {response.status_code}"
        )
