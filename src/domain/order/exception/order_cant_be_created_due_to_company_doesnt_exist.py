from shared.exception.not_found import NotFound


class OrderCantBeCreatedDueToCompanyDoesNotExist(NotFound):
    DETAIL = "Order can't be created due to company doesn't exist."

    def __init__(self):
        super().__init__(self.DETAIL)
