## end to end machine learning project


import dagshub
dagshub.init(repo_owner='Nagesh1233', repo_name='aimlproject', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)