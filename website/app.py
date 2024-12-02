import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageOps
from tensorflow.keras.models import load_model
from forEntityValues import extract_text_from_image, filter_units_by_entity

entity_names = ['item_volume', 'item_weight', 'depth', 'height', 'width', 'wattage', 'voltage']

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model
model = load_model(r"\website\savedModel\model22f.keras")

# Ensure the static/images directory exists
UPLOAD_FOLDER = r'\website\static\images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to preprocess the image
def preprocess_image(img_path):
    img = Image.open(img_path).convert('L')  # Convert to grayscale
    img = ImageOps.invert(img)  # Invert the grayscale image
    img = img.resize((512, 512))  # Resize to 512x512 pixels   
    # Convert grayscale to RGB (repeat the single grayscale channel across three channels)
    img_rgb = img.convert("RGB")
    
    imgPixel = np.array(img_rgb) / 255.0
    # Reshape the image for model input (1, 512, 512, 3)
    imgPixelReshaped = imgPixel.reshape(1, 512, 512, 3) #the saved model uses image input of 3 channel (color) hence, third dimension is added
    return imgPixelReshaped, imgPixel   # Return the processed array and 2D original pixel array

# Function to predict the digit
def predict_entity(img_path):
    img_array, processed_image = preprocess_image(img_path)
    prediction = model.predict(img_array)
    # Since the prediction is one-hot encoded, we need to map it to the entity
    predicted_class_index = np.argmax(prediction)  # Find the index of the highest probability
    print(f"\n\n {predicted_class_index} \n\n") #for debugging
    print(f"\n\n {prediction} \n\n")
    # Map the index to the entity name
    predicted_entity = entity_names[predicted_class_index]
    return predicted_entity, processed_image



# Route for the home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if an image file was uploaded
        if "image" not in request.files:
            return redirect(request.url) #if image not found go back to home page
        
        file = request.files["image"]
        
        if file.filename == "":
            return redirect(request.url) # no empty is accepted
        
        if file:
            img_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(img_path)
            
            print(f"Image saved at: {img_path}")
            relative_img_path = 'images/' + file.filename  
            
            predicted_entity, _ = predict_entity(img_path) #returns entity name prediction, and reshaped image pixel array

            #For text detection
            extracted_text = extract_text_from_image(img_path)

            filtered_values = filter_units_by_entity(extracted_text, predicted_entity) #predicted entity as parameter for filtering
            
            # Display the result
            return render_template("index.html", predicted_entity=predicted_entity,filtered_values=filtered_values, img_path=relative_img_path)
    
    return render_template("index.html", predicted_entity=None,  filtered_values=None, img_path=None) #default home page initially

if __name__ == "__main__":
    app.run(debug=True)
