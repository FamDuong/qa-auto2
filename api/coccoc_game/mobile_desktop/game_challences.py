"""
This example shows how to send a reply from the proxy immediately
without sending any data to the remote server.
"""
from mitmproxy import http
import requests

def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.
    dev_api_url = 'https://dev-browser-game-api.coccoc.com/api/v3/public-events-all-games'
    prd_api_url = 'https://browser-game-api.coccoc.com/api/v3/public-events-all-games'
    with requests.Session() as session:
        initial_response = session.get(dev_api_url)
        response = session.get(dev_api_url)
        # print(response.status_code)
    # if format == "json":
    #    api_data = json.loads(response.content)
    #    print(api_data)

    if flow.request.pretty_url.startswith(prd_api_url):
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            response.text,  # (optional) content
            {"Content-Type": "application/json"}  # (optional) headers
        )