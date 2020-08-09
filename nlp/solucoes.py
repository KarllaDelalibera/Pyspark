# Caminhos 
path_tratamento_texto = "helpers/tratamento_descricoes.py"

# Modulos auxiliares
# Adiciona o arquivo .py ao sparkcontext para disponibiliza-lo aos seus executores
sc = spark.sparkContext
sc.addPyFile(path_tratamento_texto)

# importacao de modulos
from pyspark.sql.functions import udf

from nlp.helpers import tratamento_descricoes

tratamento_texto = tratamento_descricoes.TratamentoTexto()


@udf('string')
def tratamento_strings(text):
    texto = str(text)
    texto = texto.lower()
    texto = tratamento_texto.remove_pontuacao(texto)
    texto = tratamento_texto.remove_acentuacao(texto)
    texto = tratamento_texto.remove_space(texto)
    texto = tratamento_texto.remove_space_duplicado(texto)
    return texto


# df -> dataframe
df = df.withColumn("nova_coluna_texto", tratamento_strings("coluna_texto"))

# O mesmo processo utilizando map
# df.rdd.map(lambda x: tratamento_strings(x["coluna_texto"]))\
#       .map(lambda x: Row(x)).toDF(["novo_coluna_texto"])
