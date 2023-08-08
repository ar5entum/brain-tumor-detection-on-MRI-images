from flask import Flask, request, jsonify

from  torch_utils import get_prediction

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    # xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

idx_to_class = {
    0: "Normal",
    1: "Glioma Tumor",
    2: "Meningioma Tumor",
    3: "Pituitary Tumor"
}

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error': 'no file'})
        if not allowed_file(file.filename):
            return jsonify({'error': 'format not supported'})

        try:
            prediction = get_prediction(file)
            data = {'prediction': prediction.item(), 'class_name': idx_to_class[prediction.item()]}
            return jsonify(data)
        except:
            return jsonify({'error': 'error during prediction'})
if __name__ == "__main__":
    app.run()