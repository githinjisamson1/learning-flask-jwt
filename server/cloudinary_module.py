from flask import Flask, render_template, request, jsonify
from cloudinary import CloudinaryUploader, config
from PIL import Image
from io import BytesIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uploads.db'
db = SQLAlchemy(app)

# Cloudinary configuration
config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

# Define the database model


class UploadedFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    cloudinary_public_id = db.Column(db.String(100))


# Create database tables
db.create_all()

# Function to process the image


def process_image(file):
    img = Image.open(file)
    img_resized = img.resize((300, 300))  # Resize the image to 300x300
    img_io = BytesIO()  # Create an in-memory byte stream
    # Save the resized image to the byte stream
    img_resized.save(img_io, format='JPEG')
    img_io.seek(0)  # Reset the byte stream's position to the beginning
    return img_io


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file_to_upload = request.files['file']
        processed_image = process_image(file_to_upload)

        # Upload the processed image to Cloudinary
        uploader = CloudinaryUploader()
        cloudinary_result = uploader.upload(processed_image)

        # Save information about the uploaded file to the database
        uploaded_file = UploadedFile(
            filename=file_to_upload.filename,
            cloudinary_public_id=cloudinary_result['public_id']
        )
        db.session.add(uploaded_file)
        db.session.commit()

        # Return JSON response
        return jsonify(cloudinary_result)


if __name__ == '__main__':
    app.run(debug=True)
