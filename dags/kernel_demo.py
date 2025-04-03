from datetime import datetime
import requests
import logging

logger = logging.getLogger(__name__)


from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.providers.github.operators.github import GithubOperator
from common.github_processor import post_process_github_org


# A DAG represents a workflow, a collection of tasks
with DAG(
    dag_id="kernel_demo",
    start_date=datetime(2025, 1, 1),
    schedule="14 0 * * *",
    tags=["kernel_demo"],
    catchup=False,
) as dag:
    # Tasks are represented as operators

    # NODE 1
    @task()
    def airflow():
        print("airflow")

    airflow_node = airflow()

    # NODE 2
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    # NODE 3
    @task()
    def call_w3():
        x = requests.get("https://w3schools.com/python/demopage.htm")
        # print the response text (the content of the requested file):
        print(x.text)
        open("w3.html", "w").write(x.text)

    w3 = call_w3()

    # NODE 4
    github_list_repos = GithubOperator(
        task_id="github_list_repos",
        github_method="get_user",
        github_conn_id="github_default",
        github_method_args={"login": "Tymotheus"},
        result_processor=lambda user: logger.info(list(user.get_repos())),
    )

    # NODE 5
    github_get_organization = GithubOperator(
        task_id="github_get_organization",
        github_method="get_organization",
        github_conn_id="github_default",
        github_method_args={"org": "kni-kernel"},
        result_processor=post_process_github_org,
    )

    # NODE 6
    @task()
    def test_github_report():
        content = open("commits.txt").read().splitlines()
        print(content)
        assert len(content) == 1

    test_github_node = test_github_report()

    # Set dependencies between tasks
    airflow_node >> hello
    airflow_node >> w3
    hello >> github_list_repos

    w3 >> github_list_repos
