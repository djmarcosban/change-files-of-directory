# Esse script move arquivos de dentro de pastas extras dos diretórios "dirs" para os próprios diretórios "dirs"
# Essa forma de armazenar arquivos é do oriunda do wordpress onde estava sendo armazenado arquivos não somente em ano/dia/ mas em ano/dia/hora_minuto_segundo/
# Essa organização conflitava com os links permanentes de cada imagem no banco de dados

from msilib import Directory
from pathlib import Path
import shutil
import os

# Foi setado pastas específicas para não conflitar com outros tipos de pastas de plugins
dirs = ['./uploads/2020/04', './uploads/2020/05', './uploads/2020/06', './uploads/2020/07', './uploads/2020/08', './uploads/2020/09', './uploads/2020/11', './uploads/2020/12', './uploads/2021/01', './uploads/2021/02', './uploads/2021/03', './uploads/2021/04', './uploads/2021/05', './uploads/2021/06', './uploads/2021/07', './uploads/2021/08', './uploads/2021/09', './uploads/2021/10', './uploads/2021/11', './uploads/2021/12', './uploads/2022/01', './uploads/2022/02', './uploads/2022/03', './uploads/2022/04', './uploads/2022/05', './uploads/2022/06', './uploads/2022/07']

# para cada diretorio
for d in dirs:

    #verifica se o diretorio existe
    if os.path.exists(d):
        
        print('Executing in ' + d)
        # acessa o diretorio em questao
        files = os.listdir(d)

        # para cada caminho dentro do diretorio em questao...
        for path in files:

            # concatena o caminho atual para manipulação futura
            fulldir = os.path.join(d, path)

            # verifica se o caminho é uma pasta
            if os.path.isdir(fulldir):

                # acessa o diretorio de imagens /hora_minuto_segundo/
                imagepaths = os.listdir(os.path.join(d, path))
                
                # para cada imagem no direitorio...
                for img in imagepaths:
                    archive = d + '/' + path + '/' + img
                    destiny = Path(d + '/' + img)

                    # se não existir uma imagem no diretorio destino
                    if not destiny.exists():
                        print('Moving ' + archive + ' to ' + d)
                        # move a imagem para o diretorio destino
                        # poderia ser usado a função "copy2" ao invés de "move" para sobrescrever um arquivo existente no destino final
                        # para isso, a condicional acima não precisaria ser usada
                        shutil.move(archive, d)
                    else:
                        print('Can not to move because the file already exists')

                # verifica se o diretorio de imagens /hora_minuto_segundo/ já está vazio
                if(len(os.listdir(fulldir))) == 0:

                    # remove o diretorio de imagens /hora_minuto_segundo/
                    os.rmdir(fulldir)
                    print('Removing ' + fulldir)
                else:
                    print('Can not remove path because is not empty')
            # else:
            #     print('is not path ' + path)

print('Finished')