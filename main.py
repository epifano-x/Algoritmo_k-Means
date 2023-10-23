import cv2
import numpy as np
from sklearn.cluster import KMeans

# Carregando a imagem
image = cv2.imread('sua_imagem.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convertendo para o espaço de cores RGB

# Redimensionando a imagem para um array 2D de pixels
h, w, _ = image.shape
image_2d = image.reshape((h * w, 3))

# Número de clusters (k)
k = 2

# Inicializando o modelo K-Means
kmeans = KMeans(n_clusters=k)

# Aplicando o algoritmo K-Means aos dados
kmeans.fit(image_2d)

# Obtendo os centróides dos clusters
centroids = kmeans.cluster_centers_

# Atribuindo a cada pixel o centróide mais próximo
labels = kmeans.predict(image_2d)

# Recriando a imagem segmentada com base nos centróides
segmented_image = centroids[labels].reshape((h, w, 3))

# Convertendo a imagem de volta para o espaço de cores BGR
segmented_image = segmented_image.astype(np.uint8)  # Garantindo que a profundidade seja de 8 bits por canal
segmented_image = cv2.cvtColor(segmented_image, cv2.COLOR_RGB2BGR)


# Mostrando a imagem original e a imagem segmentada
#cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem Segmentada', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
