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

@api.get("/math")
def math(request, a:int, b:int):
    return {"add": a+b, "multiply": a*b}

@api.get("/math{a}and{b}")
def math2(request, a:int, b:int):
    return {"add":a+b, "multiply":a*b}


