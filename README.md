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

suporte:
1. rar
2. zip
3. tar
4. taz
5. tgz
6. gz => no caso vai ler o arquivo
7. 7z

## criar:
para criar um arquivo compremido, basta:
azzz.exe c "arquivos para serem adicionados ao compremido" "nome do arquivo compremido"
azzz.exe c pasta1 pasta2 pasta3 arquivo.rar

suporte:
1. rar
2. zip
3. 7z
4. tar
5. taz
6. tgz
7. gz

## extrair:
para extrair um arquivo compremido, basta:
azzz.exe e "arquivo compremido" "pasta a ser criada com o conteudo dele"
azzz.exe zip.zip pastaZ

suporte:
1. rar
2. tar
3. zip
4. taz
5. tgz
6. 7z
7. gz => no caso vai criar um novo arquivo
8. tar.gz
9. tar.xz
