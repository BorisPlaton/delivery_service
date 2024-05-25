SAVE_ORDER_RESPONSES = {
    200: {
        'description': 'Existing order updated',
        'content': {
            'application/json': {
                'example': 1,
            }
        }

    },
    201: {
        'description': "New order created",
        'content': {
            'application/json': {
                'example': 2,
            }
        }
    },
}
