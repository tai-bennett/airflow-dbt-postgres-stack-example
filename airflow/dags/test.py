"""
Hello, this is a test.
"""

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime
from airflow.sdk import task, dag
import pendulum

# [START default args]
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}
# [END default args]

# THIS IS THE OLD METHOD
# # [START instantiate dags]
# with DAG("1_init_dag",default_args=default_args) as dag:
#     t1 = BashOperator(
#         task_id="touch_file",
#         bash_command="touch output.txt"
#     )
# 
#     t2 = BashOperator(
#         task_id="date",
#         bash_command="date >> ./output.txt"
#     )
# 
#     t3 = BashOperator(
#         task_id="whoami",
#         bash_command="whoami"
#     )
# 
#     # set the dependency of these tasks t1, t2, t3
#     t1 >> t2 >> t3
# # [END instantiate dags]

# This is the pythonic style dags

@dag(
    schedule=None,
    start_date=pendulum.datetime(2020, 1, 1, tz="UTC"),
    catchup=False,
    tags=["test"]
)
def test_pipeline():
    @task(multiple_outputs=True)
    def step1():
        return {"a": 100, "b": 200, "c": 300}
    @task
    def step2(input: dict):
        out = 0
        for v in input.values():
            out += v
        return out
    @task
    def step3(input):
        print("The total is: " + str(input))
    out = step1()
    out = step2(out)
    step3(out)

test_pipeline()
