from src.handler.handler import Handler

import sys
import os

module_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(module_dir, "src"))


def main() -> None:
    handler = Handler()

    handler.run()


if __name__ == "__main__":
    main()


# import requests
# import jsondictio
# import pandas as pd

# # First-API-Key: PMAK-6482bb501a49ef7914125b9e-41328798d5a16705954b615aed8626a09e

# url = "https://pokeapi.co/api/v2/pokemon/"

# pokeApi = requests.get(url)


# # print(pokeApi.status_code)
# data = pokeApi.text
# #print(data)
# parse_json = json.loads(data)
# print(parse_json)

# # results = parse_json['results']

# # if (pokeApi.status_code == 200):

# #     print("Poke Api:", parse_json)
# #     with open("PokeApi/output.json", "w") as output:
# #         output.write(json.dumps(pokeApi.json(), indent=4))

# #     print("JSON file created")


# #     df = pd.DataFrame(results)

# #     df.to_csv('PokeApi/output.csv', index=False)

# #     print("CSV file created")
