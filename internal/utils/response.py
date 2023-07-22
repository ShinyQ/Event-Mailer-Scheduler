HttpStatus = {
    200: {"code": 200, "message": "OK"},
    201: {"code": 201, "message": "Created"},
    400: {"code": 400, "message": "Bad request"},
    401: {"code": 401, "message": "Unauthorized"},
    404: {"code": 404, "message": "Not found"},
    500: {"code": 500, "message": "Internal server error"},
}


def response_json(result, status_code, message=None):
    status_obj = HttpStatus.get(status_code)
    response_object = {
        "code": status_obj["code"],
        "message": message or status_obj["message"],
        "result": result,
    }

    return response_object
