const axios = require('axios');
const fs = require('fs');
const FormData = require('form-data');

// Function to read the file as a buffer
function readFileAsBuffer(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}

async function makePrediction() {
  try {
    const fileBuffer = await readFileAsBuffer('test_images/N.jpg');
    const formData = new FormData();
    formData.append('file', fileBuffer, {
      filename: 'N.jpg',
    });

    const response = await axios.post(
      'http://localhost:5000/predict',
      formData,
      {
        headers: formData.getHeaders(),
      }
    );

    console.log(response.data);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

makePrediction();
