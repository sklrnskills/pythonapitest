import requests
import pytest
import dataBook
import pytest_html_reporter

"to install dependencies use the command : pip install -r requirements.txt"
"Test run command with report :  pytest -s --html-report=./report/testReport.html"


@pytest.mark.parametrize("type_of_character,find_text,expected_result", [('planets', 'tat', 'Tatooine')])
def test_search_people_or_planet(type_of_character, find_text, expected_result):
    url = dataBook.get_url('B3')
    payload = {'search': find_text}
    if type_of_character == 'planets':
        url = url.replace('people', type_of_character)

    response = requests.get(url, params=payload)
    if response.ok:
        json_response = response.json()
        assert json_response['results'][0]['name'] == expected_result
        assert response.headers['content-type'] == 'application/json'

    else:
        assert False, " the expected response is not received, please check your input "

def test_status_codes():
    url1 = "https://swapi.dev/api/people/1"
    url2 = "https://swapi.dev/api/people/90"
    headers = {"Content-Type": "application/json"}
    dummy_data = """
    {
      "Id": 4321,
      "name": "Kate Winslet",
      "Quantity": 6,
      "Price": 80.00
    }
    """
    assert requests.get(url1).status_code == 200
    assert requests.get(url2).status_code == 404
    assert requests.patch(url1, headers=headers, data=dummy_data).status_code == 405


def test_display_all_characters():
    url = dataBook.get_url('B2')

    response = requests.get(url)
    while True:
        if response.status_code == 200:
            json_response = response.json()

            if json_response['next'] is None:
                print("Total cast of starwars = " + str(json_response['count']))
                return
            length = len(json_response['results'])

            for i in range(length):
                print("{} : {}".format(json_response['results'][i]['name'], json_response['results'][i]['gender']))

        response = requests.get(json_response['next'])
