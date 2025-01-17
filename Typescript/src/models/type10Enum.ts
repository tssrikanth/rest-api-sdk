/**
 * RESTAPI SDKLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

import { Schema, stringEnum } from '../schema';

/**
 * Enum for Type10Enum
 */
export enum Type10Enum {
  LIVEBOARD = 'LIVEBOARD',
  DATAOBJECT = 'DATAOBJECT',
  COLUMN = 'COLUMN',
  JOIN = 'JOIN',
}

/**
 * Schema for Type10Enum
 */
export const type10EnumSchema: Schema<Type10Enum> = stringEnum(Type10Enum);
