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


export class BTCustomPropertyDefinitionParams {
    'name'?: string;
    'type'?: BTCustomPropertyDefinitionParams.TypeEnum;
    'description'?: string;
    'enumDefinition'?: Array<string>;
    'template'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "type",
            "baseName": "type",
            "type": "BTCustomPropertyDefinitionParams.TypeEnum"
        },
        {
            "name": "description",
            "baseName": "description",
            "type": "string"
        },
        {
            "name": "enumDefinition",
            "baseName": "enumDefinition",
            "type": "Array<string>"
        },
        {
            "name": "template",
            "baseName": "template",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return BTCustomPropertyDefinitionParams.attributeTypeMap;
    }
}

export namespace BTCustomPropertyDefinitionParams {
    export enum TypeEnum {
        STRING = <any> 'STRING',
        NUMBER = <any> 'NUMBER',
        INTEGER = <any> 'INTEGER',
        BOOLEAN = <any> 'BOOLEAN',
        DATE = <any> 'DATE',
        ENUM = <any> 'ENUM',
        BLOB = <any> 'BLOB',
        OBJECT = <any> 'OBJECT',
        ARRAY = <any> 'ARRAY',
        UNKNOWN = <any> 'UNKNOWN'
    }
}
