import requests


class Service:
    def __init__(self, base_url, endpoint, offset=0, limit=0) -> None:
        print("Starting Service\n")

        self.url = f"{base_url}/{endpoint}/"

        self.payload = {"offset": offset, "limit": limit}

    def fetch(self, url, page=True):
        # print("Loading data from Handler's url\n")
        # request_api = requests.get(url)
        request_api = requests.get(
            f"{url}", params=self.payload
        )  # --> passar o param de self

        json_data = (
            request_api.json()
        )  # Getting the data as a real json, used to know if has a next field and send to Parser

        # print("All the data was fetched, returning to Handler\n")

        # self.payload["offset"] = json_data['next']
        if page == True:
            self.payload["offset"] += self.payload["limit"]

        if "results" not in json_data or json_data["results"] != []:
            return json_data

        else:
            return False

    # def fetchNextPage(self, json_file):

    #     return json_file['next']

    def mount_request(
        self, endpoint_id=None, offset=0, limit=None
    ):  # Creating url based on the endpoint desired
        if endpoint_id is not None:
            # self.url = f'{base_url}/{endpoint}/{endpoint_id}/'
            url_pokemon = f"{self.url}/{endpoint_id}"
            return url_pokemon

        # self.payload = {
        #     "offset": offset,
        #     "limit": limit
        # }

    def set_url(
        self, url
    ):  # Function to use a fixed url, useful if the source is coming from a json file
        temp_url = url

        return temp_url
