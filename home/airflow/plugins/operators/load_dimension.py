from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 table = "",
                 select_sql = "",
                 append_insert = False,
                 primary_key = "",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.select_sql = select_sql
        self.append_insert = append_insert
        self.primary_key = primary_key
  

    def execute(self, context):
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        if self.append_insert:
            table_insert_sql = f"""          
                INSERT INTO {self.table}
                {self.select_sql};
            """
        else:
            redshift_hook.run(f"TRUNCATE TABLE {self.table};")
            table_insert_sql = f"""          
                INSERT INTO {self.table}
                {self.select_sql};
            """
            
            
        
        self.log.info('LoadDimensionOperator not implemented yet')
        redshift_hook.run(table_insert_sql)
        
        
