import pandas as pd

def test_csv_create():
    excel_data = 'ЗАКУПКИ.xlsx'
    df = pd.read_excel(excel_data,sheet_name='исходник')
    #print(df.columns.tolist())
    name_from_excel = df.iloc[4:, 2].astype(str)
    external_code_from_excel = df.iloc[4:, 1].astype(str)
    price_from_excel = df.iloc[4:, 7].astype(float).apply(lambda x: round(x, 2)).astype(str)
    purchase_price_from_excel = df.iloc[4:, 8].astype(float).apply(lambda x: round(x, 2)).astype(str)
    name_from_excel.replace('nan', '', inplace=True)
    external_code_from_excel.replace('nan', '', inplace=True)

    csv_data = pd.DataFrame(columns=['ID', 'EXTERNAL_CODE', 'EXTERNAL_ID', 'NAME', 'FEATURES', 'PRICE',
                                         'BARCODE', 'VENDOR_CODE', 'NDS', 'PAYMENT_SUBJECT', 'GROUP',
                                         'UNIT_CODE', 'PURCHASE_PRICE', 'WEIGHTED', 'ALCOHOL', 'GTIN',
                                         'MARK_TYPE', 'GROUPED', 'CONTAINER', 'MODIFIERS', 'INGREDIENTS',
                                         'GOOD_TYPE', 'CONTRACTOR_INN', 'CONTRACTOR_ACTIVITY_TYPE',
                                         'COUNTY_CODE', 'CUSTOM_DECLARATION', 'PLU_CODE', 'ORG_MEMBER_POINTS'])
    csv_data.to_csv('nomenclatures.csv', index=False, sep=';', encoding='cp1251')

    csv_data['NAME'] = name_from_excel
    csv_data['EXTERNAL_CODE'] = external_code_from_excel
    csv_data['PRICE'] = price_from_excel
    csv_data['PURCHASE_PRICE'] = purchase_price_from_excel
    csv_data['GOOD_TYPE'] = 'DEFAULT'
    csv_data['MARK_TYPE'] = 0
    csv_data['PAYMENT_SUBJECT'] = 1
    csv_data['UNIT_CODE'] = 796

    csv_file_path = 'nomenclatures.csv'
    with open(csv_file_path, 'w', encoding='cp1251', errors='replace', newline='') as file:
        csv_data.to_csv(file, index=False, sep=';')







