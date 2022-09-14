class solution:
    
    #1. Crear método inicializador de la clase
    def __init__(self):
        #2. Declaración de variables
        self.estructura = {}
        self.Line = {}
        self.ExpenseDetail = {}
        self.customer = {}
        self.Ref = {}
        self.Address = {}

    def llenar_Address(self):
        codigos = [170002, 170001, 170003, 170004]
        self.Address = {'city': 'Manizales', 'code_zip': codigos}

    def llenar_Ref(self):
        self.llenar_Address()
        self.Ref = {'value': 'DEF34', 'name': 'Sample Construction', 'Address': self.Address}

    def llenar_customer(self):
        self.llenar_Ref()
        self.customer = {'value': 'ABC123', 'name': 'Sample Customer', 'Ref': self.Ref}

    def llenar_ExpenseDetail(self):
        self.llenar_customer()
        self.ExpenseDetail = {'Custumer': self.customer, 'LineStatus': 'Billable'}

    def llenar_Line(self):
        self.llenar_ExpenseDetail()
        self.Line = {'Description': 'Sample Expense', 'Amount': 500, 'DetailType': 'ExpenseDetail', 'ExpenseDetail': self.ExpenseDetail}

    def llenar_estructura(self):
        self.llenar_Line()
        self.estructura = {'DueDate': '2022-02-24', 'Balance': 1990.19, 'DocNumber': 1053811422, 'Status': 'Payable', 'Line': self.Line, 'TotalAmt': 1990.19}
        self.imprimir_estructura()

    def imprimir_estructura(self):
        print(self.estructura)
