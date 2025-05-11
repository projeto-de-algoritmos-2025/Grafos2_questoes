import heapq
import sys

class Solution:
    def secondMinimum(self, n, edges, tempo, mudancas):
        from collections import defaultdict

        # Construindo o grafo como lista de adjacência
        grafo = defaultdict(list)
        for u, v in edges:
            grafo[u].append(v)
            grafo[v].append(u)

        # Inicializa tempos (duas menores chegadas por nó)
        tempos = [[sys.maxsize, sys.maxsize] for _ in range(n + 1)]
        tempos[1][0] = 0

        # Fila de prioridade (tempo, nó)
        fila = [(0, 1)]

        while fila:
            temp, no = heapq.heappop(fila)

            for vizinho in grafo[no]:
                proximo_tempo = temp

                # Ajusta pelo semáforo
                if (proximo_tempo // mudancas) % 2 == 1:
                    proximo_tempo += mudancas - (proximo_tempo % mudancas)

                proximo_tempo += tempo

                # Atualiza o tempo do vizinho
                if proximo_tempo < tempos[vizinho][0]:
                    tempos[vizinho][1] = tempos[vizinho][0]
                    tempos[vizinho][0] = proximo_tempo
                    heapq.heappush(fila, (proximo_tempo, vizinho))
                elif tempos[vizinho][0] < proximo_tempo < tempos[vizinho][1]:
                    tempos[vizinho][1] = proximo_tempo
                    heapq.heappush(fila, (proximo_tempo, vizinho))

        return -1 if tempos[n][1] == sys.maxsize else tempos[n][1]
