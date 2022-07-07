import openpyxl as pyxl


def get_url(column_name):
    try:
        workbook = pyxl.load_workbook("TestData.xlsx")
        sheet = workbook.active
        cell = sheet[column_name].value
        workbook.close()
        return cell
    except FileNotFoundError as ex:
        print("Exception!!.Testdata file is Missing or invalid filename used. ", str(ex))


