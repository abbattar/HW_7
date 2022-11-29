import pyodbc as pb

def get_drivers():
    msa_drivers = [x for x in pb.drivers() if 'ACCESS' in x.upper()]
    return msa_drivers

print(f'Access drivers: {get_drivers()}')