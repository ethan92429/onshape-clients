# onshape_client.DrawingsApi

All URIs are relative to *https://cad.onshape.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_translator_formats2**](DrawingsApi.md#get_translator_formats2) | **GET** /api/drawings/d/{did}/w/{wid}/e/{eid}/translationformats | 
[**translate_format4**](DrawingsApi.md#translate_format4) | **POST** /api/drawings/d/{did}/{wv}/{wvid}/e/{eid}/translations | Create Drawing translation


# **get_translator_formats2**
> get_translator_formats2(did, wid, eid)



### Example
```python
from __future__ import print_function
import time
import onshape_client
from onshape_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = onshape_client.DrawingsApi()
did = 'did_example' # str | 
wid = 'wid_example' # str | 
eid = 'eid_example' # str | 

try:
    api_instance.get_translator_formats2(did, wid, eid)
except ApiException as e:
    print("Exception when calling DrawingsApi->get_translator_formats2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wid** | **str**|  | 
 **eid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_format4**
> BTTranslationRequestInfo translate_format4(did, wv, wvid, eid, bt_translate_format_params)

Create Drawing translation

### Example

* OAuth Authentication (OAuth2): 
```python
from __future__ import print_function
import time
import onshape_client
from onshape_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = onshape_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = onshape_client.DrawingsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wv = 'wv_example' # str | 
wvid = 'wvid_example' # str | 
eid = 'eid_example' # str | 
bt_translate_format_params = onshape_client.BTTranslateFormatParams() # BTTranslateFormatParams | 

try:
    # Create Drawing translation
    api_response = api_instance.translate_format4(did, wv, wvid, eid, bt_translate_format_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DrawingsApi->translate_format4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wv** | **str**|  | 
 **wvid** | **str**|  | 
 **eid** | **str**|  | 
 **bt_translate_format_params** | [**BTTranslateFormatParams**](BTTranslateFormatParams.md)|  | 

### Return type

[**BTTranslationRequestInfo**](BTTranslationRequestInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

