import requests as req

res = req.get("https://restcountries.eu/data/arg.svg").content

with open("img.svg", "wb") as file:
    file.write(res)