statscollector
==============

Server to collect statistics sent by networktester. Statistics are saved to database.

Installation
============

    git clone https://github.com/annttu/statscollector.git
    cd statscollector/
    virtualenv env --python=python3.4
    . env/bin/activate
    pip install -r requirements.txt    

Setup postgresql with postgis and create database and user for statscollector.

    create user statscollector with password 'statscollector';
    grant all on database statscollector to statscollector;
    revoke all on database statscollector from public;
    \c statscollector
    create extension postgis;
    alter table spatial_ref_sys owner to statscollector;
    \q

Configure database to statscollector

    cp local_config.py.sample local_config.py
    chmod 600 local_config.py
    vim local_config.py

Done!


Run server
==========

    . env/bin/activate
    python statscollector/app.py


Add clients
===========

    . env/bin/activate
    python statscollector/add_client.py -n "client_name" -d "Client Description"

License
=======

The MIT License (MIT)
Copyright (c) 2015 Antti Jaakkola

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.