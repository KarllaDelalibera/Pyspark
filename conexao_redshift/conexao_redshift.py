from common import constants


## URL JDBC para conexao com o redshift
redshift_url = constants.REDSHIFT_URL.format(host=constants.HOST,
                                             port=constants.PORT,
                                             dbname=constants.DBNAME,
                                             user=constants.USER,
                                             password=constants.PASSWORD)


## Consulta que deseja executar
redshift_query  = """SELECT *
                     FROM name_table
                     LIMIT 10
                  """

## Executando consulta
df = spark.read \
    .format("jdbc") \
    .option("url", redshift_url) \
    .option("query",redshift_query)\
    .load()

df.show()