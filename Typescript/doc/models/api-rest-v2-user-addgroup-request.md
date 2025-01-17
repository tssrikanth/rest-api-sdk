
# Api Rest V2 User Addgroup Request

## Structure

`ApiRestV2UserAddgroupRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string \| undefined` | Optional | Username of the user account |
| `id` | `string \| undefined` | Optional | The GUID of the user account |
| `groups` | [`GroupNameAndIDInput[] \| undefined`](/doc/models/group-name-and-id-input.md) | Optional | A JSON array of group names or GUIDs or both. When both are given then id is considered |

## Example (as JSON)

```json
{
  "name": null,
  "id": null,
  "groups": null
}
```

