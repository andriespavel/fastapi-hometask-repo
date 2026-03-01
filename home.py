from fastapi import FastAPI,Body

app = FastAPI ()

HOME = [
    {'title': 'Kitchen', 'trainer': 'coffee machine', 'function': 'good'},
    {'title': 'Bedroom', 'trainer': 'lamp', 'function': 'broken'},
    {'title': 'Living Room', 'trainer': 'TV', 'function': 'excellent'}
]

@app.get("/home")
async def read_all_home():
    return HOME


@app.get("/home/{home_title}")
async def read_home(home_title: str) :
    for home in HOME:
        if home.get('title') .casefold() == home_title.casefold():
            return home



@app.get("/home/bytrainer/")
async def read_home_by_trainer(trainer: str):
    home_to_return = []
    for home in HOME:
      if home.get('trainer').casefold() == trainer.casefold():
        home_to_return.append(home)

    return home_to_return


@app.post("/home/create_home")
async def create_home(new_home=Body()):
    HOME.append(new_home)


@app.put("/home/update_home")
async def update_home(updated_home=Body()):
        for i in range(len(HOME)):
            if HOME[i].get('title').casefold() == updated_home.get('title').casefold():
                HOME[i] = updated_home


@app.delete("/home/delete_home/{home_title}")
async def delete_home(home_title: str):
    for i in range(len(HOME)):
        if HOME[i].get('title').casefold() == home_title.casefold():
            HOME.pop(i)
            break