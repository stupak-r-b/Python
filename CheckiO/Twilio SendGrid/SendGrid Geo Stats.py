"""
Your mission is to figure out which country opens your emails the most. You can use this information in order to focus on a specific segment.

Input: Day as a string in format 'YYYY-MM-DD'
Output: String, Two-digit country code of country that has more unique clicks.
"""
import sendgrid
import json


def best_country(str_date):
    API_KEY = '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'
    sg = sendgrid.SendGridAPIClient(API_KEY)
    response = sg.client.geo.stats.get(query_params={
        'start_date': str_date,
        'end_date': str_date
    })
    data = json.loads(response.body)
    country = []
    opened = []
    for i in data:
        for j in i["stats"]:
            for q in j.values():
                if type(q) == str:
                    if len(q) <= 3:
                        country.append(q)
                elif type(q) == dict:
                    opened.append(q["opens"])
    return country[opened.index(max(opened))]


if __name__ == '__main__':

    print('Your best country in 2016-01-01 was ' + best_country('2016-01-01'))
    print('Check your results')
