
# Api Rest V2 User Update Request

## Structure

`ApiRestV2UserUpdateRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Name` | `String` | Optional | Name of the user account. The username string must be unique. | String getName() | setName(String name) |
| `Id` | `String` | Optional | The GUID of the user account | String getId() | setId(String id) |
| `DisplayName` | `String` | Optional | A display name string for the user, usually their first and last name. | String getDisplayName() | setDisplayName(String displayName) |
| `Visibility` | [`VisibilityEnum`](/doc/models/visibility-enum.md) | Optional | Visibility of the user. The visibility attribute is set to DEFAULT when creating a user. Setting this to DEFAULT makes a user visible to other users and user groups, and thus allows them to share objects<br>**Default**: `VisibilityEnum.DEFAULT` | VisibilityEnum getVisibility() | setVisibility(VisibilityEnum visibility) |
| `Mail` | `String` | Optional | Email id associated with the user account | String getMail() | setMail(String mail) |
| `Password` | `String` | Optional | Password for the user account. | String getPassword() | setPassword(String password) |
| `State` | [`StateEnum`](/doc/models/state-enum.md) | Optional | Status of user account. acitve or inactive.<br>**Default**: `StateEnum.ACTIVE` | StateEnum getState() | setState(StateEnum state) |
| `NotifyOnShare` | `Boolean` | Optional | User preference for receiving email notifications when another ThoughtSpot user shares answers or pinboards.<br>**Default**: `true` | Boolean getNotifyOnShare() | setNotifyOnShare(Boolean notifyOnShare) |
| `ShowWalkMe` | `Boolean` | Optional | The user preference for revisiting the onboarding experience.<br>**Default**: `true` | Boolean getShowWalkMe() | setShowWalkMe(Boolean showWalkMe) |
| `AnalystOnboardingComplete` | `Boolean` | Optional | ThoughtSpot provides an interactive guided walkthrough to onboard new users. The onboarding experience leads users through a set of actions to help users get started and accomplish their tasks quickly. The users can turn off the Onboarding experience and access it again when they need assistance with the ThoughtSpot UI.<br>**Default**: `true` | Boolean getAnalystOnboardingComplete() | setAnalystOnboardingComplete(Boolean analystOnboardingComplete) |
| `Type` | [`Type4Enum`](/doc/models/type-4-enum.md) | Optional | Type of user. LOCAL_USER indicates that the user is created locally in the ThoughtSpot system.<br>**Default**: `Type4Enum.LOCAL_USER` | Type4Enum getType() | setType(Type4Enum type) |
| `Groups` | [`List<GroupNameAndIDInput>`](/doc/models/group-name-and-id-input.md) | Optional | A JSON array of group names or GUIDs or both. When both are given then id is considered | List<GroupNameAndIDInput> getGroups() | setGroups(List<GroupNameAndIDInput> groups) |

## Example (as JSON)

```json
{
  "name": null,
  "id": null,
  "displayName": null,
  "visibility": null,
  "mail": null,
  "password": null,
  "state": null,
  "notifyOnShare": null,
  "showWalkMe": null,
  "analystOnboardingComplete": null,
  "type": null,
  "groups": null
}
```

