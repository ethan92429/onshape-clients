/**
 * Onshape REST API
 * The Onshape REST API consumed by all clients.
 *
 * OpenAPI spec version: 1.93
 * Contact: api-support@onshape.zendesk.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export class BTCompanyUserParams {
    'email'?: string;
    'companyId'?: string;
    'admin'?: boolean;
    'guest'?: boolean;
    'light'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "email",
            "baseName": "email",
            "type": "string"
        },
        {
            "name": "companyId",
            "baseName": "companyId",
            "type": "string"
        },
        {
            "name": "admin",
            "baseName": "admin",
            "type": "boolean"
        },
        {
            "name": "guest",
            "baseName": "guest",
            "type": "boolean"
        },
        {
            "name": "light",
            "baseName": "light",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return BTCompanyUserParams.attributeTypeMap;
    }
}

