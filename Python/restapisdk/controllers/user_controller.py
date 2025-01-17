# -*- coding: utf-8 -*-

"""
restapisdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from restapisdk.api_helper import APIHelper
from restapisdk.configuration import Server
from restapisdk.controllers.base_controller import BaseController
from restapisdk.http.auth.o_auth_2 import OAuth2
from restapisdk.models.user_response import UserResponse
from restapisdk.exceptions.error_response_exception import ErrorResponseException


class UserController(BaseController):

    """A Controller to access Endpoints in the restapisdk API."""

    def __init__(self, config, call_back=None):
        super(UserController, self).__init__(config, call_back)

    def get_user(self,
                 name=None,
                 id=None):
        """Does a GET request to /api/rest/v2/user.

        To get the details of a specific user account by username or user id,
        use this endpoint. At Least one value is needed. When both are
        given,then user id will be considered to fetch user information

        Args:
            name (string, optional): Username of the user that you want to
                query
            id (string, optional): The GUID of the user account to query

        Returns:
            UserResponse: Response from the API. Details of the user

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/user'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'name': name,
            'id': id
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': self.config.content_type
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, UserResponse.from_dictionary)

        return decoded

    def create_user(self,
                    body):
        """Does a POST request to /api/rest/v2/user/create.

        To programmatically create a user account in the ThoughtSpot system,
        use this API endpoint. Using this API, you can create a user and
        assign groups. To create a user, you require admin user privileges.
        All users created in the ThoughtSpot system are added to ALL_GROUP

        Args:
            body (ApiRestV2UserCreateRequest): TODO: type description here.

        Returns:
            UserResponse: Response from the API. Details of the user created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/user/create'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, UserResponse.from_dictionary)

        return decoded

    def update_user(self,
                    body):
        """Does a PUT request to /api/rest/v2/user/update.

        You can use this endpoint to programmatically modify an existing user
        account. To modify a user, you require admin user privileges. At least
        one of User Id or username is mandatory. When both are given, then
        user id will be considered and username will be updated

        Args:
            body (ApiRestV2UserUpdateRequest): TODO: type description here.

        Returns:
            bool: Response from the API. User successfully updated

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/user/update'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text == 'true'

        return decoded

    def delete_user(self,
                    name=None,
                    id=None):
        """Does a DELETE request to /api/rest/v2/user/delete.

        To remove a user from the ThoughtSpot system, use this endpoint. At
        least one value is needed. When both are given, then user id will be
        considered to delete user.

        Args:
            name (string, optional): Username of the user account
            id (string, optional): The GUID of the user account

        Returns:
            bool: Response from the API. User successfully deleted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/user/delete'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'name': name,
            'id': id
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': self.config.content_type
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text == 'true'

        return decoded

    def add_groups_to_user(self,
                           body):
        """Does a PUT request to /api/rest/v2/user/addgroup.

        To programmatically add groups to an existing ThoughtSpot user, use
        this endpoint. When you assign groups to a user, the user inherits the
        privileges assigned to those groups. At least one of user Id or
        username is mandatory. When both are given, then user id will be
        considered.

        Args:
            body (ApiRestV2UserAddgroupRequest): TODO: type description here.

        Returns:
            bool: Response from the API. Successfully assigned groups to the
                user

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/user/addgroup'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text == 'true'

        return decoded

    def remove_groups_from_user(self,
                                body):
        """Does a PUT request to /api/rest/v2/user/removegroup.

        To programmatically remove groups from an existing ThoughtSpot user,
        use this API endpoint. The API removes only the user association. It
        does not delete the user or group from the Thoughtspot system. At
        least one of user id or username is mandatory. When both are given,
        then user id will be considered.

        Args:
            body (ApiRestV2UserRemovegroupRequest): TODO: type description
                here.

        Returns:
            bool: Response from the API. Successfully removed groups for the
                user

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/user/removegroup'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = _response.text == 'true'

        return decoded

    def search_users(self,
                     body):
        """Does a POST request to /api/rest/v2/user/search.

        To get the details of a specific user account or all users in the
        ThoughtSpot system, use this endpoint. If no input is provided, then
        all user are included in the response.

        Args:
            body (ApiRestV2UserSearchRequest): TODO: type description here.

        Returns:
            list of UserResponse: Response from the API. Array of user details
                matching the search criteria

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/rest/v2/user/search'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 500:
            raise ErrorResponseException('Operation failed or unauthorized request', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, UserResponse.from_dictionary)

        return decoded
