#!/usr/bin/env python3
"""
Log stats for Nginx.
"""

from pymongo import MongoClient


def display_logs(nginx_logs):
    """
    Provides some stats about Nginx logs stored in MongoDB.
    """
    print('{} logs'.format(nginx_logs.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        request_count = len(list(nginx_logs.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        nginx_logs.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    """
    Runs printing method using mongo client.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    display_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
