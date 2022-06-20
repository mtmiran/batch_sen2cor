### Preprocessamento de imagens sentine2

## Importando bibliotecas
import os

## Sen2cor

#  criar lista com nome das pastas sentinel2
lista_sentinel = [pasta for pasta in os.listdir()]

# executar sen2cor em loop na lista com nome das pastas sentinel2
for img in lista_sentinel:
    if "MSIL2A" not in img:
        sen2cor = f"Sen2Cor\\L2A_Process.bat {img}"
        os.system(sen2cor)
        print(f'### Imagem {img} corrigida ###')
