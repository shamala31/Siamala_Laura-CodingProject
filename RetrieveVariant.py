
import requests

url = 'https://rest.variantvalidator.org/VariantValidator/variantvalidator/'
param1='GRCh38'
param2='2:25234374:G:A'
param3='refseq_select'
data_output_type= "?content-type=application/json"

def get_fullurl(url, param1, param2, param3):
      api_url = url + param1+"/"+param2+"/"+param3 + data_output_type
      r = requests.get(api_url)
      return(r.json())

response = (get_fullurl(url,param1,param2,param3))
print (response)






