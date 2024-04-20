last_three_frames_categories = []

def get_detected_categories(detection_result):
    '''Return a list of detected object's categoires'''
    detected_categories = []
    for detection in detection_result.detections:
        for category in detection.categories:
            detected_categories.append(category.category_name)
    
    return(detected_categories)


def validate_categories(detected_categories):
    '''Return validated categories when they are kept the same in the last three frames'''
    global last_three_frames_categories
    
    # Add detected categories to the list
    last_three_frames_categories.append(detected_categories)
    
    # Ensure only the last three frames are kept in the list
    if len(last_three_frames_categories) > 3:
        last_three_frames_categories.pop(0)
    
    # Check if categories are the same in the last three frames
    if len(last_three_frames_categories) == 3:
        if all(detected_categories == last_frame_categories for last_frame_categories in last_three_frames_categories[1:]):
            return(detected_categories)
