FROM python:3.10
RUN python -m pip install --upgrade pip
RUN pip install apache-airflow[postgres]==3.1.7 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.1.7/constraints-3.10.txt" &&\
    pip install dbt==1.0.0.40.14 && \
    pip install SQLAlchemy==2.0.47 && \
    pip install graphviz
    # pip install 'apache-airflow[postgres]==1.10.14' && \
    # pip install --force-reinstall -v "MarkupSafe==2.0.1"
    # pip install dbt==0.15 && \
    # pip install SQLAlchemy==1.3.23
    # pip install wtforms==2.3.3 && \

RUN mkdir /project
COPY scripts_airflow/ /project/scripts/
COPY dags /project/dags/

RUN chmod +x /project/scripts/init.sh
RUN echo "start of entrypoint"
# ENTRYPOINT [ "/project/scripts/init.sh" ]
