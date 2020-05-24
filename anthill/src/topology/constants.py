

class Schema:

    NEST_SCHEMA = {
        "type": "object",
        "properties": {
            "node": {
                "type": "array",
                "items": [
                    {
                        "type": "object",
                        "properties": {
                            "rule": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "rule"
                        ]
                    }
                ]
            }
        },
        "required": [
            "node"
        ]
    }


class Options:

    DEPENDS_ON = "depends_on"
