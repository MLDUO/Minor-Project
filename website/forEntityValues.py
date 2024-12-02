import cv2
import easyocr
from constantsUnits import entity_unit_map
import re

def extract_text_from_image(image_path):
  # Read the image
  img = cv2.imread(image_path)

  # Initialize the EasyOCR reader (English language, no GPU)
  reader = easyocr.Reader(['en'], gpu=False)

  # Detect text in the image
  results = reader.readtext(img)

  # Extract and return only the text part from the results
  extracted_text = [text[1] for text in results]
  return extracted_text

def filter_units_by_entity(extracted_text, entity_name):

  # Get the allowed units for the specified entity (no need for checks since entity_name is always valid)
  allowed_units = entity_unit_map[entity_name]

  # Create a regex pattern to match numbers followed by any allowed unit
  unit_pattern = r'(\d+(\.\d+)?\s*(' + '|'.join(allowed_units) + r'))'
  filtered_values = []

  # Iterate over each text line and apply the regex
  for text in extracted_text:
      matches = re.findall(unit_pattern, text.lower())
      filtered_values.extend([match[0] for match in matches])

  return filtered_values