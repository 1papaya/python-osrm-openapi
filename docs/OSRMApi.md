# osrm_api.OSRMApi

All URIs are relative to *http://router.project-osrm.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nearest**](OSRMApi.md#nearest) | **GET** /nearest/{version}/{profile}/{coordinates}.json | 


# **nearest**
> object nearest(version, profile, coordinates, number, bearings=bearings, radiuses=radiuses, generate_hints=generate_hints, hints=hints, approaches=approaches, exclude=exclude)



### Example

```python
from __future__ import print_function
import time
import osrm_api
from osrm_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = osrm_api.OSRMApi()
version = 'version_example' # str | 
profile = 'profile_example' # str | 
coordinates = 'coordinates_example' # str | 
number = 1 # int |  (default to 1)
bearings = 'bearings_example' # str |  (optional)
radiuses = 'radiuses_example' # str |  (optional)
generate_hints = True # bool |  (optional)
hints = 'hints_example' # str |  (optional)
approaches = 'approaches_example' # str |  (optional)
exclude = 'exclude_example' # str |  (optional)

try:
    api_response = api_instance.nearest(version, profile, coordinates, number, bearings=bearings, radiuses=radiuses, generate_hints=generate_hints, hints=hints, approaches=approaches, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OSRMApi->nearest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **profile** | **str**|  | 
 **coordinates** | **str**|  | 
 **number** | **int**|  | [default to 1]
 **bearings** | **str**|  | [optional] 
 **radiuses** | **str**|  | [optional] 
 **generate_hints** | **bool**|  | [optional] 
 **hints** | **str**|  | [optional] 
 **approaches** | **str**|  | [optional] 
 **exclude** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

