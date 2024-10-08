import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\bin\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 18'
preset = '-preset medium'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = ''

class Conversor:
    def __init__(self ,origem="",destino="", formato = '', formatoInput = ''):
        self.origem = origem
        self.destino = destino
        self.formato = formato
        self.formatoInput = formatoInput

    def ExecultaConversao(self):
        try:
            for raiz, pastas, arquivos in os.walk(self.origem):
                for arquivo in arquivos:
                    if not fnmatch.fnmatch(arquivo, '*.'+ self.formatoInput):
                        continue

                    caminho_completo = os.path.join(raiz, arquivo)
                    nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
                    caminho_legenda = nome_arquivo + '.srt'

                    if os.path.isfile(caminho_legenda):
                        input_legenda = f'-i "{caminho_legenda}"'
                        map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
                    else:
                        input_legenda = ''
                        map_legenda = ''

                    nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

                    nome_novo_arquivo = nome_arquivo + '_Convertido' + self.formato
                    arquivo_saida = os.path.join(self.destino, nome_novo_arquivo)

                    comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
                        f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
                        f'{debug} {map_legenda} "{arquivo_saida}"'

                    os.system(comando)
        except Exception:
            sys.exit()
    