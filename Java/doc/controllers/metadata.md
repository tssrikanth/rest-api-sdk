# Metadata

```java
MetadataController metadataController = client.getMetadataController();
```

## Class Name

`MetadataController`

## Methods

* [Get Tag](/doc/controllers/metadata.md#get-tag)
* [Create Tag](/doc/controllers/metadata.md#create-tag)
* [Update Tag](/doc/controllers/metadata.md#update-tag)
* [Delete Tag](/doc/controllers/metadata.md#delete-tag)
* [Assign Tag](/doc/controllers/metadata.md#assign-tag)
* [Unassign Tag](/doc/controllers/metadata.md#unassign-tag)
* [Assign Favorite](/doc/controllers/metadata.md#assign-favorite)
* [Unassign Favorite](/doc/controllers/metadata.md#unassign-favorite)
* [Get Homeliveboard](/doc/controllers/metadata.md#get-homeliveboard)
* [Assign Homeliveboard](/doc/controllers/metadata.md#assign-homeliveboard)
* [Unassign Homeliveboard](/doc/controllers/metadata.md#unassign-homeliveboard)
* [Get Incomplete Objects](/doc/controllers/metadata.md#get-incomplete-objects)
* [Get Object Header](/doc/controllers/metadata.md#get-object-header)
* [Get Object Visualization Header](/doc/controllers/metadata.md#get-object-visualization-header)
* [Get Object Detail](/doc/controllers/metadata.md#get-object-detail)
* [Export Object TML](/doc/controllers/metadata.md#export-object-tml)
* [Import Object TML](/doc/controllers/metadata.md#import-object-tml)


# Get Tag

To get details of a specific tag, use this endpoint. At least one of id or name of tag is required. When both are given, then id will be considered.

```java
CompletableFuture<MetadataTagResponse> getTagAsync(
    final String name,
    final String id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `String` | Query, Optional | Name of the tag |
| `id` | `String` | Query, Optional | The GUID of the tag |

## Response Type

[`MetadataTagResponse`](/doc/models/metadata-tag-response.md)

## Example Usage

```java
metadataController.getTagAsync(null, null).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Create Tag

To programmatically create tags, use this endpoint

```java
CompletableFuture<MetadataTagResponse> createTagAsync(
    final ApiRestV2MetadataTagCreateRequest body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiRestV2MetadataTagCreateRequest`](/doc/models/api-rest-v2-metadata-tag-create-request.md) | Body, Required | - |

## Response Type

[`MetadataTagResponse`](/doc/models/metadata-tag-response.md)

## Example Usage

```java
ApiRestV2MetadataTagCreateRequest body = new ApiRestV2MetadataTagCreateRequest();
body.setName("name6");

metadataController.createTagAsync(body).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Update Tag

To programmatically update tags, use this endpoint. At least one of id or name of tag is required. When both are given, then id will be considered.

```java
CompletableFuture<Boolean> updateTagAsync(
    final ApiRestV2MetadataTagUpdateRequest body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiRestV2MetadataTagUpdateRequest`](/doc/models/api-rest-v2-metadata-tag-update-request.md) | Body, Required | - |

## Response Type

`boolean`

## Example Usage

```java
ApiRestV2MetadataTagUpdateRequest body = new ApiRestV2MetadataTagUpdateRequest();

metadataController.updateTagAsync(body).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Delete Tag

To programmatically delete tags, use this endpoint. At least one of id or name of tag is required. When both are given, then id will be considered.

```java
CompletableFuture<Boolean> deleteTagAsync(
    final String name,
    final String id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `String` | Query, Optional | Name of the tag |
| `id` | `String` | Query, Optional | The GUID of the tag |

## Response Type

`boolean`

## Example Usage

```java
metadataController.deleteTagAsync(null, null).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Assign Tag

To programmatically assign tags to a metadata object, such as a liveboard, search answer, table, worksheet, or view, use this endpoint.  At least one of id or name of tag is required. When both are given, then id will be considered.

```java
CompletableFuture<Boolean> assignTagAsync(
    final ApiRestV2MetadataTagAssignRequest body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiRestV2MetadataTagAssignRequest`](/doc/models/api-rest-v2-metadata-tag-assign-request.md) | Body, Required | - |

## Response Type

`boolean`

## Example Usage

```java
ApiRestV2MetadataTagAssignRequest body = new ApiRestV2MetadataTagAssignRequest();
body.setMetaObject(new LinkedList<>());

MetaObjectInput bodyMetaObject0 = new MetaObjectInput();
bodyMetaObject0.setId("id6");
bodyMetaObject0.setType(TypeEnum.ANSWER);
body.getMetaObject().add(bodyMetaObject0);

MetaObjectInput bodyMetaObject1 = new MetaObjectInput();
bodyMetaObject1.setId("id7");
bodyMetaObject1.setType(TypeEnum.LIVEBOARD);
body.getMetaObject().add(bodyMetaObject1);


metadataController.assignTagAsync(body).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Unassign Tag

To programmatically unassign tags to a metadata object, such as a liveboard, search answer, table, worksheet, or view, use this endpoint. At least one of id or name of tag is required. When both are given, then id will be considered.

```java
CompletableFuture<Boolean> unassignTagAsync(
    final ApiRestV2MetadataTagUnassignRequest body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiRestV2MetadataTagUnassignRequest`](/doc/models/api-rest-v2-metadata-tag-unassign-request.md) | Body, Required | - |

## Response Type

`boolean`

## Example Usage

```java
ApiRestV2MetadataTagUnassignRequest body = new ApiRestV2MetadataTagUnassignRequest();
body.setMetaObject(new LinkedList<>());

MetaObjectInput bodyMetaObject0 = new MetaObjectInput();
bodyMetaObject0.setId("id6");
bodyMetaObject0.setType(TypeEnum.ANSWER);
body.getMetaObject().add(bodyMetaObject0);

MetaObjectInput bodyMetaObject1 = new MetaObjectInput();
bodyMetaObject1.setId("id7");
bodyMetaObject1.setType(TypeEnum.LIVEBOARD);
body.getMetaObject().add(bodyMetaObject1);


metadataController.unassignTagAsync(body).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Assign Favorite

To programmatically assign objects to favorites for a given user account, use this endpoint. At least one of user id or username is required. When both are given, then id will be considered.

```java
CompletableFuture<Boolean> assignFavoriteAsync(
    final ApiRestV2MetadataFavoriteAssignRequest body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiRestV2MetadataFavoriteAssignRequest`](/doc/models/api-rest-v2-metadata-favorite-assign-request.md) | Body, Required | - |

## Response Type

`boolean`

## Example Usage

```java
ApiRestV2MetadataFavoriteAssignRequest body = new ApiRestV2MetadataFavoriteAssignRequest();
body.setMetaObject(new LinkedList<>());

MetaObjectInput bodyMetaObject0 = new MetaObjectInput();
bodyMetaObject0.setId("id6");
bodyMetaObject0.setType(TypeEnum.ANSWER);
body.getMetaObject().add(bodyMetaObject0);

MetaObjectInput bodyMetaObject1 = new MetaObjectInput();
bodyMetaObject1.setId("id7");
bodyMetaObject1.setType(TypeEnum.LIVEBOARD);
body.getMetaObject().add(bodyMetaObject1);


metadataController.assignFavoriteAsync(body).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Unassign Favorite

To programmatically unassign objects to favorites for a given user account, use this endpoint. At least one of user id or username is required. When both are given, then id will be considered.Screen reader support enabled.

```java
CompletableFuture<Boolean> unassignFavoriteAsync(
    final ApiRestV2MetadataFavoriteUnassignRequest body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiRestV2MetadataFavoriteUnassignRequest`](/doc/models/api-rest-v2-metadata-favorite-unassign-request.md) | Body, Required | - |

## Response Type

`boolean`

## Example Usage

```java
ApiRestV2MetadataFavoriteUnassignRequest body = new ApiRestV2MetadataFavoriteUnassignRequest();
body.setMetaObject(new LinkedList<>());

MetaObjectInput bodyMetaObject0 = new MetaObjectInput();
bodyMetaObject0.setId("id6");
bodyMetaObject0.setType(TypeEnum.ANSWER);
body.getMetaObject().add(bodyMetaObject0);

MetaObjectInput bodyMetaObject1 = new MetaObjectInput();
bodyMetaObject1.setId("id7");
bodyMetaObject1.setType(TypeEnum.LIVEBOARD);
body.getMetaObject().add(bodyMetaObject1);


metadataController.unassignFavoriteAsync(body).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Get Homeliveboard

To get the name and id of liveboard that is set as a home liveboard for a user, use this endpoint. At least one of user id or username is required. When both are given, then id will be considered.

```java
CompletableFuture<HomeLiveboardResponse> getHomeliveboardAsync(
    final String userName,
    final String userId)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userName` | `String` | Query, Optional | - |
| `userId` | `String` | Query, Optional | The GUID of the user |

## Response Type

[`HomeLiveboardResponse`](/doc/models/home-liveboard-response.md)

## Example Usage

```java
metadataController.getHomeliveboardAsync(null, null).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Assign Homeliveboard

To assign a specific liveboard as a home liveboard for a user, use this endpoint. At least one of user id or username is required. When both are given, then id will be considered.

```java
CompletableFuture<Boolean> assignHomeliveboardAsync(
    final ApiRestV2MetadataHomeliveboardAssignRequest body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiRestV2MetadataHomeliveboardAssignRequest`](/doc/models/api-rest-v2-metadata-homeliveboard-assign-request.md) | Body, Required | - |

## Response Type

`boolean`

## Example Usage

```java
ApiRestV2MetadataHomeliveboardAssignRequest body = new ApiRestV2MetadataHomeliveboardAssignRequest();

metadataController.assignHomeliveboardAsync(body).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Unassign Homeliveboard

To unassign the home liveboard set for a user, use this endpoint. At least one of user id or username is required. When both are given, then id will be considered.

```java
CompletableFuture<Boolean> unassignHomeliveboardAsync(
    final ApiRestV2MetadataHomeliveboardUnassignRequest body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiRestV2MetadataHomeliveboardUnassignRequest`](/doc/models/api-rest-v2-metadata-homeliveboard-unassign-request.md) | Body, Required | - |

## Response Type

`boolean`

## Example Usage

```java
ApiRestV2MetadataHomeliveboardUnassignRequest body = new ApiRestV2MetadataHomeliveboardUnassignRequest();

metadataController.unassignHomeliveboardAsync(body).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Get Incomplete Objects

To get a list of objects with incomplete metadata, use this endpoint

```java
CompletableFuture<Object> getIncompleteObjectsAsync()
```

## Response Type

`Object`

## Example Usage

```java
metadataController.getIncompleteObjectsAsync().thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Get Object Header

To get header details for metadata objects, use this endpoint. You can provide as input selective fields to get the data for.

```java
CompletableFuture<Object> getObjectHeaderAsync(
    final Type2Enum type,
    final List<String> outputFields,
    final String offset,
    final String batchSize,
    final SortByEnum sortBy,
    final SortOrderEnum sortOrder,
    final String namePattern,
    final List<String> fetchId,
    final List<String> skipId,
    final Boolean showHidden,
    final AutoCreatedEnum autoCreated)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | [`Type2Enum`](/doc/models/type-2-enum.md) | Query, Required | Type of the metadata object being searched. |
| `outputFields` | `List<String>` | Query, Optional | Array of header field names that need to be included in the header response |
| `offset` | `String` | Query, Optional | The batch offset, starting from where the records should be included in the response. If no input is provided then offset starts from 0. |
| `batchSize` | `String` | Query, Optional | The number of records that should be included in the response starting from offset position. If no input is provided then first page is included in the response. |
| `sortBy` | [`SortByEnum`](/doc/models/sort-by-enum.md) | Query, Optional | Field based on which the response needs to be ordered.<br>**Default**: `SortByEnum.DEFAULT` |
| `sortOrder` | [`SortOrderEnum`](/doc/models/sort-order-enum.md) | Query, Optional | Order in which sortBy should be applied.<br>**Default**: `SortOrderEnum.DEFAULT` |
| `namePattern` | `String` | Query, Optional | A pattern to match the name of the metadata object. This parameter supports matching case-insensitive strings. For a wildcard match, use %. |
| `fetchId` | `List<String>` | Query, Optional | A JSON array containing the GUIDs of the metadata objects that you want to fetch. |
| `skipId` | `List<String>` | Query, Optional | A JSON array containing the GUIDs of the metadata objects that you want to skip. |
| `showHidden` | `Boolean` | Query, Optional | When set to true, returns details of the hidden objects, such as a column in a worksheet or a table. |
| `autoCreated` | [`AutoCreatedEnum`](/doc/models/auto-created-enum.md) | Query, Optional | String for UI and backend boolean- A flag to indicate whether to list only the auto created objects. When no value is provided as input then all objects are returned. |

## Response Type

`Object`

## Example Usage

```java
Type2Enum type = Type2Enum.COLUMN_ALL;
SortByEnum sortBy = SortByEnum.DEFAULT;
SortOrderEnum sortOrder = SortOrderEnum.DEFAULT;

metadataController.getObjectHeaderAsync(type, null, null, null, sortBy, sortOrder, null, null, null, null, null).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Get Object Visualization Header

Use this endpoint to get header details of visualization charts for a given liveboard or answer. At least one of id or name of liveboard or answer is required. When both are given, then id will be considered.

```java
CompletableFuture<List<Object>> getObjectVisualizationHeaderAsync(
    final String id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `String` | Query, Required | The GUID of the liveboard or answer |

## Response Type

`List<Object>`

## Example Usage

```java
String id = "id0";

metadataController.getObjectVisualizationHeaderAsync(id).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Get Object Detail

Use this endpoint to get full details of metadata objects

```java
CompletableFuture<List<Object>> getObjectDetailAsync(
    final Type3Enum type,
    final List<String> id,
    final Boolean showHidden,
    final Boolean dropQuestionDetails,
    final String version)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | [`Type3Enum`](/doc/models/type-3-enum.md) | Query, Required | Type of the metadata object being searched. Valid values |
| `id` | `List<String>` | Query, Required | A JSON array of GUIDs of the objects. |
| `showHidden` | `Boolean` | Query, Optional | When set to true, returns details of the hidden objects, such as a column in a worksheet or a table. |
| `dropQuestionDetails` | `Boolean` | Query, Optional | When set to true, the search assist data associated with a worksheet is not included in the API response. This attribute is applicable only for LOGICAL_TABLE data type. |
| `version` | `String` | Query, Optional | Specify the version to retrieve the objects from. By default, the API returns metadata for all versions of the object. |

## Response Type

`List<Object>`

## Example Usage

```java
Type3Enum type = Type3Enum.DATAOBJECT;
List<String> id = new LinkedList<>();
id.add("id0");

metadataController.getObjectDetailAsync(type, id, null, null, null).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Export Object TML

To export ThoughtSpot objects represented in ThoughtSpot Modeling Language (TML), use this endpoint

```java
CompletableFuture<Object> exportObjectTMLAsync(
    final ApiRestV2MetadataTmlExportRequest body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiRestV2MetadataTmlExportRequest`](/doc/models/api-rest-v2-metadata-tml-export-request.md) | Body, Required | - |

## Response Type

`Object`

## Example Usage

```java
ApiRestV2MetadataTmlExportRequest body = new ApiRestV2MetadataTmlExportRequest();
body.setId(new LinkedList<>());
body.getId().add("id6");
body.getId().add("id7");

metadataController.exportObjectTMLAsync(body).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |


# Import Object TML

To import ThoughtSpot objects represented in ThoughtSpot Modeling Language (TML), use this endpoint

```java
CompletableFuture<Object> importObjectTMLAsync(
    final ApiRestV2MetadataTmlImportRequest body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ApiRestV2MetadataTmlImportRequest`](/doc/models/api-rest-v2-metadata-tml-import-request.md) | Body, Required | - |

## Response Type

`Object`

## Example Usage

```java
ApiRestV2MetadataTmlImportRequest body = new ApiRestV2MetadataTmlImportRequest();
body.setObjectTML(new LinkedList<>());
body.getObjectTML().add("objectTML5");
body.getObjectTML().add("objectTML6");

metadataController.importObjectTMLAsync(body).thenAccept(result -> {
    // TODO success callback handler
}).exceptionally(exception -> {
    // TODO failure callback handler
    return null;
});
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 500 | Operation failed or unauthorized request | [`ErrorResponseException`](/doc/models/error-response-exception.md) |

