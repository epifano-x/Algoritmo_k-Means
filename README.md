# K-Means em Processamento de Imagens

Este repositório contém um exemplo de implementação do algoritmo K-Means em imagens, útil para fins de quantização de cores e segmentação de imagens. Este projeto foi desenvolvido como parte da disciplina de Processamento de Imagens e Reconhecimento de Padrões.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas Python instaladas:

- OpenCV (para carregar e exibir imagens)
- Numpy (para manipulação de dados)
- Scikit-learn (para a implementação do algoritmo K-Means)

Você pode instalá-las utilizando o pip:

```
pip install opencv-python numpy scikit-learn
```


## Uso

1. Clone este repositório


2. Coloque sua imagem de entrada na raiz do projeto e atualize o caminho da imagem no código para a sua imagem específica:

```python
# Carregue a imagem
image = cv2.imread('sua_imagem.jpg')

```
3. Execute o script Python:
```
python kmeans_image.py

```
4. A imagem quantizada será exibida na tela.

## Customização

Você pode customizar o número de clusters (variável k) no código para ajustar a quantização de cores conforme necessário.

## Contribuições

Sinta-se à vontade para contribuir para este projeto ou relatar problemas encontrados. Todas as contribuições são bem-vindas!





Divirta-se com a implementação do K-Means em imagens! Se tiver alguma dúvida ou precisar de assistência, sinta-se à vontade para entrar em contato.
