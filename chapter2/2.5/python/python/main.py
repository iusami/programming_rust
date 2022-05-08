from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get("/", response_class=HTMLResponse)
async def get_index():
    data = """
    <title>GCD Calculator</title>
        <form action="/gcd" method="post">
            <input type="text" name="n" />
            <input type="text" name="m" />
            <button type="submit">Compute GCD</button>
        </form>
    """
    return data

@app.post("/gcd", response_class=HTMLResponse)
async def compute_gcd(n: int = Form(...), m: int = Form(...)):
    result = await gcd(n, m)
    data = f"""The greatest common divisor of the numbers {n} and {m} \
                is <b>{result}</b>\n)
            """
    return data

async def gcd(n: int, m: int) -> int:
    assert (n != 0) & (m != 0), "n and m must be non-zero"
    while m != 0:
        if m < n :
            t = m
            m = n
            n = t
        m = m % n
    return n