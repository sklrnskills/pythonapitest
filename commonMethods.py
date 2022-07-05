import openpyxl as pyxl


def get_url(column_name):
    try:
        workbook = pyxl.load_workbook("TestData.xlsx")
        sheet = workbook.active
        cell = sheet[column_name].value
        workbook.close()
        return cell
    except FileNotFoundError as ex:
        print("Exception!!.Testdata file maybe Missing. ", str(ex))


