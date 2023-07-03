import pandas as pd
from datetime import date


class Parser:
    def __init__(self) -> None:
        print("Starting Parser\n")

        self.control_id = 1

    def parse_data_list(self, data, counter):
        print("Starting parsing list process\n")

        results = data["results"]

        df = pd.DataFrame(results)

        print("Data of page", counter, "parsed, sending to Handler\n")

        return df

    def parse_data_id(
        self, data, endpoint
    ):  # At the moment, specific for pokemon endpoint
        # print(f"Starting process from specific id")

        # df = pd.json_normalize(data)

        output_dict = {}

        id_controller = []

        if endpoint == "pokemon":
            ability_list = []

            pokemon_name = data["name"]  # Pokemon's name

            pokemon_id = data["id"]

            pokemon_base_experience = data["base_experience"]

            pokemon_abilities = data["abilities"]

            # ability_list = self.creating_resource_list(pokemon_abilities,'ability' ,'name')

            # print(pokemon_abilities)

            for ability in pokemon_abilities:
                ability_list.append(ability["ability"]["name"])  # Pokemon's ability
                id_controller.append(self.control_id)
                self.control_id += 1

            output_dict = {
                "id": pokemon_id,
                "name": pokemon_name,
                "base_experience": pokemon_base_experience,
                "abilities": ability_list,
            }

        elif endpoint == "berry":
            flavor_list = []

            berry_name = data["name"]

            berry_id = data["id"]

            berry_growth_time = data["growth_time"]

            berry_flavors = data["flavors"]

            for flavor in berry_flavors:
                flavor_list.append(flavor["flavor"]["name"])
                id_controller.append(self.control_id)
                self.control_id += 1

            output_dict = {
                "id": berry_id,
                "name": berry_name,
                "growth_time": berry_growth_time,
                "flavors": flavor_list,
            }

        # print(output_dict)

        # print(pokemon_name)

        df = pd.DataFrame(output_dict)

        df["_id"] = id_controller
        df["_created_at"] = date.today()

        # df['abilities'] = ','.join(df['abilities'])

        # df = df.drop_duplicates()

        # print(df)

        # print("Returning info to handler\n")

        return df

    def df_to_csv(self, df):
        try:
            csv_file = df.to_csv().encode("utf-8")
            return csv_file
        except:
            print("File is not a DataFrame")

    def appending_dfs(self, df_list):
        df_temp = pd.DataFrame()

        df_temp = pd.concat([df for df in df_list], ignore_index=True)

        return df_temp

    # def creating_resource_list(self, resource_list, resource_key ,item):

    #     resource_final=[]

    #     for resource in resource_list:
    #         resource_final.append(resource[resource_key][item])
