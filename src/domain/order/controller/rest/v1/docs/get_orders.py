GET_ORDERS_RESPONSES = {
    200: {
        'description': """
1. Some orders exist
2. No orders exist
        """,
        'content': {
            'application/json': {
                'examples': {
                    'Some orders exist': {
                        'value': None,
                    },
                    'No orders exist': {
                        'value': [],
                    }
                },
            }
        }
    },
}
