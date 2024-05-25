from domain.order.controller.rest.v1.types.output.order import OrderOutput


GET_ORDER_RESPONSES = {
    200: {
        'description': 'Order exist',
        'model': OrderOutput,
    },
    204: {
        'description': "Order doesn't exist",
        'content': {
            'application/json': {
                'example': '',
            }
        }
    },
}
