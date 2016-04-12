#!/usr/bin/env python

import routes
import database
import string

import random

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--name', help="Client name", required=True)
    parser.add_argument('-d', '--description', help="Client description", required=True)

    args = parser.parse_args()

    database.DB.create_tables()

    s = database.DB.get_session()

    new_token = ''.join([random.choice(string.ascii_letters + string.digits) for x in range(32)])
    new_token_hash = routes.create_password(new_token)

    new_client = database.Clients()
    new_client.name = args.name
    new_client.description = args.description
    new_client.key = new_token_hash

    s.add(new_client)
    s.commit()


    print("Token: %s" % new_token)
