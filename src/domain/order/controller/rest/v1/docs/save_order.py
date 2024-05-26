from domain.order.exception.order_cant_be_created_due_to_company_doesnt_exist import \
    OrderCantBeCreatedDueToCompanyDoesNotExist


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
    404: {
        'description': 'If order saves data with not existing company.',
        'content': {
            'application/json': {
                'example': {
                    'detail': OrderCantBeCreatedDueToCompanyDoesNotExist.DETAIL,
                },
            }
        }
    }
}
