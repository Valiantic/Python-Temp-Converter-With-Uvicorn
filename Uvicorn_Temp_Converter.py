
import uvicorn
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
async def index():
    ret = '''<html>
<body>
    <h1> Temperature Converter Prototype Using Uvicorn </h1>
    <h4> By Steven Madali </h4>
    </hr>
    <h4> Type first the number you want to convert then / c for Celsius / f for Fahrenheit/ k for Kelvin </h4>
    <h4>http://localhost:5000/</h4>
</body>
</html>'''
    return Response(content=ret, media_type="text/html")

@app.get("/{n1}/{conv}")
async def docompute(n1:float, conv:str):
    result = 0
    if conv == 'c':
        result = n1 * 9 / 5 + 32
        message = f"The converted Celsius temperature is equal to {result}°F. Fahrenheit"
        
    elif conv == 'f':
        result = (n1 - 32) * 5 / 9
        message = f"The converted Fahrenheit temperature is equal to {result}°C. Celsius"
    elif conv == 'k':
        result = n1 + 273.5
        message = f"The converted Celsius temperature is equal to {result}°K. Kelvin"
        
    return {"message": message}

if __name__ == "__main__":
    uvicorn.run("Uvicorn_Temp_Converter:app", host="127.0.0.1", port=5000, reload=True)
