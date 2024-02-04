import requests
API_KEY = "6a9aa6800c30e9afa96b01eec1d7c35274f040f710eda0c7563362157196cf62"


def scan_file(api_key, file_path):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': api_key}
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (file_path, file)}
            response = requests.post(url, files=files, params=params)
    except Exception:
        return False

    return response.json()


def get_report(api_key, resource):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': api_key, 'resource': resource}
    response = requests.get(url, params=params)
    try:
        return response.json()
    except Exception:
        return False


def start(file_path):
    scan_result = scan_file(API_KEY, file_path)
    if scan_result:
        resource = scan_result['resource']
        report_result = get_report(API_KEY, resource)
        return report_result
    else:
        return False
