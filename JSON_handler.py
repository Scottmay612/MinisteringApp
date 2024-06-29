import json
from datetime import date, time, datetime

class JSON_handler:
    
    # Read file contents.
    @staticmethod
    def read_file(file_name = "calling_info.json"):
        with open(file_name, "r") as f:
            return json.load(f)


    # Write new info to the file.
    @staticmethod
    def write_to_file(data, file_name = "calling_info.json"):

        serialized_data = JSON_handler.serialize_dates(data)
        serialized_data = JSON_handler.serialize_times(serialized_data)

        with open(file_name, "w") as f:
            json.dump(serialized_data, f, indent=4)

    # Serialize the meeting dates so that they can be written cleanly to a file.
    # Chat GPT created this function for me and I modified it slightly.
    @staticmethod
    def serialize_dates(data):
        serialized_data = []
        for item in data:
            serialized_item = item.copy()
            if 'meeting_date' in serialized_item and isinstance(serialized_item['meeting_date'], date):
                serialized_item['meeting_date'] = datetime.strftime(serialized_item['meeting_date'], "%m-%d-%Y")
            serialized_data.append(serialized_item)
        return serialized_data
    
    # Serialize the meeting times so that they can be written cleanly to a file.
    # Chat GPT created this function for me and I modified it slightly.
    @staticmethod
    def serialize_times(data):
        serialized_data = []
        for item in data:
            serialized_item = item.copy()
            if 'meeting_time' in serialized_item and isinstance(serialized_item['meeting_time'], time):
                serialized_item['meeting_time'] = serialized_item['meeting_time'].strftime("%I:%M %p")
            serialized_data.append(serialized_item)
        return serialized_data
    
    # Turn the serialized times back into time objects.
    def deserialize_times(time_str):
        time_object = datetime.strptime(time_str, "%I:%M %p").time()
        return time_object
    
    # Turn the serialized dates back into date objects.
    def deserialize_dates(date_str):
        date_object = datetime.strptime(date_str, "%m-%d-%Y").date()

        return date_object
