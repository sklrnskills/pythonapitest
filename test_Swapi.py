import requests
import pytest
import commonMethods
import pytest_html_reporter

"to install dependencies use the command : pip install -r requirements.txt"
"use the following command to run the tests and get console output as well plus generate html report as well"
"command :  pytest -s --html-report=./report/testReport.html"


@pytest.mark.parametrize("character_type,search_text,expected_result", [('planets', 'tat', 'Tatooine')])
def test_search_people_or_planet(character_type, search_text, expected_result):
    url = commonMethods.get_url('B3')
    payload = {'search': search_text}
    if character_type == 'planets':
        url = url.replace('people', character_type)

    response = requests.get(url, params=payload)
    if response.ok:
        json_response = response.json()
        assert json_response['results'][0]['name'] == expected_result
        assert response.headers['content-type'] == 'application/json'

    else:
        assert False, "wrong status code received from resource"


def test_status_codes():
    url1 = "https://swapi.dev/api/people/1"
    url2 = "https://swapi.dev/api/people/230"
    headers = {"Content-Type": "application/json"}
    dummy_data = """
    {
      "Id": 43215,
      "name": "John Doe",
      "Quantity": 3,
      "Price": 20.00
    }
    """
    assert requests.get(url1).status_code == 200
    assert requests.get(url2).status_code == 404
    assert requests.patch(url1, headers=headers, data=dummy_data).status_code == 405


def test_list_all_character_names():
    url = commonMethods.get_url('B2')

    response = requests.get(url)
    while True:
        if response.status_code == 200:
            json_response = response.json()

            if json_response['next'] is None:
                print("Total StarWars characters = " + str(json_response['count']))
                return
            length = len(json_response['results'])

            for i in range(length):
                print("{} : {}".format(json_response['results'][i]['name'], json_response['results'][i]['gender']))

        response = requests.get(json_response['next'])
