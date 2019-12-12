import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from Functions import * 

def test_predict():
    assert callable(predict)
    assert predict(1, 2, 3) == 5
    assert predict(0, 0, 0) == 0
    assert isinstance(predict(3, 6, 9), int)
    
def test_raw_data_to_protein_values():
    assert callable(raw_data_to_protein_values)
    assert isinstance(raw_data_to_protein_values(3,6,9), list)
