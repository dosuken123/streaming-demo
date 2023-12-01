# LangChain FastAPI Streaming example

curl example:

```
Shinyas-Air:~ shinya$ curl -v -N -X 'POST' \
>   'http://127.0.0.1:8000/' \
>   -H 'accept: application/json' \
>   -H 'Content-Type: application/json' \
>   -d '{
>   "query": "Can you explain how 1+1 work in math?"
> }'
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1:8000...
* Connected to 127.0.0.1 (127.0.0.1) port 8000 (#0)
> POST / HTTP/1.1
> Host: 127.0.0.1:8000
> User-Agent: curl/8.1.2
> accept: application/json
> Content-Type: application/json
> Content-Length: 54
> 
< HTTP/1.1 200 OK
< date: Fri, 01 Dec 2023 00:21:08 GMT
< server: uvicorn
< transfer-encoding: chunked
< 
 Sure, let me explain how addition with 1+1 works in math:

The plus sign "+" represents the operation of addition. Addition is combining or joining two numbers together to get a total or sum.

So 1+1 means:
- Take the number 1
- Take another instance of the number 1
- Combine these two 1s together
- The result is 2

So when you add 1+1, you are adding one 1 and another 1. Since 1+1=2, the end result of the addition problem 1+1 is the number 2.

The process goes like this:

Start with 1
Add another 1 
The total after joining those two 1 numerals is 2

So in the simplest sense, 1+1=2 just means that one 1 plus an additional 1 makes the number 2. It's a basic math equation to understand the fundamental concept of adding equal numbers or units to get a total amount.* Connection #0 to host 127.0.0.1 left intact
Shinyas-Air:~ shinya$ 
```