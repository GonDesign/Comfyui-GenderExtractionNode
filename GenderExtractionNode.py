
class GenderExtraction:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_input": ("STRING", {
                    "multiline": True, 
                    "default": "Input your text here..."
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "extract_gender"

    CATEGORY = "Text Processing"

    def extract_gender(self, text_input):
        import re
        match = re.search(r'\b(1girl|1boy)\b', text_input)
        if match:
            return (match.group(0),)
        else:
            return ("No match found",)


# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "GenderExtraction": GenderExtraction
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "GenderExtraction": "Gender Extraction Node"
}
