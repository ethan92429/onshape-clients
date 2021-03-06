# onshape_client.AccountsApi

All URIs are relative to *https://cad.onshape.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_purchase_new**](AccountsApi.md#cancel_purchase_new) | **DELETE** /api/accounts/{aid}/purchases/{pid} | Cancel Recurring Subscription
[**consume_purchase**](AccountsApi.md#consume_purchase) | **POST** /api/accounts/purchases/{pid}/consume | Mark Purchase Consumed For User
[**get_plan_purchases**](AccountsApi.md#get_plan_purchases) | **GET** /api/accounts/plans/{planId}/purchases | Get Plan Purchases
[**get_purchases**](AccountsApi.md#get_purchases) | **GET** /api/accounts/purchases | Get User&#39;s Appstore Purchases.


# **cancel_purchase_new**
> cancel_purchase_new(aid, pid, cancel_immediately=cancel_immediately)

Cancel Recurring Subscription

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
api_instance = onshape_client.AccountsApi(onshape_client.ApiClient(configuration))
aid = 'aid_example' # str | 
pid = 'pid_example' # str | 
cancel_immediately = False # bool |  (optional) (default to False)

try:
    # Cancel Recurring Subscription
    api_instance.cancel_purchase_new(aid, pid, cancel_immediately=cancel_immediately)
except ApiException as e:
    print("Exception when calling AccountsApi->cancel_purchase_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aid** | **str**|  | 
 **pid** | **str**|  | 
 **cancel_immediately** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consume_purchase**
> BTPurchaseInfo consume_purchase(pid, bt_purchase_user_params=bt_purchase_user_params)

Mark Purchase Consumed For User

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
api_instance = onshape_client.AccountsApi(onshape_client.ApiClient(configuration))
pid = 'pid_example' # str | 
bt_purchase_user_params = onshape_client.BTPurchaseUserParams() # BTPurchaseUserParams |  (optional)

try:
    # Mark Purchase Consumed For User
    api_response = api_instance.consume_purchase(pid, bt_purchase_user_params=bt_purchase_user_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->consume_purchase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **str**|  | 
 **bt_purchase_user_params** | [**BTPurchaseUserParams**](BTPurchaseUserParams.md)|  | [optional] 

### Return type

[**BTPurchaseInfo**](BTPurchaseInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan_purchases**
> BTListResponseBTPurchaseInfo get_plan_purchases(plan_id, offset=offset, limit=limit)

Get Plan Purchases

### Example
```python
from __future__ import print_function
import time
import onshape_client
from onshape_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = onshape_client.AccountsApi()
plan_id = 'plan_id_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 20 # int |  (optional) (default to 20)

try:
    # Get Plan Purchases
    api_response = api_instance.get_plan_purchases(plan_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_plan_purchases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**BTListResponseBTPurchaseInfo**](BTListResponseBTPurchaseInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchases**
> list[BTPurchaseInfo] get_purchases(all=all, own_purchase_only=own_purchase_only)

Get User's Appstore Purchases.

### Example
```python
from __future__ import print_function
import time
import onshape_client
from onshape_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = onshape_client.AccountsApi()
all = False # bool |  (optional) (default to False)
own_purchase_only = False # bool |  (optional) (default to False)

try:
    # Get User's Appstore Purchases.
    api_response = api_instance.get_purchases(all=all, own_purchase_only=own_purchase_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_purchases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**|  | [optional] [default to False]
 **own_purchase_only** | **bool**|  | [optional] [default to False]

### Return type

[**list[BTPurchaseInfo]**](BTPurchaseInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.onshape.v1+json;charset=UTF-8; qs=0.1, application/json;charset=UTF-8; qs=0.9

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

