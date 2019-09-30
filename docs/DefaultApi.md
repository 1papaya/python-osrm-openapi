# osrm_api.DefaultApi

All URIs are relative to *http://router.project-osrm.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**route**](DefaultApi.md#route) | **GET** /route/{version}/{profile}/{coordinates}.json | 


# **route**
> object route(version, profile, coordinates, bearings=bearings, radiuses=radiuses, generate_hints=generate_hints, hints=hints, approaches=approaches, exclude=exclude, alternatives=alternatives, steps=steps, annotations=annotations, geometries=geometries, overview=overview, continue_straight=continue_straight, waypoints=waypoints)



### Example

```python
from __future__ import print_function
import time
import osrm_api
from osrm_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = osrm_api.DefaultApi()
version = 'version_example' # str | Version of the protocol implemented by the service. v1 for all OSRM 5.x installations
profile = 'profile_example' # str | Mode of transportation, is determined statically by the Lua profile that is used to prepare the data using osrm-extract. Typically car, bike or foot if using one of the supplied profiles.
coordinates = 'coordinates_example' # str | 
bearings = 'bearings_example' # str | Limits the search to segments with given bearing in degrees towards true north in clockwise direction. (optional)
radiuses = 'radiuses_example' # str | Limits the search to given radius in meters. (optional)
generate_hints = True # bool | Adds a Hint to the response which can be used in subsequent requests, see hints parameter. (optional)
hints = 'hints_example' # str | Hint from previous request to derive position in street network. (optional)
approaches = 'approaches_example' # str | Keep waypoints on curb side. (optional)
exclude = 'exclude_example' # str | Additive list of classes to avoid, order does not matter. (optional)
alternatives = osrm_api.OneOfbooleaninteger() # OneOfbooleaninteger | Search for alternative routes. Passing a number alternatives=n searches for up to n alternative routes. (optional)
steps = False # bool | Returned route steps for each route leg (optional) (default to False)
annotations = False # bool | Returns additional metadata for each coordinate along the route geometry. (optional) (default to False)
geometries = 'polyline' # str | Returned route geometry format (influences overview and per step) (optional) (default to 'polyline')
overview = 'overview_example' # str | Add overview geometry either full, simplified according to highest zoom level it could be display on, or not at all. (optional)
continue_straight = 'continue_straight_example' # str | Forces the route to keep going straight at waypoints constraining uturns there even if it would be faster. Default value depends on the profile. (optional)
waypoints = 'waypoints_example' # str | Treats input coordinates indicated by given indices as waypoints in returned Match object. Default is to treat all input coordinates as waypoints. (optional)

try:
    api_response = api_instance.route(version, profile, coordinates, bearings=bearings, radiuses=radiuses, generate_hints=generate_hints, hints=hints, approaches=approaches, exclude=exclude, alternatives=alternatives, steps=steps, annotations=annotations, geometries=geometries, overview=overview, continue_straight=continue_straight, waypoints=waypoints)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Version of the protocol implemented by the service. v1 for all OSRM 5.x installations | 
 **profile** | **str**| Mode of transportation, is determined statically by the Lua profile that is used to prepare the data using osrm-extract. Typically car, bike or foot if using one of the supplied profiles. | 
 **coordinates** | **str**|  | 
 **bearings** | **str**| Limits the search to segments with given bearing in degrees towards true north in clockwise direction. | [optional] 
 **radiuses** | **str**| Limits the search to given radius in meters. | [optional] 
 **generate_hints** | **bool**| Adds a Hint to the response which can be used in subsequent requests, see hints parameter. | [optional] 
 **hints** | **str**| Hint from previous request to derive position in street network. | [optional] 
 **approaches** | **str**| Keep waypoints on curb side. | [optional] 
 **exclude** | **str**| Additive list of classes to avoid, order does not matter. | [optional] 
 **alternatives** | [**OneOfbooleaninteger**](.md)| Search for alternative routes. Passing a number alternatives&#x3D;n searches for up to n alternative routes. | [optional] 
 **steps** | **bool**| Returned route steps for each route leg | [optional] [default to False]
 **annotations** | **bool**| Returns additional metadata for each coordinate along the route geometry. | [optional] [default to False]
 **geometries** | **str**| Returned route geometry format (influences overview and per step) | [optional] [default to &#39;polyline&#39;]
 **overview** | **str**| Add overview geometry either full, simplified according to highest zoom level it could be display on, or not at all. | [optional] 
 **continue_straight** | **str**| Forces the route to keep going straight at waypoints constraining uturns there even if it would be faster. Default value depends on the profile. | [optional] 
 **waypoints** | **str**| Treats input coordinates indicated by given indices as waypoints in returned Match object. Default is to treat all input coordinates as waypoints. | [optional] 

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
**400** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

