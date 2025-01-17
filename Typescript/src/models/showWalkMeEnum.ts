/**
 * RESTAPI SDKLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

import { Schema, stringEnum } from '../schema';

/**
 * Enum for ShowWalkMeEnum
 */
export enum ShowWalkMeEnum {
  True = 'True',
  False = 'False',
}

/**
 * Schema for ShowWalkMeEnum
 */
export const showWalkMeEnumSchema: Schema<ShowWalkMeEnum> = stringEnum(ShowWalkMeEnum);
