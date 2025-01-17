/*
 * RESTAPISDKLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

package localhost.models;

import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonSetter;
import java.util.List;

/**
 * This is a model class for ApiRestV2UserUpdateRequest type.
 */
public class ApiRestV2UserUpdateRequest {
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private String name;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private String id;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private String displayName;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private VisibilityEnum visibility;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private String mail;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private String password;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private StateEnum state;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private Boolean notifyOnShare;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private Boolean showWalkMe;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private Boolean analystOnboardingComplete;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private Type4Enum type;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private List<GroupNameAndIDInput> groups;

    /**
     * Default constructor.
     */
    public ApiRestV2UserUpdateRequest() {
        visibility = VisibilityEnum.DEFAULT;
        state = StateEnum.ACTIVE;
        notifyOnShare = true;
        showWalkMe = true;
        analystOnboardingComplete = true;
        type = Type4Enum.LOCAL_USER;
    }

    /**
     * Initialization constructor.
     * @param  name  String value for name.
     * @param  id  String value for id.
     * @param  displayName  String value for displayName.
     * @param  visibility  VisibilityEnum value for visibility.
     * @param  mail  String value for mail.
     * @param  password  String value for password.
     * @param  state  StateEnum value for state.
     * @param  notifyOnShare  Boolean value for notifyOnShare.
     * @param  showWalkMe  Boolean value for showWalkMe.
     * @param  analystOnboardingComplete  Boolean value for analystOnboardingComplete.
     * @param  type  Type4Enum value for type.
     * @param  groups  List of GroupNameAndIDInput value for groups.
     */
    public ApiRestV2UserUpdateRequest(
            String name,
            String id,
            String displayName,
            VisibilityEnum visibility,
            String mail,
            String password,
            StateEnum state,
            Boolean notifyOnShare,
            Boolean showWalkMe,
            Boolean analystOnboardingComplete,
            Type4Enum type,
            List<GroupNameAndIDInput> groups) {
        this.name = name;
        this.id = id;
        this.displayName = displayName;
        this.visibility = visibility;
        this.mail = mail;
        this.password = password;
        this.state = state;
        this.notifyOnShare = notifyOnShare;
        this.showWalkMe = showWalkMe;
        this.analystOnboardingComplete = analystOnboardingComplete;
        this.type = type;
        this.groups = groups;
    }

    /**
     * Getter for Name.
     * Name of the user account. The username string must be unique.
     * @return Returns the String
     */
    @JsonGetter("name")
    public String getName() {
        return name;
    }

    /**
     * Setter for Name.
     * Name of the user account. The username string must be unique.
     * @param name Value for String
     */
    @JsonSetter("name")
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Getter for Id.
     * The GUID of the user account
     * @return Returns the String
     */
    @JsonGetter("id")
    public String getId() {
        return id;
    }

    /**
     * Setter for Id.
     * The GUID of the user account
     * @param id Value for String
     */
    @JsonSetter("id")
    public void setId(String id) {
        this.id = id;
    }

    /**
     * Getter for DisplayName.
     * A display name string for the user, usually their first and last name.
     * @return Returns the String
     */
    @JsonGetter("displayName")
    public String getDisplayName() {
        return displayName;
    }

    /**
     * Setter for DisplayName.
     * A display name string for the user, usually their first and last name.
     * @param displayName Value for String
     */
    @JsonSetter("displayName")
    public void setDisplayName(String displayName) {
        this.displayName = displayName;
    }

    /**
     * Getter for Visibility.
     * Visibility of the user. The visibility attribute is set to DEFAULT when creating a user.
     * Setting this to DEFAULT makes a user visible to other users and user groups, and thus allows
     * them to share objects
     * @return Returns the VisibilityEnum
     */
    @JsonGetter("visibility")
    public VisibilityEnum getVisibility() {
        return visibility;
    }

    /**
     * Setter for Visibility.
     * Visibility of the user. The visibility attribute is set to DEFAULT when creating a user.
     * Setting this to DEFAULT makes a user visible to other users and user groups, and thus allows
     * them to share objects
     * @param visibility Value for VisibilityEnum
     */
    @JsonSetter("visibility")
    public void setVisibility(VisibilityEnum visibility) {
        this.visibility = visibility;
    }

    /**
     * Getter for Mail.
     * Email id associated with the user account
     * @return Returns the String
     */
    @JsonGetter("mail")
    public String getMail() {
        return mail;
    }

    /**
     * Setter for Mail.
     * Email id associated with the user account
     * @param mail Value for String
     */
    @JsonSetter("mail")
    public void setMail(String mail) {
        this.mail = mail;
    }

    /**
     * Getter for Password.
     * Password for the user account.
     * @return Returns the String
     */
    @JsonGetter("password")
    public String getPassword() {
        return password;
    }

    /**
     * Setter for Password.
     * Password for the user account.
     * @param password Value for String
     */
    @JsonSetter("password")
    public void setPassword(String password) {
        this.password = password;
    }

    /**
     * Getter for State.
     * Status of user account. acitve or inactive.
     * @return Returns the StateEnum
     */
    @JsonGetter("state")
    public StateEnum getState() {
        return state;
    }

    /**
     * Setter for State.
     * Status of user account. acitve or inactive.
     * @param state Value for StateEnum
     */
    @JsonSetter("state")
    public void setState(StateEnum state) {
        this.state = state;
    }

    /**
     * Getter for NotifyOnShare.
     * User preference for receiving email notifications when another ThoughtSpot user shares
     * answers or pinboards.
     * @return Returns the Boolean
     */
    @JsonGetter("notifyOnShare")
    public Boolean getNotifyOnShare() {
        return notifyOnShare;
    }

    /**
     * Setter for NotifyOnShare.
     * User preference for receiving email notifications when another ThoughtSpot user shares
     * answers or pinboards.
     * @param notifyOnShare Value for Boolean
     */
    @JsonSetter("notifyOnShare")
    public void setNotifyOnShare(Boolean notifyOnShare) {
        this.notifyOnShare = notifyOnShare;
    }

    /**
     * Getter for ShowWalkMe.
     * The user preference for revisiting the onboarding experience.
     * @return Returns the Boolean
     */
    @JsonGetter("showWalkMe")
    public Boolean getShowWalkMe() {
        return showWalkMe;
    }

    /**
     * Setter for ShowWalkMe.
     * The user preference for revisiting the onboarding experience.
     * @param showWalkMe Value for Boolean
     */
    @JsonSetter("showWalkMe")
    public void setShowWalkMe(Boolean showWalkMe) {
        this.showWalkMe = showWalkMe;
    }

    /**
     * Getter for AnalystOnboardingComplete.
     * ThoughtSpot provides an interactive guided walkthrough to onboard new users. The onboarding
     * experience leads users through a set of actions to help users get started and accomplish
     * their tasks quickly. The users can turn off the Onboarding experience and access it again
     * when they need assistance with the ThoughtSpot UI.
     * @return Returns the Boolean
     */
    @JsonGetter("analystOnboardingComplete")
    public Boolean getAnalystOnboardingComplete() {
        return analystOnboardingComplete;
    }

    /**
     * Setter for AnalystOnboardingComplete.
     * ThoughtSpot provides an interactive guided walkthrough to onboard new users. The onboarding
     * experience leads users through a set of actions to help users get started and accomplish
     * their tasks quickly. The users can turn off the Onboarding experience and access it again
     * when they need assistance with the ThoughtSpot UI.
     * @param analystOnboardingComplete Value for Boolean
     */
    @JsonSetter("analystOnboardingComplete")
    public void setAnalystOnboardingComplete(Boolean analystOnboardingComplete) {
        this.analystOnboardingComplete = analystOnboardingComplete;
    }

    /**
     * Getter for Type.
     * Type of user. LOCAL_USER indicates that the user is created locally in the ThoughtSpot
     * system.
     * @return Returns the Type4Enum
     */
    @JsonGetter("type")
    public Type4Enum getType() {
        return type;
    }

    /**
     * Setter for Type.
     * Type of user. LOCAL_USER indicates that the user is created locally in the ThoughtSpot
     * system.
     * @param type Value for Type4Enum
     */
    @JsonSetter("type")
    public void setType(Type4Enum type) {
        this.type = type;
    }

    /**
     * Getter for Groups.
     * A JSON array of group names or GUIDs or both. When both are given then id is considered
     * @return Returns the List of GroupNameAndIDInput
     */
    @JsonGetter("groups")
    public List<GroupNameAndIDInput> getGroups() {
        return groups;
    }

    /**
     * Setter for Groups.
     * A JSON array of group names or GUIDs or both. When both are given then id is considered
     * @param groups Value for List of GroupNameAndIDInput
     */
    @JsonSetter("groups")
    public void setGroups(List<GroupNameAndIDInput> groups) {
        this.groups = groups;
    }

    /**
     * Converts this ApiRestV2UserUpdateRequest into string format.
     * @return String representation of this class
     */
    @Override
    public String toString() {
        return "ApiRestV2UserUpdateRequest [" + "name=" + name + ", id=" + id + ", displayName="
                + displayName + ", visibility=" + visibility + ", mail=" + mail + ", password="
                + password + ", state=" + state + ", notifyOnShare=" + notifyOnShare
                + ", showWalkMe=" + showWalkMe + ", analystOnboardingComplete="
                + analystOnboardingComplete + ", type=" + type + ", groups=" + groups + "]";
    }

    /**
     * Builds a new {@link ApiRestV2UserUpdateRequest.Builder} object.
     * Creates the instance with the state of the current model.
     * @return a new {@link ApiRestV2UserUpdateRequest.Builder} object
     */
    public Builder toBuilder() {
        Builder builder = new Builder()
                .name(getName())
                .id(getId())
                .displayName(getDisplayName())
                .visibility(getVisibility())
                .mail(getMail())
                .password(getPassword())
                .state(getState())
                .notifyOnShare(getNotifyOnShare())
                .showWalkMe(getShowWalkMe())
                .analystOnboardingComplete(getAnalystOnboardingComplete())
                .type(getType())
                .groups(getGroups());
        return builder;
    }

    /**
     * Class to build instances of {@link ApiRestV2UserUpdateRequest}.
     */
    public static class Builder {
        private String name;
        private String id;
        private String displayName;
        private VisibilityEnum visibility = VisibilityEnum.DEFAULT;
        private String mail;
        private String password;
        private StateEnum state = StateEnum.ACTIVE;
        private Boolean notifyOnShare = true;
        private Boolean showWalkMe = true;
        private Boolean analystOnboardingComplete = true;
        private Type4Enum type = Type4Enum.LOCAL_USER;
        private List<GroupNameAndIDInput> groups;



        /**
         * Setter for name.
         * @param  name  String value for name.
         * @return Builder
         */
        public Builder name(String name) {
            this.name = name;
            return this;
        }

        /**
         * Setter for id.
         * @param  id  String value for id.
         * @return Builder
         */
        public Builder id(String id) {
            this.id = id;
            return this;
        }

        /**
         * Setter for displayName.
         * @param  displayName  String value for displayName.
         * @return Builder
         */
        public Builder displayName(String displayName) {
            this.displayName = displayName;
            return this;
        }

        /**
         * Setter for visibility.
         * @param  visibility  VisibilityEnum value for visibility.
         * @return Builder
         */
        public Builder visibility(VisibilityEnum visibility) {
            this.visibility = visibility;
            return this;
        }

        /**
         * Setter for mail.
         * @param  mail  String value for mail.
         * @return Builder
         */
        public Builder mail(String mail) {
            this.mail = mail;
            return this;
        }

        /**
         * Setter for password.
         * @param  password  String value for password.
         * @return Builder
         */
        public Builder password(String password) {
            this.password = password;
            return this;
        }

        /**
         * Setter for state.
         * @param  state  StateEnum value for state.
         * @return Builder
         */
        public Builder state(StateEnum state) {
            this.state = state;
            return this;
        }

        /**
         * Setter for notifyOnShare.
         * @param  notifyOnShare  Boolean value for notifyOnShare.
         * @return Builder
         */
        public Builder notifyOnShare(Boolean notifyOnShare) {
            this.notifyOnShare = notifyOnShare;
            return this;
        }

        /**
         * Setter for showWalkMe.
         * @param  showWalkMe  Boolean value for showWalkMe.
         * @return Builder
         */
        public Builder showWalkMe(Boolean showWalkMe) {
            this.showWalkMe = showWalkMe;
            return this;
        }

        /**
         * Setter for analystOnboardingComplete.
         * @param  analystOnboardingComplete  Boolean value for analystOnboardingComplete.
         * @return Builder
         */
        public Builder analystOnboardingComplete(Boolean analystOnboardingComplete) {
            this.analystOnboardingComplete = analystOnboardingComplete;
            return this;
        }

        /**
         * Setter for type.
         * @param  type  Type4Enum value for type.
         * @return Builder
         */
        public Builder type(Type4Enum type) {
            this.type = type;
            return this;
        }

        /**
         * Setter for groups.
         * @param  groups  List of GroupNameAndIDInput value for groups.
         * @return Builder
         */
        public Builder groups(List<GroupNameAndIDInput> groups) {
            this.groups = groups;
            return this;
        }

        /**
         * Builds a new {@link ApiRestV2UserUpdateRequest} object using the set fields.
         * @return {@link ApiRestV2UserUpdateRequest}
         */
        public ApiRestV2UserUpdateRequest build() {
            return new ApiRestV2UserUpdateRequest(name, id, displayName, visibility, mail, password,
                    state, notifyOnShare, showWalkMe, analystOnboardingComplete, type, groups);
        }
    }
}
