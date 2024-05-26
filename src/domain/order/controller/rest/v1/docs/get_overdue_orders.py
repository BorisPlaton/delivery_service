from domain.order.controller.rest.v1.types.output.order import OverdueOrderOutput


GET_OVERDUE_ORDERS_RESPONSES = {
    200: {
        'description': 'Overdue orders exist',
        'model': list[OverdueOrderOutput],
    },
    204: {
        'description': "Not overdue orders exist",
        'content': {
            'application/json': {
                'example': '',
            }
        }
    },
}
