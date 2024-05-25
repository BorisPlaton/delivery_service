SAVE_COMPANY_RESPONSES = {
    200: {
        'description': 'Existing company updated',
        'content': {
            'application/json': {
                'example': 1,
            }
        }

    },
    201: {
        'description': "New company created",
        'content': {
            'application/json': {
                'example': 2,
            }
        }
    },
}
