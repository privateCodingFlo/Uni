import numpy as np


def create_block_matrix(n):
    # Tridiagonalmatrix A erstellen [cite: 30]
    A = 4 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
    # Identitätsmatrix I
    I = np.eye(n)

    # Blockmatrix C aufbauen [cite: 31, 32]
    # Wir erstellen eine Liste von Listen (Blöcken) und nutzen np.block
    blocks = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        blocks[i][i] = A  # Diagonale Blöcke sind A
        if i > 0:
            blocks[i][i-1] = -I  # Untere Neben-Blöcke
        if i < n - 1:
            blocks[i][i+1] = -I  # Obere Neben-Blöcke

    # Fehlende Blöcke mit Nullen füllen
    for i in range(n):
        for j in range(n):
            if blocks[i][j] is None:
                blocks[i][j] = np.zeros((n, n))

    return np.block(blocks)


C = create_block_matrix(5)  # Beispiel für n=5
print("Blockmatrix C Gestalt:", C.shape)
