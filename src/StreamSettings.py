import json

class StreamSettings:

    def __init__(self):

        pass

    def get_keywords_from_json(self, filename):

        status = True
        try:
            with open(filename) as file:

                data = json.load(file)

                if data:
                    data = sum(data["keywords"].values(), [])

                else:
                    status = False

        except Exception as e:
            status = False
            data = e


        return status, data

