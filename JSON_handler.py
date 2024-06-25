class JSON_handler():
    
    @staticmethod
    def read_file(file_name = "calling_info.json"):
        with open(file_name, "r") as f:
            f.read()
