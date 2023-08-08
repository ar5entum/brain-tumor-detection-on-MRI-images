import io
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import torch.nn.functional as F

# load model

class Net(nn.Module):
    def __init__(self, num_classes=4):
        super(Net, self).__init__()
        # Convolutional layers
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)

        # Max pooling layers
        self.pool = nn.MaxPool2d(2, 2)

        # Fully connected layers
        self.fc1 = nn.Linear(128 * 32 * 32, 256)
        self.fc2 = nn.Linear(256, 128)

        # Output layer
        self.fc3 = nn.Linear(128, num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = F.relu(self.conv3(x))
        x = self.pool(x)

        # Flatten the feature maps
        x = x.view(-1, 128 * 32 * 32)

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x

model = Net()

PATH = "api/weights.pth"
device = torch.device('cpu')
model.load_state_dict(torch.load(PATH, map_location=device))
model.eval()

# image -> tensor
def get_prediction(image_path):
  transform = transforms.Compose([
      transforms.Grayscale(num_output_channels=1),
      transforms.Resize(256),
      transforms.RandomCrop(256),
      transforms.ToTensor(),
      transforms.Normalize((.1307), (.3081)),
  ])

  image = Image.open(image_path)
  image = transform(image)

  # predict
  outputs = model(image)
      # max returns (value ,index)
  _, predicted = torch.max(outputs.data, 1)

  return predicted
