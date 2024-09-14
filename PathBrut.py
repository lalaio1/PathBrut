import sys
import time
import queue
import os.path
import random
import argparse
import requests
from concurrent.futures import ThreadPoolExecutor
from typing import List, Optional
from resources.banner import *
from resources.colors import *
from resources.useragents import *

print(banner)

def main(args: argparse.Namespace) -> None:
    extensoes = [ext.strip() for ext in args.extensoes.split(',')] if args.extensoes else []
    
    try:
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            futuros = [executor.submit(dir_bruter, args, extensoes) for _ in range(args.threads)]
            
            for futuro in futuros:
                try:
                    futuro.result()
                except Exception as e:
                    if args.verbose:
                        print(f"{white}[{red}ERRO{white}] Erro na execução da thread: {red}{e}{reset}")

    except Exception as e:
        print(f"{white}[{red}ERRO{white}] Ocorreu um erro inesperado: {red}{e}{reset}")

def validar_wordlist(parser: argparse.ArgumentParser, caminho_wordlist: str) -> Optional[List[str]]:
    if not os.path.exists(caminho_wordlist):
        parser.error(f"O arquivo especificado {caminho_wordlist} não foi encontrado.")
    
    try:
        with open(caminho_wordlist, 'r', encoding='utf-8') as arquivo:
            palavras = arquivo.readlines()
        print(f"{white}> Wordlist: {green}{caminho_wordlist}{reset}")
        return [palavra.strip() for palavra in palavras]
    except IOError as e:
        parser.error(f"Erro ao abrir a wordlist {caminho_wordlist}: {e}")

def salvar_resultados(url_alvo: str) -> None:
    try:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('resultados_PathBrut.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'[{timestamp}] : {url_alvo}\n')
        print(f"{green}[SUCESSO]{reset} Resultado salvo: {url_alvo}")
    except IOError as e:
        print(f"{red}[ERRO]{reset} Não foi possível salvar o resultado: {e}")

def dir_bruter(args: argparse.Namespace, extensoes: List[str]) -> None:
    url_base = args.url.rstrip('/')
    palavras = queue.Queue()

    for palavra in args.wordlist:
        palavras.put(palavra)
    
    while not palavras.empty():
        tentativa = palavras.get()
        lista_tentativas = []

        if "." not in tentativa:
            lista_tentativas.append(f"/{tentativa}/")
        else:
            lista_tentativas.append(f"/{tentativa}")

        if extensoes:
            lista_tentativas.extend([f"/{tentativa}{extensao}" for extensao in extensoes])

        for brute in lista_tentativas:
            url_alvo = f"{url_base}{brute}"
            testar_url(url_alvo, args)

def testar_url(url_alvo: str, args: argparse.Namespace) -> None:
    headers = {"User-Agent": random.choice(user_agents)}
    try:
        with requests.get(url_alvo, headers=headers, timeout=5) as resposta:
            if resposta.status_code == 200:
                if args.output:
                    salvar_resultados(url_alvo)
                print(f"{white}[{green}+{white}] {resposta.status_code}: {green}{url_alvo}{reset}")
            elif resposta.status_code == 404:
                if args.verbose:
                    print(f"{white}[{red}-{white}] {resposta.status_code}: {red}{url_alvo}{reset}")
            else:
                if args.verbose:
                    print(f"{white}[{blue}?{white}] {resposta.status_code}: {blue}{url_alvo}{reset}")
    except requests.Timeout:
        if args.verbose:
            print(f"{white}[{dark_yellow}T{white}] Requisição expirou: {dark_yellow}{url_alvo}{reset}")
    except requests.RequestException as e:  
        if args.verbose:
            print(f"{white}[{red}ERRO{white}] Ocorreu um erro: {red}{e}{reset}")

def configurar_argumentos() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=f'',
    )
    parser.add_argument('-t', '--threads', type=int, help='número de threads (padrão é 1)', metavar='<threads>', default=1)
    parser.add_argument('-u', '--url', type=str, help='URL alvo', metavar='<url>', required=True)
    parser.add_argument('-w', '--wordlist', help="arquivo/caminho para a wordlist", metavar='<wordlist>', required=True, type=lambda x: validar_wordlist(parser, x))
    parser.add_argument('-o', '--output', help='salvar resultados encontrados em um arquivo', action='store_true')
    parser.add_argument('-v', '--verbose', help='saída detalhada (mostrar logs/erros de rede)', action='store_true')
    parser.add_argument('-e', '--extensoes', help='extensões (exemplo ".php,.exe,.bak")', metavar='<extensoes>')
    return parser

if __name__ == '__main__':
    parser = configurar_argumentos()
    args = parser.parse_args()
    
    try:
        print(f"{white}> Alvo: {green}{args.url}{reset}")
        print(f"{white}-{reset}" * 41)
        main(args)
    except KeyboardInterrupt:
        print(f"{white}[{red}CTRLC{white}] Saindo...{reset}")
        sys.exit(1)
    except Exception as e:
        if args.verbose:
            print(f"{white}[{red}ERRO{white}] Ocorreu um erro: {red}{e}{reset}")