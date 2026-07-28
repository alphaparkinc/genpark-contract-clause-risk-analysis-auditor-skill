from client import ContractAuditorClient

def main():
    client = ContractAuditorClient()
    res = client.audit_contract(contract_text='Indemnity clause unlimited liability')
    print(f"Result for risk_level: {res['risk_level']}")

if __name__ == "__main__":
    main()
