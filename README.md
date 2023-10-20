# ovisgs

Ovisgs é uma ferramenta simples para encontrar subdomínios de um site-alvo.

## Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/K1R4-H4CK3R/ovisgs.git
cd ovisgs
```

2. Instale as dependências usando `pip`:

```bash
pp install -r requirements.txt
```

3. Execute o script:

```bash
python ovisgs.py
```
4. Siga as instruções na tela para inserir o site-alvo (com HTTP ou HTTPS) e o caminho para o arquivo de lista de palavras.

5. Aguarde enquanto o script procura subdomínios.

6. Os subdomínios encontrados serão exibidos na saída.

## Requisitos

- Python 3.x
- Módulo `dns.resolver`
- Módulo `requests`
- Módulo `colorama`

## Contribuindo

Sinta-se à vontade para contribuir para este projeto. Basta criar um fork, fazer as alterações e enviar um pull request.

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.