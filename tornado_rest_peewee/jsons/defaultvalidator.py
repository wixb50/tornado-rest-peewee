# @Author: xiewenqian <int>
# @Date:   2016-08-26T17:54:26+08:00
# @Email:  wixb50@gmail.com
# @Last modified by:   int
# @Last modified time: 2016-09-09T16:42:04+08:00


from jsonschema import Draft4Validator, validators


def extend_with_default(validator_class):
    validate_properties = validator_class.VALIDATORS["properties"]

    def set_defaults(validator, properties, instance, schema):
        for error in validate_properties(
            validator, properties, instance, schema,
        ):
            yield error

        for property, subschema in properties.items():
            if "default" in subschema:
                instance.setdefault(property, subschema["default"])

    return validators.extend(
        validator_class, {"properties" : set_defaults},
    )


DefaultDraft4Validator = extend_with_default(Draft4Validator)
