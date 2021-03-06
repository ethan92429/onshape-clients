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


export class BTUserWebPreferencesParams {
    'id'?: string;
    'userId'?: string;
    'preferenceName'?: string;
    'retinaDisplaySetting'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "userId",
            "baseName": "userId",
            "type": "string"
        },
        {
            "name": "preferenceName",
            "baseName": "preferenceName",
            "type": "string"
        },
        {
            "name": "retinaDisplaySetting",
            "baseName": "retinaDisplaySetting",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return BTUserWebPreferencesParams.attributeTypeMap;
    }
}

