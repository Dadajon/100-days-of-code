import matplotlib.pyplot as plt
import numpy as np
import torch
import torchvision.datasets as datasets
from torchvision import transforms

from model import Model

mnist_train = datasets.MNIST(root='./data', train=True, download=True,
                             transform=transforms.Compose([transforms.ToTensor()]))
mnist_test = datasets.MNIST(root='./data', train=True, download=True,
                            transform=transforms.Compose([transforms.ToTensor()]))

mnist_valid, mnist_test = torch.utils.data.random_split(mnist_test,
                                                        [int(0.9 * len(mnist_test)), int(0.1 * len(mnist_test))])

train_dataloader = torch.utils.data.DataLoader(mnist_train, batch_size=64, shuffle=True)
valid_dataloader = torch.utils.data.DataLoader(mnist_valid, batch_size=32, shuffle=False)
test_dataloader = torch.utils.data.DataLoader(mnist_test, batch_size=32, shuffle=False)

print("Training dataset size: {}".format(len(mnist_train)))
print("Validation dataset size: {}".format(len(mnist_valid)))
print("Test dataset size: {}".format(len(mnist_test)))

# visualize data
fig = plt.figure(figsize=(20, 10))
for i in range(1, 6):
    img = transforms.ToPILImage(mode='L')(mnist_train[i][0])
    fig.add_subplot(1, 6, i)
    plt.title(mnist_train[i][1])
    plt.imshow(img)
plt.show()

model = Model()
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

if torch.cuda.is_available():
    model.cuda()

no_epochs = 100
train_loss = list()
val_loss = list()
best_val_loss = 1
for epoch in range(no_epochs):
    total_train_loss = 0
    total_val_loss = 0

    model.train()
    # training
    for itr, (image, label) in enumerate(train_dataloader):
        if torch.cuda.is_available():
            image = image.cuda()
            label = image.cuda()

        optimizer.zero_grad()

        pred = model(image)

        loss = criterion(pred, label)
        total_train_loss += loss.item()

        loss.backward()
        optimizer.step()

    total_train_loss = total_train_loss / (itr + 1)
    train_loss.append(total_train_loss)

    # validation
    model.eval()
    total = 0
    for itr, (image, label) in enumerate(valid_dataloader):
        if torch.cuda.is_available():
            image = image.cuda()
            label = label.cuda()

        pred = model(image)

        loss = criterion(pred, label)
        total_val_loss += loss.item()

        pred = torch.nn.functional.softmax(pred, dim=1)
        for i, p in enumerate(pred):
            if label[i] == torch.max(p.data, 0)[1]:
                total = total + 1

    accuracy = total / len(mnist_valid)

    total_val_loss = total_val_loss / (itr + 1)
    val_loss.append(total_val_loss)

    print("\nEpoch: {}/{}, Train Loss: {:.8f}, Val Loss: {:.8f}, Val Accuracy: {:.8f}".format(epoch + 1, no_epochs,
                                                                                              total_train_loss,
                                                                                              total_val_loss, accuracy))

    if total_val_loss < best_val_loss:
        best_val_loss = total_val_loss
        print("Saving the model state dictionary for Epoch: {} with Validation loss: {:.8f}".format(epoch + 1,
                                                                                                    total_val_loss))

fig = plt.figure(figsize=(20, 10))
plt.plot(np.arange(1, no_epochs + 1), train_loss, label="Train Loss")
plt.plot(np.arange(1, no_epochs + 1), val_loss, label="Validation Loss")
plt.xlabel("Loss")
plt.ylabel("Epochs")
plt.title("Loss Plots")
plt.legend(loc="upper right")
plt.show()
plt.savefig("loss.png")

# test model
model.load_state_dict(torch.load("model.dth"))
model.eval()

results = list()
total = 0
for itr, (image, label) in enumerate(test_dataloader):
    if torch.cuda.is_available():
        image = image.cuda()
        label = label.cuda()

    pred = model(image)
    pred = torch.nn.functional.softmax(pred, dim=1)

    for i, p in enumerate(pred):
        if label[i] == torch.max(p.data, 0)[1]:
            total += 1
            results.append((image, torch.max(p.data, 0)[1]))

test_accuracy = total / (itr + 1)
print("Test accuracy: {:.8f}".format(test_accuracy))


# visualize results
fig = plt.figure(figsize=(20, 10))
for i in range(1, 11):
    img = transforms.ToPILImage(mode="L")(results[i][0].squeeze(0).detach().cpu())
    fig.add_subplot(2, 5, i)
    plt.title(results[i][1].item())
    plt.imshow(img)
plt.show()
plt.savefig("test.png")
