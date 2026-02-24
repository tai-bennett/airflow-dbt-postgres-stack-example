"""
Hello, this is a test.
"""

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

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

# [START instantiate dags]
init_dag = DAG(
    "1_init_dag",
    default_args=default_args,
    schedule_interval=@once
)
test_dag = DAG(
    "2_test_dag",
    default_args=default_args,
    schedule_interval=None
)
# [END instantiate dags]

t1 = BashOperator(
    task_id="touch file",
    bash_command="touch ./output.txt",
    dag=init_dag
)

t2 = BashOperator(
    task_id="date",
    bash_command="date >> ./output.txt",
    dag=test_dag
)

t3 = BashOperator(
    task_id="whoami",
    bash_command="whoami >> ./output.txt",
    dag=test_dag
)

t1
t2 >> t3
