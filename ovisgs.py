import dns.resolver
import requests
import colorama
import sys
import time
from colorama import Fore, Style

# Inicialize o colorama para adicionar cores ao terminal
colorama.init(autoreset=True)

# Banner colorido
banner = f"""
{Fore.RED}
 ██████╗ ██╗   ██╗██╗███████╗ ██████╗ ███████╗
██╔═══██╗╚██╗ ██╔╝██║██╔════╝██╔════╝ ██╔════╝
██║   ██║ ╚████╔╝ ██║███████╗██║  ███╗███████╗
██║   ██║  ╚██╔╝  ██║╚════██║██║   ██║╚════██║
╚██████╔╝   ██║   ██║███████║╚██████╔╝███████║
 ╚═════╝    ╚═╝   ╚═╝╚══════╝ ╚═════╝ ╚══════╝
{Fore.RESET}
Subdomínio Finder - Encontre subdomínios rapidamente!
"""

def find_subdomains(base_url, wordlist_file):
    # Carregando a lista de palavras
    with open(wordlist_file, "r") as file:
        wordlist = file.read().splitlines()

    subdomains = set()

    print("Procurando subdomínios... ", end="", flush=True)
    animation = "|/-\\"
    for _ in range(20):
        for char in animation:
            sys.stdout.write(char)
            sys.stdout.flush()
            sys.stdout.write("\b")

            time.sleep(0.1)

    for word in wordlist:
        subdomain = f"{word}.{base_url}"
        try:
            # Consulta DNS para verificar se o subdomínio existe
            answers = dns.resolver.query(subdomain, "A")
            if answers:
                subdomains.add(subdomain)
        except dns.resolver.NXDOMAIN:
            pass

    return subdomains

if __name__ == "__main__":
    print(banner)
    base_url = input("Digite o site alvo (com HTTP ou HTTPS): ")
    wordlist_file = input("Digite o caminho para o arquivo de lista de palavras: ")

    subdomains = find_subdomains(base_url, wordlist_file)

    if subdomains:
        print("\nSubdomínios encontrados:")
        for subdomain in subdomains:
            print(f"{Fore.GREEN}{subdomain}{Fore.RESET}")
    else:
        print(f"{Fore.RED}Nenhum subdomínio encontrado.{Fore.RESET}")