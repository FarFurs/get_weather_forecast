import requests


def main() -> None:
    url_template = 'http://wttr.dvmn.org/{}'
    params = {"MnqT": "", "lang": "ru"}
    locations = ['svo', 'london', 'Cherepovets']
    for location in locations:
        try:
            response = requests.get(
                                    url_template.format(location),
                                    params=params
                                    )
            response.raise_for_status()
            print(response.text)
        except ConnectionError:
            print(response.status_code)


if __name__ == '__main__':
    main()
