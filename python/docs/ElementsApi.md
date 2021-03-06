# onshape_client.ElementsApi

All URIs are relative to *https://cad.onshape.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_element_from_source_document1**](ElementsApi.md#copy_element_from_source_document1) | **POST** /api/elements/copyelement/{did}/workspace/{wid} | 
[**decode_configuration**](ElementsApi.md#decode_configuration) | **GET** /api/elements/d/{did}/{wvm}/{wvmid}/e/{eid}/configurationencodings/{cid} | 
[**delete8**](ElementsApi.md#delete8) | **DELETE** /api/elements/d/{did}/w/{wid}/e/{eid} | 
[**encode_configuration_map**](ElementsApi.md#encode_configuration_map) | **POST** /api/elements/d/{did}/e/{eid}/configurationencodings | 
[**get_configuration3**](ElementsApi.md#get_configuration3) | **GET** /api/elements/d/{did}/{wvm}/{wvmid}/e/{eid}/configuration | 
[**get_element_by_version_deprecated**](ElementsApi.md#get_element_by_version_deprecated) | **GET** /api/elements/{did}/version/{vid} | 
[**get_element_by_workspace_deprecated**](ElementsApi.md#get_element_by_workspace_deprecated) | **GET** /api/elements/{did}/workspace/{wid} | 
[**get_element_metadata**](ElementsApi.md#get_element_metadata) | **GET** /api/elements/d/{did}/{wv}/{wvid}/e/{eid}/metadata | 
[**get_element_metadata_deprecated**](ElementsApi.md#get_element_metadata_deprecated) | **GET** /api/elements/{emid} | 
[**get_element_translator_formats1**](ElementsApi.md#get_element_translator_formats1) | **GET** /api/elements/translatorFormats/{did}/{wid}/{eid} | 
[**get_translator_formats3**](ElementsApi.md#get_translator_formats3) | **GET** /api/elements/translatorFormats | 
[**update_configuration2**](ElementsApi.md#update_configuration2) | **POST** /api/elements/d/{did}/{wvm}/{wvmid}/e/{eid}/configuration | 
[**update_element_metadata**](ElementsApi.md#update_element_metadata) | **POST** /api/elements/d/{did}/{wv}/{wvid}/e/{eid}/metadata | 
[**update_references1**](ElementsApi.md#update_references1) | **POST** /api/elements/d/{did}/w/{wid}/e/{eid}/updatereferences | 
[**upload_file2**](ElementsApi.md#upload_file2) | **POST** /api/elements/upload/{did} | 


# **copy_element_from_source_document1**
> copy_element_from_source_document1(did, wid, bt_copy_element_params)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wid = 'wid_example' # str | 
bt_copy_element_params = onshape_client.BTCopyElementParams() # BTCopyElementParams | 

try:
    api_instance.copy_element_from_source_document1(did, wid, bt_copy_element_params)
except ApiException as e:
    print("Exception when calling ElementsApi->copy_element_from_source_document1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wid** | **str**|  | 
 **bt_copy_element_params** | [**BTCopyElementParams**](BTCopyElementParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decode_configuration**
> decode_configuration(did, wvm, wvmid, eid, cid, link_document_id=link_document_id, include_display=include_display, configuration_is_id=configuration_is_id)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wvm = 'wvm_example' # str | 
wvmid = 'wvmid_example' # str | 
eid = 'eid_example' # str | 
cid = 'cid_example' # str | 
link_document_id = 'link_document_id_example' # str |  (optional)
include_display = False # bool |  (optional) (default to False)
configuration_is_id = False # bool |  (optional) (default to False)

try:
    api_instance.decode_configuration(did, wvm, wvmid, eid, cid, link_document_id=link_document_id, include_display=include_display, configuration_is_id=configuration_is_id)
except ApiException as e:
    print("Exception when calling ElementsApi->decode_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wvm** | **str**|  | 
 **wvmid** | **str**|  | 
 **eid** | **str**|  | 
 **cid** | **str**|  | 
 **link_document_id** | **str**|  | [optional] 
 **include_display** | **bool**|  | [optional] [default to False]
 **configuration_is_id** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete8**
> delete8(did, wid, eid)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wid = 'wid_example' # str | 
eid = 'eid_example' # str | 

try:
    api_instance.delete8(did, wid, eid)
except ApiException as e:
    print("Exception when calling ElementsApi->delete8: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encode_configuration_map**
> encode_configuration_map(did, eid, bt_configuration_params, version_id=version_id, link_document_id=link_document_id)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
eid = 'eid_example' # str | 
bt_configuration_params = onshape_client.BTConfigurationParams() # BTConfigurationParams | 
version_id = 'version_id_example' # str |  (optional)
link_document_id = 'link_document_id_example' # str |  (optional)

try:
    api_instance.encode_configuration_map(did, eid, bt_configuration_params, version_id=version_id, link_document_id=link_document_id)
except ApiException as e:
    print("Exception when calling ElementsApi->encode_configuration_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **eid** | **str**|  | 
 **bt_configuration_params** | [**BTConfigurationParams**](BTConfigurationParams.md)|  | 
 **version_id** | **str**|  | [optional] 
 **link_document_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration3**
> get_configuration3(did, wvm, wvmid, eid)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wvm = 'wvm_example' # str | 
wvmid = 'wvmid_example' # str | 
eid = 'eid_example' # str | 

try:
    api_instance.get_configuration3(did, wvm, wvmid, eid)
except ApiException as e:
    print("Exception when calling ElementsApi->get_configuration3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wvm** | **str**|  | 
 **wvmid** | **str**|  | 
 **eid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_by_version_deprecated**
> get_element_by_version_deprecated(did, vid, with_thumbnails=with_thumbnails)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
vid = 'vid_example' # str | 
with_thumbnails = False # bool |  (optional) (default to False)

try:
    api_instance.get_element_by_version_deprecated(did, vid, with_thumbnails=with_thumbnails)
except ApiException as e:
    print("Exception when calling ElementsApi->get_element_by_version_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **vid** | **str**|  | 
 **with_thumbnails** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_by_workspace_deprecated**
> get_element_by_workspace_deprecated(did, wid, with_thumbnails=with_thumbnails)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wid = 'wid_example' # str | 
with_thumbnails = False # bool |  (optional) (default to False)

try:
    api_instance.get_element_by_workspace_deprecated(did, wid, with_thumbnails=with_thumbnails)
except ApiException as e:
    print("Exception when calling ElementsApi->get_element_by_workspace_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wid** | **str**|  | 
 **with_thumbnails** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_metadata**
> get_element_metadata(did, wv, wvid, eid, link_document_id=link_document_id)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wv = 'wv_example' # str | 
wvid = 'wvid_example' # str | 
eid = 'eid_example' # str | 
link_document_id = 'link_document_id_example' # str |  (optional)

try:
    api_instance.get_element_metadata(did, wv, wvid, eid, link_document_id=link_document_id)
except ApiException as e:
    print("Exception when calling ElementsApi->get_element_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wv** | **str**|  | 
 **wvid** | **str**|  | 
 **eid** | **str**|  | 
 **link_document_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_metadata_deprecated**
> get_element_metadata_deprecated(emid)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
emid = 'emid_example' # str | 

try:
    api_instance.get_element_metadata_deprecated(emid)
except ApiException as e:
    print("Exception when calling ElementsApi->get_element_metadata_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_translator_formats1**
> get_element_translator_formats1(did, wid, eid, check_content=check_content, configuration=configuration)



### Example
```python
from __future__ import print_function
import time
import onshape_client
from onshape_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = onshape_client.ElementsApi()
did = 'did_example' # str | 
wid = 'wid_example' # str | 
eid = 'eid_example' # str | 
check_content = True # bool |  (optional) (default to True)
configuration = 'configuration_example' # str |  (optional)

try:
    api_instance.get_element_translator_formats1(did, wid, eid, check_content=check_content, configuration=configuration)
except ApiException as e:
    print("Exception when calling ElementsApi->get_element_translator_formats1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wid** | **str**|  | 
 **eid** | **str**|  | 
 **check_content** | **bool**|  | [optional] [default to True]
 **configuration** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_translator_formats3**
> get_translator_formats3()



### Example
```python
from __future__ import print_function
import time
import onshape_client
from onshape_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = onshape_client.ElementsApi()

try:
    api_instance.get_translator_formats3()
except ApiException as e:
    print("Exception when calling ElementsApi->get_translator_formats3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration2**
> update_configuration2(did, wvm, wvmid, eid, body=body)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wvm = 'wvm_example' # str | 
wvmid = 'wvmid_example' # str | 
eid = 'eid_example' # str | 
body = 'body_example' # str |  (optional)

try:
    api_instance.update_configuration2(did, wvm, wvmid, eid, body=body)
except ApiException as e:
    print("Exception when calling ElementsApi->update_configuration2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wvm** | **str**|  | 
 **wvmid** | **str**|  | 
 **eid** | **str**|  | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_element_metadata**
> update_element_metadata(did, wv, wvid, eid, btpdm_metadata_params)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wv = 'wv_example' # str | 
wvid = 'wvid_example' # str | 
eid = 'eid_example' # str | 
btpdm_metadata_params = onshape_client.BTPDMMetadataParams() # BTPDMMetadataParams | 

try:
    api_instance.update_element_metadata(did, wv, wvid, eid, btpdm_metadata_params)
except ApiException as e:
    print("Exception when calling ElementsApi->update_element_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wv** | **str**|  | 
 **wvid** | **str**|  | 
 **eid** | **str**|  | 
 **btpdm_metadata_params** | [**BTPDMMetadataParams**](BTPDMMetadataParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_references1**
> update_references1(did, wid, eid, bt_update_reference_params)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wid = 'wid_example' # str | 
eid = 'eid_example' # str | 
bt_update_reference_params = onshape_client.BTUpdateReferenceParams() # BTUpdateReferenceParams | 

try:
    api_instance.update_references1(did, wid, eid, bt_update_reference_params)
except ApiException as e:
    print("Exception when calling ElementsApi->update_references1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wid** | **str**|  | 
 **eid** | **str**|  | 
 **bt_update_reference_params** | [**BTUpdateReferenceParams**](BTUpdateReferenceParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file2**
> upload_file2(did, element_id=element_id, workspace_id=workspace_id, content_disposition=content_disposition, entity=entity, headers=headers, media_type=media_type, message_body_workers=message_body_workers, parent=parent, providers=providers, body_parts=body_parts, parameterized_headers=parameterized_headers)



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
api_instance = onshape_client.ElementsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
element_id = 'element_id_example' # str |  (optional)
workspace_id = 'workspace_id_example' # str |  (optional)
content_disposition = onshape_client.ContentDisposition() # ContentDisposition |  (optional)
entity = NULL # object |  (optional)
headers = onshape_client.BodyPartHeaders() # BodyPartHeaders |  (optional)
media_type = onshape_client.BodyPartMediaType() # BodyPartMediaType |  (optional)
message_body_workers = onshape_client.MessageBodyWorkers() # MessageBodyWorkers |  (optional)
parent = onshape_client.MultiPart() # MultiPart |  (optional)
providers = NULL # object |  (optional)
body_parts = onshape_client.BodyPart() # list[BodyPart] |  (optional)
parameterized_headers = onshape_client.BodyPartHeaders() # BodyPartHeaders |  (optional)

try:
    api_instance.upload_file2(did, element_id=element_id, workspace_id=workspace_id, content_disposition=content_disposition, entity=entity, headers=headers, media_type=media_type, message_body_workers=message_body_workers, parent=parent, providers=providers, body_parts=body_parts, parameterized_headers=parameterized_headers)
except ApiException as e:
    print("Exception when calling ElementsApi->upload_file2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **element_id** | **str**|  | [optional] 
 **workspace_id** | **str**|  | [optional] 
 **content_disposition** | [**ContentDisposition**](ContentDisposition.md)|  | [optional] 
 **entity** | [**object**](object.md)|  | [optional] 
 **headers** | [**BodyPartHeaders**](BodyPartHeaders.md)|  | [optional] 
 **media_type** | [**BodyPartMediaType**](BodyPartMediaType.md)|  | [optional] 
 **message_body_workers** | [**MessageBodyWorkers**](MessageBodyWorkers.md)|  | [optional] 
 **parent** | [**MultiPart**](MultiPart.md)|  | [optional] 
 **providers** | [**object**](object.md)|  | [optional] 
 **body_parts** | [**list[BodyPart]**](BodyPart.md)|  | [optional] 
 **parameterized_headers** | [**BodyPartHeaders**](BodyPartHeaders.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

