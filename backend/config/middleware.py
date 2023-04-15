import uuid
import logging
from django.conf import settings
import json
from config.env import BACKEND_DIR


class RequestResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger("request-response-logger")

        PATH = BACKEND_DIR / "logs/jobs.log"
        file_handler = logging.FileHandler(PATH, encoding="utf-8")
        self.logger.addHandler(file_handler)

    def __call__(self, request):
        unique_id = str(uuid.uuid4().hex)
        if "/debug" not in request.path:
            # A unique ID is generated for each incoming request
            user = getattr(request, "user", None)
            query_param = request.GET.dict()
            body_param = request.body.decode("utf-8")
            param = body_param or query_param
            # The unique ID is set as an attribute to the thread-local object.
            settings.THREAD_LOCALS.request_id = unique_id
            self.logger.info(
                f"******** REQUEST DETAILS ********\nPATH:= {request.method}\nUSER:= {user}\n{request.get_full_path()}\nBODY:={param}"
            )

        response = self.get_response(request)
        response["X-Log-ID"] = unique_id

        if response.status_code != 500:
            if getattr(response, "data", None) is not None:
                self.logger.info(
                    f"******** RESPONSE DETAILS ********\nSTATUS:= {response.status_code}\nBODY:= {json.dumps(response.data, indent=4, default=str)}"
                )

        return response
