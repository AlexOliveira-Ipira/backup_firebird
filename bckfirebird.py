# Rotina de restaure , renomeando o banco para o 001
import os
from dotenv import load_dotenv
import fdb 

try:
  nome_arquivo = ('.env')
  if os.path.isfile(nome_arquivo):
    arquivo = open(nome_arquivo, 'r+')
  else:
    arquivo = open(nome_arquivo, 'w+')
    arquivo.writelines(u'BANCO_DADOS = Nome do Banco' +"\n")
    arquivo.writelines(u'BACKUP_NAME = Nome do Backup'+"\n")
    arquivo.writelines(u'BANCO_PATH = Pasta do Banco'+"\n")
    arquivo.writelines(u'BANCO_HOST = localhost'+"\n")
    arquivo.writelines(u'BANCO_USER = sysdba'+"\n")
    arquivo.writelines(u'BANCO_PASS = masterkey'+"\n")
    print()
    print('Favor alterar os dados no arquivo de configuração!')
    print('.env , se não encontrar na pasta favor habilitar ')
    print('nas configurações do windows a opção de visualizar')
    print('arquivos ocultos.')
    input("Pressione ENTER para continuar!")
except FileNotFoundError:
  print()
  print('Enconrado erro na criação do arquivo')

finally:
  arquivo.close()

if load_dotenv('.env'):
  BANCO = os.getenv('BANCO_DADOS')
  BACKUP_NAME = os.getenv('BACKUP_NAME')
  BANCO_PATH = os.getenv('BANCO_PATH')
  BANCO_HOST = os.getenv('BANCO_HOST')
  BANCO_USER = os.getenv('BANCO_USER')
  BANCO_PASS = os.getenv('BANCO_PASS')
else:
  print()
  print('erro lendo variaveis')

#Conectando ao banco
try:
  con = fdb.services.connect(host=BANCO_HOST,user=BANCO_USER, password=BANCO_PASS)
  if BANCO != 'Nome do Banco' and BACKUP_NAME !='Nome do Backup'and BANCO_PATH !='Pasta do Banco':
    print()
    print(f'Realizando o backup do arquivo {BANCO} para o arquivo {BACKUP_NAME}', end='\n')
except fdb.Error:
  print()
  print('Arquivo de configuação invalido')
#Mostra as linhas após o backup
#Verifica a possibilidade de melhorar essa rotina
def infoback(line):
  print(line)

#Função do backup
def backuplgpd(banco , backup): 
  try:
    con.backup(banco, backup, callback=infoback)
  except fdb.Error:
    print()
    print('Arquivo de configuação invalido, verifique!')

#Chamando a função do bakup

if __name__ == '__main__':
  backuplgpd( BANCO_PATH + BANCO , BANCO_PATH + BACKUP_NAME)
