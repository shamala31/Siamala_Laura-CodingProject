
import unittest

from CodingProject import RetrieveVariant

url = 'https://rest.variantvalidator.org/VariantValidator/variantvalidator/'
param1 ='GRCh38'
param2 ='2:25234374:G:A'
param3 ='refseq_select'
data_output_type= "?content-type=application/json"

class url(unittest.TestCase):
    def get_fullurl(url, param1, param2, param3 ,):
     url = url + param1 +"/ " +param2 +"/ " +param3 + data_output_type

    assert response url == 200\
        (True)  # add assertion here

if __name__ == '__main__':
    unittest.main()
