import statistics

def analisar_tempo_execucao(arquivo):
    with open(arquivo, 'r') as f:
        tempos = [float(linha.strip()) for linha in f if linha.strip()]

    media = statistics.mean(tempos)
    desvio_padrao = statistics.stdev(tempos)

    print(f"Média do tempo de execução: {media:.2f} segundos")
    print(f"Desvio padrão: {desvio_padrao:.2f} segundos")

analisar_tempo_execucao('log.txt')
