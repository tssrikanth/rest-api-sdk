
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `content_type` | `string` | body content type for post request<br>*Default*: `'application/json'` |
| `accept_language` | `string` | response format<br>*Default*: `'application/json'` |
| `access_token` | `string` | The OAuth 2.0 Access Token to use for API requests. |
| `base_url` | `string` | *Default*: `'https://localhost:443'` |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT', 'GET', 'PUT']** |

The API client can be initialized as follows:

```python
from restapisdk.restapisdk_client import RestapisdkClient
from restapisdk.configuration import Environment

client = RestapisdkClient(
    content_type='application/json',
    accept_language='application/json',
    access_token='AccessToken',
    environment=Environment.PRODUCTION,
    base_url = 'https://localhost:443',)
```

## RESTAPI SDK Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| session | Gets SessionController |
| user | Gets UserController |
| group | Gets GroupController |
| metadata | Gets MetadataController |
| database | Gets DatabaseController |
| dependency | Gets DependencyController |

