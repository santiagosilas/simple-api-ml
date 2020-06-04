from requests import put, get, post, delete
import numpy as np
import os, json

if __name__ == '__main__':
    features = [2.5, 1.2, 3.4, 4.5]
    url = 'http://localhost:5000/predict?features={}'.format(features)
    print('Response:', get(url).json())