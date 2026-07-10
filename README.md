# word_b64

Um utilitário simples em Python. Ele lê um arquivo de texto ou uma wordlist e codifica cada linha em Base64, gravando o resultado num arquivo de saída.

Serve bem quando a aplicação alvo manda credenciais ou parâmetros em Base64. Você prepara a wordlist já codificada e usa em fuzzing e testes de autenticação autorizados.

## Requisitos

Python 3. Usa só a biblioteca padrão, com argparse e base64.

## Uso

```bash
python3 word_b64.py --encode arquivo_entrada -O arquivo_saida
```

O `--encode` recebe o arquivo de entrada, uma entrada por linha. O `-O` é o arquivo de saída com as linhas já em Base64.

Exemplo:

```bash
python3 word_b64.py --encode wordlist.txt -O wordlist_b64.txt
```

O script ainda imprime uns comandos sed opcionais para limpar caracteres residuais da saída, caso você queira só o valor Base64 puro.

## Aviso

Ferramenta de apoio para testes de segurança autorizados. Use só em sistemas seus ou com permissão formal por escrito.
