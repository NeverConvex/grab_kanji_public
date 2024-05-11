import os, sys
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = open("google_vision_user_credentials.txt", 'r').readline().strip() # User must add this file themselves
from google.cloud import vision

def pic_to_text(img_path, verbose=True):
    """
        Detects & returns text in an image file via Google Vision API
    """
    client = vision.ImageAnnotatorClient()
    with open(img_path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # NOTE from Google Vision docs: For less dense text, consider changing this to text_detection (vs document_text_detection)
    response = client.document_text_detection(image=image)
    text = response.full_text_annotation.text
    if verbose:
        print(f"From {img_path}, Google Vision OCR extracted text: {text}")
    return text

def test(monitor_index=0, img_type="JPEG"):
    text = pic_to_text(f"test/test{monitor_index}.{img_type.lower()}")
    with open("test/dump.txt", 'a', encoding="utf-8") as of:
        of.write(f"\n{text}")

if __name__ == "__main__":
    print(f"Received command-line args: {sys.argv}")
    monitor_indices = [int(cmd_line_arg) for cmd_line_arg in sys.argv[1:]] if len(sys.argv)>1 else 0
    test(monitor_indices[0]) # TODO generalize to allow for multiple indices? (add a loop in test)
