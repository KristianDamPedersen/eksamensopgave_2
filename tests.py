# Det her dokument er for tests.
#import '../elements/import_data' as impd

def test_import_nations():
    pass
    Lines = impd.nations.readlines()
    for line in Lines:
        print('Line: {}'.format(line.strip()))