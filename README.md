# word_b64

Utilitário simples em Python que lê um arquivo de texto (ou wordlist) e codifica cada linha em **Base64**, gravando o resultado em um arquivo de saída.

Útil em cenários de pentest onde a aplicação alvo transmite credenciais ou parâmetros em Base64: permite preparar rapidamente uma wordlist já codificada para uso em fuzzing e testes de autenticação **autorizados**.

## Requisitos

- Python 3 (apenas biblioteca padrão — `argparse`, `base64`)

## Uso

```bash
python3 word_b64.py --encode <arquivo_entrada> -O <arquivo_saida>
```

| Argumento | Descrição |
|-----------|-----------|
| `--encode` | Arquivo de entrada com uma entrada por linha |
| `-O` | Arquivo de saída com as linhas codificadas em Base64 |

### Exemplo

```bash
python3 word_b64.py --encode wordlist.txt -O wordlist_b64.txt
```

O script imprime comandos `sed` opcionais para limpar caracteres residuais (`b'...'`) da saída, caso deseje apenas o valor Base64 puro.

## Aviso

Ferramenta de apoio para **testes de segurança autorizados**. Utilize somente em sistemas próprios ou com permissão formal por escrito.
