import json


def response(flow):
    res = flow.response
    headers = flow.request.headers
    cookies = flow.request.cookies
    query = flow.request.query
    data = res.text

    request_query = {k: v for k, v in flow.request.query.items()}
    request_headers = {k: v for k, v in flow.request.headers.items()}
    response_headers = {k: v for k, v in flow.response.headers.items()}
    # print(request_headers)
    # print(data)

    payload = {"query": request_query, "headers": request_headers}

    try:
        v = request_query["v"]
        if v == "0":
            with open("header.json", 'w') as file:
                file.write(json.dumps(payload, indent=2))
            print("get header")
    except:
        pass
