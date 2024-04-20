

def get_detected_categories(detection_result):
    '''Return a list of detected object's categoires'''
    detected_categories = []
    for detection in detection_result.detections:
        for category in detection.categories:
            detected_categories.append(category.category_name)
    
    return(detected_categories)