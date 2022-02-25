import argparse
import base64

parser = argparse.ArgumentParser()
parser.add_argument('--encode', help='File you want to encode.', required=True)
parser.add_argument('-O', help='Output file', required=True)
args = vars(parser.parse_args())

args_encode = args['encode']
args_output = args['O']

try:
    print('    successfully coded')
    print(f'''
    Use remove '
    execute: sed -i "s/'//g" {args_output}
    Use remove [, ', b
    sed -i "s|[[,',b]||g" {args_output}  
    Use remove ]
    sed -i "s|[]]||g" {args_output}
    ''')

    file_encode = open(args_encode, 'r')
    conteudo_encode = file_encode.readlines() #Aqui ele já retorna um em baixo do outro.
    #print(conteudo_encode) #Mostra o que leu na variável acima. Não filtrado.
    arquivo_encodado = open(args_output, 'w')
    for line_encode in conteudo_encode: #Faz o conteúdo do conteudo_encode ficar deitado para ser codificado.
        encode = base64.b64encode(line_encode.encode())#Codificação do base64.
        arquivo_encodado.writelines(str(f'{encode}\n'))#Jogando dentro do arquivo.
except Exception:
    print('Ops!! Try again.')
