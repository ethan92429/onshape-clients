# onshape_client.DocumentsApi

All URIs are relative to *https://cad.onshape.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create11**](DocumentsApi.md#create11) | **POST** /api/documents | 
[**download_external_data**](DocumentsApi.md#download_external_data) | **GET** /api/documents/d/{did}/externaldata/{fid} | Download External Data
[**get_current_microversion**](DocumentsApi.md#get_current_microversion) | **GET** /api/documents/d/{did}/{wv}/{wvid}/currentmicroversion | 
[**get_documents**](DocumentsApi.md#get_documents) | **GET** /api/documents | Get Documents
[**merge_into_workspace**](DocumentsApi.md#merge_into_workspace) | **POST** /api/documents/{did}/workspaces/{wid}/merge | Merge into workspace
[**restore_document**](DocumentsApi.md#restore_document) | **POST** /api/documents/{did}/restore | Restore Document


# **create11**
> create11(bt_document_params)



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
api_instance = onshape_client.DocumentsApi(onshape_client.ApiClient(configuration))
bt_document_params = onshape_client.BTDocumentParams() # BTDocumentParams | 

try:
    api_instance.create11(bt_document_params)
except ApiException as e:
    print("Exception when calling DocumentsApi->create11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bt_document_params** | [**BTDocumentParams**](BTDocumentParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_external_data**
> file download_external_data(did, fid, if_none_match=if_none_match)

Download External Data

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
api_instance = onshape_client.DocumentsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
fid = 'fid_example' # str | 
if_none_match = 'if_none_match_example' # str |  (optional)

try:
    # Download External Data
    api_response = api_instance.download_external_data(did, fid, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->download_external_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **fid** | **str**|  | 
 **if_none_match** | **str**|  | [optional] 

### Return type

**file**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9, application/vnd.onshape.v1+octet-stream; qs=0.1, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_microversion**
> get_current_microversion(did, wv, wvid)



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
api_instance = onshape_client.DocumentsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wv = 'wv_example' # str | 
wvid = 'wvid_example' # str | 

try:
    api_instance.get_current_microversion(did, wv, wvid)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_current_microversion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wv** | **str**|  | 
 **wvid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents**
> BTGlobalTreeNodeListResponse get_documents(q=q, filter=filter, owner=owner, owner_type=owner_type, sort_column=sort_column, sort_order=sort_order, offset=offset, limit=limit, label=label, project=project, parent_id=parent_id)

Get Documents

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
api_instance = onshape_client.DocumentsApi(onshape_client.ApiClient(configuration))
q = 'q_example' # str |  (optional)
filter = 56 # int |  (optional)
owner = 'owner_example' # str |  (optional)
owner_type = 1 # int |  (optional) (default to 1)
sort_column = 'createdAt' # str |  (optional) (default to 'createdAt')
sort_order = 'desc' # str |  (optional) (default to 'desc')
offset = 0 # int |  (optional) (default to 0)
limit = 20 # int |  (optional) (default to 20)
label = 'label_example' # str |  (optional)
project = 'project_example' # str |  (optional)
parent_id = 'parent_id_example' # str |  (optional)

try:
    # Get Documents
    api_response = api_instance.get_documents(q=q, filter=filter, owner=owner, owner_type=owner_type, sort_column=sort_column, sort_order=sort_order, offset=offset, limit=limit, label=label, project=project, parent_id=parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **filter** | **int**|  | [optional] 
 **owner** | **str**|  | [optional] 
 **owner_type** | **int**|  | [optional] [default to 1]
 **sort_column** | **str**|  | [optional] [default to &#39;createdAt&#39;]
 **sort_order** | **str**|  | [optional] [default to &#39;desc&#39;]
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 20]
 **label** | **str**|  | [optional] 
 **project** | **str**|  | [optional] 
 **parent_id** | **str**|  | [optional] 

### Return type

[**BTGlobalTreeNodeListResponse**](BTGlobalTreeNodeListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_into_workspace**
> BTDocumentMergeInfo merge_into_workspace(did, wid, bt_version_or_workspace_info)

Merge into workspace

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
api_instance = onshape_client.DocumentsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 
wid = 'wid_example' # str | 
bt_version_or_workspace_info = onshape_client.BTVersionOrWorkspaceInfo() # BTVersionOrWorkspaceInfo | 

try:
    # Merge into workspace
    api_response = api_instance.merge_into_workspace(did, wid, bt_version_or_workspace_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->merge_into_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **wid** | **str**|  | 
 **bt_version_or_workspace_info** | [**BTVersionOrWorkspaceInfo**](BTVersionOrWorkspaceInfo.md)|  | 

### Return type

[**BTDocumentMergeInfo**](BTDocumentMergeInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.onshape.v2+json;charset=UTF-8; qs=0.2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_document**
> BTDocumentMergeInfo restore_document(did)

Restore Document

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
api_instance = onshape_client.DocumentsApi(onshape_client.ApiClient(configuration))
did = 'did_example' # str | 

try:
    # Restore Document
    api_response = api_instance.restore_document(did)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->restore_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 

### Return type

[**BTDocumentMergeInfo**](BTDocumentMergeInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v2+json;charset=UTF-8; qs=0.2

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

