# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 21:22:02 2025

@author: USER
"""

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = '1234567890',
    database = 'englearn'
    )