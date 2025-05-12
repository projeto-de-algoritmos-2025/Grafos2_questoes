from typing import List

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        class ConjuntoDisjunto:
            def __init__(self):
                self.pai = {}
                self.classificacao = {} 
                self.contagem_valor = {} 

            def encontrar(self, u):
                if self.pai[u] != u:
                    self.pai[u] = self.encontrar(self.pai[u])
                return self.pai[u]

            def unir(self, u, v):
                raiz_u = self.encontrar(u)
                raiz_v = self.encontrar(v)
                
                if raiz_u == raiz_v:
                    return
                
                if self.classificacao[raiz_u] > self.classificacao[raiz_v]:
                    self.pai[raiz_v] = raiz_u
                    self.contagem_valor[raiz_u] += self.contagem_valor[raiz_v]
                else:
                    self.pai[raiz_u] = raiz_v
                    self.contagem_valor[raiz_v] += self.contagem_valor[raiz_u]
                    if self.classificacao[raiz_u] == self.classificacao[raiz_v]:
                        self.classificacao[raiz_v] += 1

        n = len(vals)
        lista_adj = [[] for _ in range(n)]
        
        for u, v in edges:
            lista_adj[u].append(v)
            lista_adj[v].append(u)
        
        from collections import defaultdict
        nos_por_valor = defaultdict(list)
        for i in range(n):
            nos_por_valor[vals[i]].append(i)
        valores_ordenados = sorted(nos_por_valor.keys())
        
        dsu = ConjuntoDisjunto()
        resposta = 0
        
        for valor_atual in valores_ordenados:
            nos_atuais = nos_por_valor[valor_atual]
            
            for no in nos_atuais:
                if no not in dsu.pai:
                    dsu.pai[no] = no
                    dsu.classificacao[no] = 1
                    dsu.contagem_valor[no] = 1 
            
            for no in nos_atuais:
                for vizinho in lista_adj[no]:
                    if vals[vizinho] > valor_atual:
                        continue
                    if vizinho not in dsu.pai:
                        continue
                    
                    dsu.unir(no, vizinho)
            
            contador = defaultdict(int)
            for no in nos_atuais:
                raiz = dsu.encontrar(no)
                contador[raiz] += 1
            
            for qtd in contador.values():
                resposta += qtd * (qtd + 1) // 2
        
        return resposta