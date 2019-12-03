<img src="https://cdn.svgporn.com/logos/pytorch.svg" align="right" width="15%"/>

# MNIST Classification using a CNN

> IDE

![PyCharm](https://img.shields.io/badge/PyCharm-2019.2.5%20(Professional%20Edition)-brightgreen)
![PyTorch](https://img.shields.io/badge/PyTorch-1.3.1-red)
![Python](https://img.shields.io/badge/Python-3.7.5-blue)

```python

mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))
mnist_testset = datasets.MNIST(root='./data', train=False, download=True, transform=transforms.Compose([transforms.ToTensor()]))

```

![result](img/data_download.png)
