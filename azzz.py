import os
from os.path import isfile, splitext, basename, abspath, exists, isdir, normpath
import tkinter as tk
import sys
from sys import argv
import subprocess
#compremidos
import zipfile#para criar, extrair e listar .zips
import tarfile#para listar, extrair e criar .tar
import rarfile#para listar .rar
import gzip#para criar, extrair e ler .gz e .z
import py7zr#para criar, extrair e listar .7z

#rar.exe para criar .rar
#unrar.exe para extrair .rar
#tar.exe para criar .tar, .taz e .tgz

#modos
#c para criar um arquivo compremido
#e para extrair um arquivo compremido
#se nao tiver nenhum modo, o modo = 'L'

#funcao para obter todas as estensoes de um arquivo
def spl(c):
    c= c.split('.')
    if not c:
        return '[]'
    
    c= list(c)
    if len(c) < 2:
        return str(c)
    elif len(c) == 3:
        c= f'{c[-2]}.{c[-1]}'
        return c
    else:
        return ' '.join(c[1:])

def ler(path, ext):
    match ext:
        case 'gz':
            with gzip.open(path, 'rb') as f:
                data = f.read()
                print(data.decode('utf-8'))
        case 'xz':
            print('Sem suporte')
def listar(path, ext):
        match ext:
            case 'zip':
                z= zipfile.ZipFile(path, 'r')
                for i in z.namelist():
                    print(f'[item]: {i}')
            case 'rar':
                r= rarfile.RarFile(path, 'r')
                for i in r.namelist():
                    print(f'[item]: {i}')
            case 'tar':
                t= tarfile.open(path, 'r')
                for i in t.getmembers():
                    print(f'[item]: {i.name}')
            case 'tgz' | 'taz':
                t= tarfile.open(path, 'r:gz')
                for i in t.getmembers():
                    print(f'[item]: {i.name}')
            case 'gz':
                ler(path, ext)
            case '7z':
                sz= py7zr.SevenZipFile(path, mode='r')
                for i in sz.getnames():
                    print(i)
            case 'xz':
                print('Sem suporte')
            case 'tar.gz':
                t= tarfile.open(path, 'r:gz')
                for i in t.getmembers():
                    print(f'[item]: {i.name}')
            case 'tar.xz':
                t= tarfile.open(path, 'r:xz')
                for i in t.getmembers():
                    print(f'[item]: {i.name}')
def extrair(path, ext, novo):
    match ext:
        case 'zip':
            os.makedirs(novo, exist_ok=True)
            print(f'{path} para <{novo}>/')
            # Extraindo o arquivo .zip
            z= zipfile.ZipFile(path, 'r')
            z.extractall(novo)
            print(f'[concluido] => extracao feita')
        case 'rar':
            os.makedirs(novo, exist_ok=True)
            print(f'{path} para <{novo}>/')
            ca= ['unrar.exe', 'x', path, novo]
            comando= subprocess.run(ca, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if comando.returncode== 0:
                print(f'[concluido] => extracao feita')
            else:
                print(f'[encerramento] => ocorreu algum erro')
        case 'tar' | 'taz' |'tgz':
            os.makedirs(novo, exist_ok=True)
            print(f'{path} para <{novo}>/')
            t= tarfile.open(path, "r:*")
            # Extrai todos os arquivos para o diretório de destino
            t.extractall(novo)
            print(f'[concluido] => extracao feita, nao ocorreu erros')
        case '7z':
            os.makedirs(novo, exist_ok=True)
            print(f'{path} para <{novo}>/')
            seven= py7zr.SevenZipFile(path, mode='r')
            seven.extractall(novo)
            print(f'[concluido] => extracao feita')
        case 'gz':
            print(f'{path} transformado para {novo}')
            with gzip.open(path, 'rb') as g:
                with open(novo, 'ab') as a:
                    a.write(g.read())
            print(f'[concluido] => extracao feita')
        case 'xz':
            print('Sem suporte')
        case 'tar.gz':
            os.makedirs(novo, exist_ok=True)
            print(f'{path} para <{novo}>/')
            # Abrindo o arquivo .tar.gz
            t= tarfile.open(path, 'r:gz')
            t.extractall(novo)
            print(f'[concluido] => extracao feita')
        case 'tar.xz':
            os.makedirs(novo, exist_ok=True)
            print(f'{path} para <{novo}>/')
            # Abrindo o arquivo .tar.gz
            t= tarfile.open(path, 'r:xz')
            t.extractall(novo)
            print(f'[concluido] => extracao feita')

def criar(path, ext, novo):
    match ext:
        case 'zip':
            path= path.split(' ')
            for i in path:
                if isdir(i):
                    with zipfile.ZipFile(novo, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                    #Percorre todos os diretórios e arquivos dentro da pasta
                        for root, dirs, files in os.walk(i):
                            for file in files:
                                # Cria o caminho completo do arquivo
                                file_path = os.path.join(root, file)
                                # Adiciona o arquivo ao ZIP, mantendo a estrutura de diretórios
                                zip_file.write(file_path, os.path.relpath(file_path, i))
                            for dir in dirs:
                                # Cria o caminho completo do arquivo
                                file_path = os.path.join(root, dir)
                                # Adiciona o arquivo ao ZIP, mantendo a estrutura de diretórios
                                zip_file.write(file_path, os.path.relpath(file_path, i))
            print(f'[concluido] arquivo {novo} foi criado, com um total de {len(path)} de itens')
        case 'rar':
            ca= ['rar.exe', 'a', novo]
            path= path.split(' ')
            for i in path:
                ca.append(i)
            comando= subprocess.run(ca, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if comando.returncode== 0:
                print(f'[concluido] arquivo {novo} foi criado, com um total de {len(path)} de itens')
            else:
                print(f'[encerramento] => ocorreu algum erro')
        case 'tar':
            path= path.split(' ')
            with tarfile.open(novo, 'w') as t:
                for i in path:
                    t.add(i)
            print(f'[concluido] arquivo {novo} foi criado, com um total de {len(path)} de itens')
        case 'taz':
            ca= ['tar.exe', '-czf', novo]
            path= path.split(' ')
            for i in path:
                ca.append(i)
            comando= subprocess.run(ca, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if comando.returncode== 0:
                print(f'[concluido] arquivo {novo} foi criado, com um total de {len(path)} de itens')
            else:
                print(f'[encerramento] => ocorreu algum erro')
        case 'tgz':
            path= path.split(' ')
            with tarfile.open(novo, 'w:gz') as t:
                for i in path:
                    t.add(i)
            print(f'[concluido] arquivo {novo} foi criado, com um total de {len(path)} de itens')
        case 'gz':
            a= open(path, 'rb')
            data= a.read()
            a.close()
            novo= splitext(novo)
            path= splitext(path)
            novo= novo[0] + path[1] + novo[1]
            with gzip.open(novo, 'wb') as f:
                f.write(data)
            print(f'[concluido] arquivo {novo} foi criado')
        case '7z':
            path= path.split(' ')
            with py7zr.SevenZipFile(novo, 'w') as seven:
                for i in path:
                    # Adicione arquivos ao arquivo .7z
                    if isdir(i):
                        seven.writeall(abspath(i), arcname= i)
                    else:
                        seven.write(abspath(i), arcname= i)
            print(f'[concluido] arquivo {novo} foi criado, com um total de {len(path)} de itens')
        case 'xz':
            print('Sem suporte')
m= argv[1]
def modo(path, ext, novo):
    if m== 'e':
        extrair(path, ext, novo)
    elif m== 'c':
        criar(path, ext, novo)
        
#verificando os argumentos
if len(argv) >= 3:#se for passado argumento 'c' ou 'e'
    #novo= ''#onde sera o nome do novo arquivo compremido ou o nome da pasta que o arquivo sera extraido
    if m== 'c':
        novo= argv[-1]
        argv.pop()
        c= ' '.join(argv[2:])
        exts= spl(novo)
        modo(c, exts, novo)
    elif m== 'e':
        novo= argv[-1]
        argv.pop()
        c= ' '.join(argv[2:])
        exts= spl(c)
        modo(c, exts, novo)
    else:
        print('[erro] => modo invalido')
        sys.exit()

elif len(argv) == 2:#foi passado o nome do arquivo main.py + um compremido
    c= ' '.join(argv[1:])
    #sep= splitext(c)
    exts= spl(c)
    sep= exts.split('.')
    if isfile(c):
        listar(c, exts)
    else:
        print(f'[erro] nao e um arquivo ou nao sem suporte')
        sys.exit()

elif len(argv) == 1:
    print('[info]: Ajuda da cli')
    print('Este script serve para manipulacao de arquivos compremidos')
    print('tendo suporte para os seguintes tipos:')
    print('.zip, .tar, .rar, .7z, .z, .gz, .taz, .tgz')
    print()
    print('O funcionamento é:')
    print('Caso digite apenas o nome da cli, ira para sessao de ajuda')
    print('Caso digite o nome da cli, o modo, e, um arquivo compremido, ira fazer a funcao do modo')
    print('[modos]: L ou sem modo para listar o conteudo, \nC para criar um novo compremido,\nE para extrair')
    print("[nota]: se o caminho do arquivo compremido for grande, passe entre '' ")
    print('Para criar arquivos compremidos, passe primeiro o conteudo, e por ultimo o nome do arquivo compremido a ser criado')

else:
    print('Ocorreu um erro')