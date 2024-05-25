from domain.company.controller.rest.v1.types.output.company import CompanyOutput


GET_COMPANY_RESPONSES = {
    200: {
        'description': 'Company exist',
        'model': CompanyOutput,
    },
    204: {
        'description': "Company doesn't exist",
        'content': {
            'application/json': {
                'example': '',
            }
        }
    },
}

