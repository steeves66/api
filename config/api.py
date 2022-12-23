from ninja import NinjaAPI

api = NinjaAPI()

#@api.get("/hello")
#def hello(request):
#    return "Hello world"

@api.get("/add")
def add(request, a:int, b:int):
    return {"result": a+b}

@api.get("/hello")
def hello(request, name:str="world"):
    return f"Hello {name}"
