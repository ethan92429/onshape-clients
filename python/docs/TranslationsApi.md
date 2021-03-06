# onshape_client.TranslationsApi

All URIs are relative to *https://cad.onshape.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_translation**](TranslationsApi.md#create_translation) | **POST** /api/translations/d/{did}/w/{wid} | 
[**delete_translation**](TranslationsApi.md#delete_translation) | **DELETE** /api/translations/{tid} | 
[**get_document_translations**](TranslationsApi.md#get_document_translations) | **GET** /api/translations/d/{did} | 
[**get_translation**](TranslationsApi.md#get_translation) | **GET** /api/translations/{tid} | 
[**get_translator_formats5**](TranslationsApi.md#get_translator_formats5) | **GET** /api/translations/translationformats | 


# **create_translation**
> create_translation(did, wid, content_disposition=content_disposition, entity=entity, headers=headers, media_type=media_type, message_body_workers=message_body_workers, parent=parent, providers=providers, body_parts=body_parts, parameterized_headers=parameterized_headers)



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
api_instance = onshape_client.TranslationsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wid = 'wid_example' # str | 
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
    api_instance.create_translation(did, wid, content_disposition=content_disposition, entity=entity, headers=headers, media_type=media_type, message_body_workers=message_body_workers, parent=parent, providers=providers, body_parts=body_parts, parameterized_headers=parameterized_headers)
except ApiException as e:
    print("Exception when calling TranslationsApi->create_translation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wid** | **str**|  | 
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

# **delete_translation**
> delete_translation(tid)



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
api_instance = onshape_client.TranslationsApi(onshape_client.ApiClient(configuration))
tid = 'tid_example' # str | 

try:
    api_instance.delete_translation(tid)
except ApiException as e:
    print("Exception when calling TranslationsApi->delete_translation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_translations**
> get_document_translations(did, offset=offset, limit=limit)



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
api_instance = onshape_client.TranslationsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 20 # int |  (optional) (default to 20)

try:
    api_instance.get_document_translations(did, offset=offset, limit=limit)
except ApiException as e:
    print("Exception when calling TranslationsApi->get_document_translations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 20]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_translation**
> get_translation(tid)



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
api_instance = onshape_client.TranslationsApi(onshape_client.ApiClient(configuration))
tid = 'tid_example' # str | 

try:
    api_instance.get_translation(tid)
except ApiException as e:
    print("Exception when calling TranslationsApi->get_translation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_translator_formats5**
> get_translator_formats5()



### Example
```python
from __future__ import print_function
import time
import onshape_client
from onshape_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = onshape_client.TranslationsApi()

try:
    api_instance.get_translator_formats5()
except ApiException as e:
    print("Exception when calling TranslationsApi->get_translator_formats5: %s\n" % e)
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

