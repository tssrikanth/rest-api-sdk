
# Api Rest V2 Group Search Request

## Structure

`ApiRestV2GroupSearchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string \| undefined` | Optional | Name of the user group |
| `id` | `string \| undefined` | Optional | GUID of the group to update |
| `displayName` | `string \| undefined` | Optional | A unique display name string for the user group, for example, Developer group. |
| `visibility` | [`Visibility3Enum \| undefined`](/doc/models/visibility-3-enum.md) | Optional | The visibility attribute is set to DEFAULT when creating a group. Setting this to DEFAULT makes a group visible to other users and user groups, and thus allows them to share objects |
| `description` | `string \| undefined` | Optional | Description text for the group. |
| `privileges` | [`PrivilegeEnum[] \| undefined`](/doc/models/privilege-enum.md) | Optional | A JSON array of privileges assigned to the group |
| `groups` | [`GroupNameAndIDInput[] \| undefined`](/doc/models/group-name-and-id-input.md) | Optional | A JSON array of group names or GUIDs or both. When both are given then id is considered |
| `users` | [`UserNameAndIDInput[] \| undefined`](/doc/models/user-name-and-id-input.md) | Optional | A JSON array of name of users or GUIDs of users or both. When both are given then id is considered |
| `type` | [`Type7Enum \| undefined`](/doc/models/type-7-enum.md) | Optional | Type of user group. LOCAL_GROUP indicates that the user is created locally in the ThoughtSpot system. |

## Example (as JSON)

```json
{
  "name": null,
  "id": null,
  "displayName": null,
  "visibility": null,
  "description": null,
  "privileges": null,
  "groups": null,
  "users": null,
  "type": null
}
```

