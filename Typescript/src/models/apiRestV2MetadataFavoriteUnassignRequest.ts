/**
 * RESTAPI SDKLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

import { array, lazy, object, optional, Schema, string } from '../schema';
import { MetaObjectInput, metaObjectInputSchema } from './metaObjectInput';

export interface ApiRestV2MetadataFavoriteUnassignRequest {
  /** Name of the user */
  userName?: string;
  /** The GUID of the user */
  userId?: string;
  /** Metadata object details */
  metaObject: MetaObjectInput[];
}

export const apiRestV2MetadataFavoriteUnassignRequestSchema: Schema<ApiRestV2MetadataFavoriteUnassignRequest> = object(
  {
    userName: ['userName', optional(string())],
    userId: ['userId', optional(string())],
    metaObject: ['metaObject', array(lazy(() => metaObjectInputSchema))],
  }
);
