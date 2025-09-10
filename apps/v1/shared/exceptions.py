from drf_standardized_errors.handler import exception_handler as dre_handler
from rest_framework.views import exception_handler as drf_handler
from rest_framework.response import Response


def json_api_exception_handler(exc, context):
    print("Custom exception handler active")

    response = dre_handler(exc, context) or drf_handler(exc, context)
    if response is None:
        return None

    raw_data = response.data
    errors = []

    if isinstance(raw_data, dict) and "errors" in raw_data:
        for err in raw_data["errors"]:
            error_obj = {
                "status": str(response.status_code),
                "code": err.get("code", "error"),
                "detail": err.get("detail", "An error occurred."),
            }
            if err.get("attr"):
                error_obj["source"] = {"pointer": f"/data/attributes/{err['attr']}"}
            errors.append(error_obj)

    elif "detail" in raw_data:
        errors.append({
            "status": str(response.status_code),
            "detail": raw_data["detail"],
        })

    # 🚨 This line is key — don’t wrap twice
    return Response(errors, status=response.status_code)
