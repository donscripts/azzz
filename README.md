# azzz > compr-ncompr
Manipulação de arquivos compremidos

# *azzz.exe*:
ele tem as mesmas funcionalidades dos arquivos *ncompr.exe* e *compr.exe*, porém, um pouco melhoradas.

### Suporte:
1. zip
2. rar
3. tar
4. taz
5. tgz
6. tar.gz
7. tar.xz

### suporte para criação:
1. rar
2. zip
3. tar
4. taz
5. tgz
6. .gz

### suporte para extração:
1. rar
2. zip
3. tar
4. taz
5. tgz
6. tar.gz
7. tar.xz
8. .gz => no caso seria a leitura

# Funcionamento:
## listar:
para listar o conteudo de um arquivo compremido, basta apenas:
azzz.exe nome do arquivo
azzz.exe tar.tar

## criar:
para criar um arquivo compremido, basta:
azzz.exe c "arquivos para serem adicionados ao compremido" "nome do arquivo compremido"
azzz.exe c pasta1 pasta2 pasta3 arquivo.rar

## extrair:
para extrair um arquivo compremido, basta:
azzz.exe e "arquivo compremido" "pasta a ser criada com o conteudo dele"
azzz.exe zip.zip pastaZ
