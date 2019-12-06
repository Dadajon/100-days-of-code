<img src="https://cdn.svgporn.com/logos/pytorch.svg" align="right" width="15%"/>

# MNIST Classification using a CNN

> IDE

![PyCharm](https://img.shields.io/badge/PyCharm-2019.3%20(Professional%20Edition)-brightgreen)
![PyTorch](https://img.shields.io/badge/PyTorch-1.3.1-red)
![Python](https://img.shields.io/badge/Python-3.7.5-blue)

```python

mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))
mnist_testset = datasets.MNIST(root='./data', train=False, download=True, transform=transforms.Compose([transforms.ToTensor()]))

```

![result](img/data_download.png)

```python
print("Training dataset size: ", len(mnist_trainset))
print("Validation dataset size: ", len(mnist_valset))
print("Testing dataset size: ", len(mnist_testset))
```

![size](img/dataset_size.png)

```python
# visualize data
fig=plt.figure(figsize=(20, 10))
for i in range(1, 6):
    img = transforms.ToPILImage(mode='L')(mnist_trainset[i][0])
    fig.add_subplot(1, 6, i)
    plt.title(mnist_trainset[i][1])
    plt.imshow(img)
plt.show()
```

![mnist](img/mnist.png)

``` python
fig=plt.figure(figsize=(20, 10))
plt.plot(np.arange(1, no_epochs+1), train_loss, label="Train loss")
plt.plot(np.arange(1, no_epochs+1), val_loss, label="Validation loss")
plt.xlabel('Loss')
plt.ylabel('Epochs')
plt.title("Loss Plots")
plt.legend(loc='upper right')
plt.show()
```

![result](https://miro.medium.com/max/2368/1*JMdv-1vZoY_JLmRJo1ZMTQ.png)
![tr_res](img/training.png)