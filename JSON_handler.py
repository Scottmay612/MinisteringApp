import json

class JSON_handler:
    
    @staticmethod
    def read_file(file_name = "calling_info.json"):
        with open(file_name, "r") as f:
            return json.load(f)


    @staticmethod
    def write_to_file(data, file_name = "calling_info.json"):
        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)
