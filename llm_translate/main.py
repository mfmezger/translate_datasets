from prefect import flow, task
from typing import List
import httpx


@task(retries=3)
def download_datasets(repo: str):
    url = f"https://api.github.com/repos/{repo}"

@task()
def convert_to_csv(repo: str):
    pass


@flow(name="GitHub Stars")
def dataset_preprocessing(repos: List[str]):
    for repo in repos:
        download_datasets(repo)


# run the flow!
dataset_preprocessing(["PrefectHQ/Prefect"])