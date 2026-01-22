import logging

logger = logging.getLogger("request")

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info("Request %s %s", request.method, request.path)

        logger.debug("Headers: %s", dict(request.headers))

        if request.method in ("POST", "PUT", "PATCH"):
            try:
                logger.debug("Body: %s", request.body.decode())
            except Exception:
                logger.debug("Body: <cannot decode>")

        response = self.get_response(request)

        logger.info("Response status: %s ------------------------------------------------------------------------------------",
                    response.status_code)
        
        if response.status_code >= 400:
             try:
                 logger.error("Error response: %s", response.content.decode())
             except Exception:
                 logger.error("Error response: <cannot decode>")
                 
        return response
