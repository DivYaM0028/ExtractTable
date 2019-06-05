from tabula import read_pdf
from tabulate import tabulate
import camelot
import pandas as pd
def Pages():
    tables = camelot.read_pdf("11_chapter 2.pdf",pages='all')
    result=[]
    coordinates=[]
    for i in tables:
        result.append(i.page)
        coordinates.append(i._bbox)
    pages = [str(i) + str(j) for i, j in zip(result, coordinates)] 
    return pages
