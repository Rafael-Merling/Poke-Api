# Project's Objective

This a simple project created with the objective to learn how a ETL project works, since the information fetch from a source (PokeApi)
to loading the project on a target (MinIO). It used the help from pandas package wo it would be possible to use dataframes to help the data
transformation and used a docker as a learning purpose as well


### What was used
- Python 3 programming language
- Local Host MinIO

### How to make this project work
If you want to edit this project, you can clone this repository, and use the pip install on the packages that are inside de "requirements.txt" file

If you want to just execute the project, you need to have the docker installed in your machine, and then use

```
docker build -t pokeapi -f docker/Dockerfile
docker run -d pokeapi
```

Then you just need to execute the docker with a bash command, and then use the following command

```
python3 ./main.py
```
