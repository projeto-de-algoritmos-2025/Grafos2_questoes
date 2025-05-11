import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        
        # Fila de prioridade (min-heap) para armazenar [tempo, x, y]
        pq = []
        
        # Matriz de visitados
        visited = [[False] * n for _ in range(n)]
        
        # Adiciona a célula inicial (0, 0) na fila com o tempo inicial sendo o valor de grid[0][0]
        heapq.heappush(pq, (grid[0][0], 0, 0))
        visited[0][0] = True
        
        # Direções para movimentação: [cima, baixo, esquerda, direita]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while pq:
            # Remove a célula com o menor tempo atual
            time, x, y = heapq.heappop(pq)
            
            # Se chegamos no destino (n-1, n-1), retorna o tempo acumulado
            if x == n - 1 and y == n - 1:
                return time
            
            # Explora as células adjacentes (4 direções)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Verifica se a nova célula está dentro do grid e ainda não foi visitada
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    
                    # Calcula o tempo necessário para entrar na célula adjacente
                    # É o maior valor entre o tempo atual e a elevação da célula adjacente
                    heapq.heappush(pq, (max(time, grid[nx][ny]), nx, ny))
        
        return -1  # Este ponto nunca será alcançado, pois o grid é garantido como navegável
