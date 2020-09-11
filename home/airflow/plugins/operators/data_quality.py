from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 sample_query = "",
                 expected_output = "",
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.sample_query = sample_query
        self.expected_result = expected_result
        

    def execute(self, context):
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        
        records = redshift_hook.get_records(self.sample_query)
        if records[0][0] != self.expected_output:
            raise ValueError(f"""
                Data quality check failed. \
                {records[0][0]} does not equal {self.expected_output}
            """)
        else:
            self.log.info("Data quality check passed")
            
        self.log.info('DataQualityOperator not implemented yet')