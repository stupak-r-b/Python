"""
Your mission is to figure out how many spam reports you receive on a specific day.

Input: Day as a string in format 'YYYY-MM-DD'
Output: Int. The amount of spam reports
"""

import sendgrid, json
from datetime import timedelta, datetime


def how_spammed(str_date):
    API_KEY = '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'
    sg = sendgrid.SendGridAPIClient(API_KEY)
    start_time = datetime.strptime(str_date, '%Y-%m-%d')
    end_time = start_time + timedelta(days=1)
    response = sg.client.suppression.spam_reports.get(
        query_params={'start_time': int(start_time.timestamp()), 'end_time': int(end_time.timestamp())})
    data = json.loads(response.body)
    count = 0
    for i in data: count += 1
    return count


if __name__ == '__main__':

    print('You had {} spam reports in 2016-01-01'.format(how_spammed('2016-01-01')))
    print('Check your results')
