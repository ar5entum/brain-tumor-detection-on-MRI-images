# Brain Tumor Detection using PyTorch CNN with Electron Frontend and Flask Backend

![Brain Tumor Detection](screen.png)

## Introduction

This project is an open-source implementation of a Brain Tumor Detection system using a Convolutional Neural Network (CNN) trained on 12,000 MRI scans of the brain. The CNN model is built using the PyTorch framework, and it is integrated with a cross-platform Electron frontend and a Flask backend to create a user-friendly application.

The purpose of this project is to provide a reliable tool for detecting brain tumors in MRI scans, which can aid medical professionals in diagnosing brain-related conditions. The trained model achieves high accuracy in detecting tumors and can be utilized for both research and practical medical purposes.

## Features

- Accurate Brain Tumor Detection: The CNN model is trained on a large dataset of MRI scans, enabling it to accurately detect brain tumors.
- Cross-Platform Electron Frontend: The Electron frontend provides a user-friendly graphical interface, making the application accessible on multiple platforms.
- Python Flask Backend: The Flask backend serves as an API to interact with the CNN model and handle incoming requests from the frontend.
- Easy-to-Use Interface: The application offers a simple and intuitive user interface for uploading MRI scans and obtaining tumor detection results.

## Installation

Follow these steps to set up the Brain Tumor Detection application:

1. Clone the GitHub repository:

   ```
   git clone https://github.com/ar5entum/brain-tumor-detection-on-MRI-images.git
   cd brain-tumor-detection
   ```

2. Set up the Python environment and install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Install Node.js and npm to handle the Electron frontend:

   ```
   # Install Node.js (https://nodejs.org)
   # Verify the installation:
   node -v
   npm -v
   ```

4. Set up the Electron frontend:

   ```
   cd frontend
   npm install
   ```

5. Build the Electron application:
   ```
   npm run build
   ```

## Usage

1. Launch the Electron frontend:

   ```
   npm start
   ```

2. Start the Flask backend API:

   ```
   cd api && export FLASK_APP=main.py && flask run
   ```

3. The Electron application window will open. Use the intuitive interface to upload MRI scans and obtain brain tumor detection results.

## Dataset

The CNN model was trained on a dataset of 12,000 MRI scans of the brain, collected from various sources, including Kaggle. The dataset is not included with this repository due to its large size, but you can obtain a similar dataset from publicly available sources or medical research organizations.

## Contributing

We welcome contributions to enhance the functionality and performance of this project. If you are interested in contributing, please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We would like to express our gratitude to the open-source community, PyTorch, Electron, Flask, and Kaggle for their valuable contributions, which made this project possible.

## Contact

If you have any questions or feedback, please feel free to contact us at [email@example.com](mailto:email@example.com).

---

_Note: Replace `ar5entum` in the GitHub repository URL with the actual username of the project repository owner._
