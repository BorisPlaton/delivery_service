from domain.company.controller.rest.v1.types.output.order import CompanyOrderOutput


GET_COMPANY_ORDERS_RESPONSES = {
    200: {
        'description': 'Company has orders',
        'model': list[CompanyOrderOutput],
    },
    204: {
        'description': "Company doesn't have orders or company doesn't exist",
        'content': {
            'application/json': {
                'example': '',
            }
        }
    },
}

