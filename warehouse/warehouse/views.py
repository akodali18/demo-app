import logging
import random
import sys
import time
import requests
from concurrent.futures import ThreadPoolExecutor
from rest_framework.response import Response
from rest_framework.decorators import api_view

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

executor = ThreadPoolExecutor(max_workers=2)


@api_view(http_method_names=["GET"])
def fetch(request, order_num):
    try:
        time.sleep(1)
        if random.randint(1, 1000) == 1000:
            raise RuntimeError("Random Service Unavailable!")
        if not order_num:
            raise ValueError("Invalid Order Num!")
        # executor.submit(async_fetch, tracer.active_span)
        if random.randint(1, 3) == 3:
            requests.get(
                "http://localhost:" + request.META["SERVER_PORT"] + "/check_stock")
        return Response(
            data={"status": "Order:" + order_num + " fetched from warehouse"},
            status=202)
    except RuntimeError:
        return handle_exception(sys.exc_info(), 503)
    except ValueError:
        return handle_exception(sys.exc_info(), 400)

@api_view(http_method_names=["GET"])
def check_stock(request):
    time.sleep(1)
    return Response(status=202)

def handle_exception(exe_info, status_code=None):
    error_msg = str(exe_info[1])
    if error_msg:
        logging.warning(error_msg)
    if not status_code:
        return
    else:
        return Response(error_msg, status=status_code)
