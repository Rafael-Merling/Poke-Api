from src.service.service import Service
from src.parser.parser import Parser
from src.loader.loader import Loader


class Handler:
    def __init__(self) -> None:
        print("Process started!\n")

    def run(self):
        endpoint = "pokemon"

        service = Service(
            base_url="https://pokeapi.co/api/v2/", endpoint=endpoint, limit=150
        )

        parser = Parser()

        loader = Loader(
            endpoint="127.0.0.1:9000", secret_key="minioadmin", access_key="minioadmin"
        )

        # base_url= 'https://pokeapi.co/api/v2/'

        # url = service.mountURL(const_url=const_url,endpoint='pokemon',limit=151)
        # service.mountURL(const_url=const_url,
        #                       endpoint='pokemon', limit=151)

        # print(url)

        page_counter = 1

        print(("Starting fetching process.\n"))

        while data := service.fetch(url=service.url):
            id_counter = 1

            print("Loading data from Handler's url\n")

            print("Fetching data from page", page_counter, "\n")

            # while(url is not None):

            # data = service.fetch(url=url)

            if "results" in data:
                df_list = []

                json_file = data["results"]
                print("Getting specific ids of page", page_counter)
                for key in json_file:
                    print("Loading from id", id_counter)
                    id_counter += 1
                    key_url = service.set_url(
                        url=key["url"]
                    )  # Using a URL inside the JSON file to preserve the original url on the service class
                    data_id = service.fetch(url=key_url, page=False)

                    # print(data_id)
                    df = parser.parse_data_id(data=data_id, endpoint=endpoint)
                    df_list.append(df)

                    if id_counter == 10:
                        break

                    # print(df)
                    # print('\n')
                    # loader.load_df(df=df,file_name=key['name'])

                print("All the data was fetched, returning to Handler\n")

                # print(df_list[0])

                df_final = parser.appending_dfs(df_list)

                # print(df_final)

                df_csv = parser.df_to_csv(df_final)

                loader.load_df(
                    df=df_csv,
                    folder_name=endpoint,
                    file_name=f"pokemons_and_abilities {page_counter}",
                )

            else:
                print("All the data was fetched\n")
                print("Raw data received, sending to Parser\n")
                # df = parser.parse_data(data=data, counter=counter)
                df = parser.parse_data_list(data=data, counter=page_counter)
                # loader.load_df(df=df, file_name=f'pokemon{page_counter}')

            print("Formatted data received, sending to Loader\n")

            page_counter += 1

            # loader.load_df(df=df, counter=page_counter)

        else:
            print("All pages fetched\n")

        print("Process finished\n")
