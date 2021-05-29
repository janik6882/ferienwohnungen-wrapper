import json
import requests


class Ferienwohnungen():
    def __init__(self):
        self.base = "https://www.ferienwohnungen.de"
        self.api = self.base + "/api/json"

    def result_count(self, query=None, start=None, end=None, persons=None):
        """
        Get result counts for a query.

        Comment: show results for a query wiht certain params
        Input: Name of instance optional: query, starting-date, ending-date, person-count
        Output: JSON serialized data from Webrequest
        Special: Nothing special
        """
        query = query or ""
        start = start or ""
        end = end or ""
        persons = persons or 0
        url = self.api + "/result-count/"
        params = {
            "query": query,
            "startdatum": start,
            "enddatum": end,
            "pe": persons,
        }
        r = requests.get(url, params=params)
        data = json.loads(r.content)
        return data

    def search(self, persons, start, end, type=None, bbox=None, cid=None, size=None, num=None, sorting=None):
        """
        Get results of a search for certain areas

        Comment: Get results for areas using the type, starting and ending date
        Input:Number of persons, starting and ending date, cid, further optional
              parameters
        Output: JSON serialized result of Web request
        Special: cid is the location id (example: Europe=1), the 'lower' regions
                 can be found in the filters section of the higher region
        """
        url = self.base + "/suche.json/"
        type = type or "ferienunterkuenfte"
        bbox = bbox or ""
        cid = cid or 1
        size = size or 1
        num = num or 1
        sorting = sorting or ""
        params = {
            "pe": persons,
            "startdatum": start,
            "enddatum": end,
            "view": type,
            "bbox": bbox,
            "cid": cid,
        }
        r = requests.get(url, params=params)
        data = json.loads(r.content)
        return data

    def get_unit_info(self, unit_num):
        """
        Get Unit Info for a certain Unit

        Comment: Get's Unit Info for a given Unit by it's Number
        Input: Name of Instance, Unit-Number
        Output: JSON serialized Response of the Web-Request
        Special: Nothing special
        """
        url = self.api + "/unit-navigation/"
        params = {
            "oid": unit_num
        }
        r = requests.get(url, params=params)
        print(r.url)
        data = json.loads(r.content)
        return data


def main():
    test = Ferienwohnungen()
    x = test.get_unit_info(30029)
    print(x)
    json.dump(x, open("out.json", "w"))


if __name__ == '__main__':
    main()
