GET_COMPANIES_RESPONSES = {
    200: {
        'description': """
1. Some companies exist
2. No companies exist
        """,
        'content': {
            'application/json': {
                'examples': {
                    'Some companies exist': {
                        'value': None,
                    },
                    'No companies exist': {
                        'value': [],
                    }
                },
            }
        }
    },
}
