# this module supply the virustotal feature in the code, interacting with the virustotal api using the requests module
import requests
_API_KEY = "6a9aa6800c30e9afa96b01eec1d7c35274f040f710eda0c7563362157196cf62"


# upload the file to the virustotal server and ask to scan it
def _scan_file(api_key: str, file_path: str) -> bool | dict:
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': api_key}
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (file_path, file)}
            response = requests.post(url, files=files, params=params)
    except Exception:
        return False

    return response.json()


# get the file scan from the virustotal api
def _get_report(api_key: str, resource: any) -> bool | dict:
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': api_key, 'resource': resource}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception:
        return False


# the logic of the handler
def start(file_path: str) -> bool | dict:
    scan_result = _scan_file(_API_KEY, file_path)
    if scan_result:
        resource = scan_result['resource']
        report_result = _get_report(_API_KEY, resource)
        return report_result
    else:
        return False
